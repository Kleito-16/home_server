import os
import time
import random
import math

# --- Configuration ---
TERMINAL_WIDTH = 120  # Adjust to your terminal width
TERMINAL_HEIGHT = 240 # Adjust to your terminal height
FOV = 2050.0  # Field of View, affects perspective. Higher values = less perspective
BASE_DIAMETER = 16 # "Diameter" in characters when sphere is at reference z-depth
CHAR_ASPECT_RATIO = 2.0 # Characters are often ~2x taller than wide, adjust as needed

# Movement Box (3D)
MIN_X, MAX_X = -50, 50
MIN_Y, MAX_Y = -30, 30
MIN_Z, MAX_Z = 10, 150 # Z > 0; closer to FOV value is "closer" to screen

# --- ANSI Colors ---
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_RESET = "\033[0m"
SPHERE_CHAR = "●" # Or use '@', '#', 'O' etc.

# --- Utility Functions ---
def clear_terminal():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Sphere:
    def __init__(self, x, y, z, dx, dy, dz, color, base_diameter):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.color = color
        self.base_diameter = base_diameter
        self.char = SPHERE_CHAR

    def update_position(self):
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

        # Bounce off walls
        if not MIN_X < self.x < MAX_X:
            self.dx *= -1
            self.x = max(MIN_X + 1, min(self.x, MAX_X -1))
        if not MIN_Y < self.y < MAX_Y:
            self.dy *= -1
            self.y = max(MIN_Y + 1, min(self.y, MAX_Y-1))
        if not MIN_Z < self.z < MAX_Z:
            self.dz *= -1
            self.z = max(MIN_Z + 1, min(self.z, MAX_Z-1)) # Ensure z > 0

        # Randomly change direction sometimes
        if random.random() < 0.02: # 2% chance each frame
            self.dx = random.choice([-1, 1]) * random.uniform(0.5, 1.5)
        if random.random() < 0.02:
            self.dy = random.choice([-1, 1]) * random.uniform(0.5, 1.5)
        if random.random() < 0.02:
            self.dz = random.choice([-1, 1]) * random.uniform(0.5, 1.5)


def project_to_screen(x_3d, y_3d, z_3d, diameter_3d):
    """Projects 3D coordinates and diameter to 2D screen coordinates and size."""
    if z_3d <= 0: # Avoid division by zero or negative z
        return None, None, 0 # Not visible or behind camera

    scale_factor = FOV / (FOV + z_3d)

    screen_x = int(x_3d * scale_factor + TERMINAL_WIDTH / 2)
    screen_y = int(y_3d * scale_factor / CHAR_ASPECT_RATIO + TERMINAL_HEIGHT / 2) # Adjust for char aspect ratio
    projected_diameter = int(diameter_3d * scale_factor)

    return screen_x, screen_y, max(1, projected_diameter) # Ensure diameter is at least 1

def draw_spheres_to_buffer(spheres, buffer):
    """Draws spheres onto the character buffer, handling depth."""
    # Sort spheres by Z-coordinate (further away first)
    sorted_spheres = sorted(spheres, key=lambda s: s.z, reverse=True)

    for sphere in sorted_spheres:
        screen_x, screen_y, projected_diameter = project_to_screen(
            sphere.x, sphere.y, sphere.z, sphere.base_diameter
        )

        if screen_x is None: # Sphere is behind or too close to camera plane
            continue

        # For simplicity, draw a character block. A true circle is harder.
        # The "projected_diameter" here will define the width.
        # Height will be roughly half to account for character aspect ratio for a more circular look.
        sphere_width = projected_diameter
        sphere_height = max(1, int(projected_diameter / CHAR_ASPECT_RATIO))

        start_col = screen_x - sphere_width // 2
        end_col = start_col + sphere_width
        start_row = screen_y - sphere_height // 2
        end_row = start_row + sphere_height

        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                # Basic check to make it slightly more "circular" by checking distance
                # from center of the drawn rectangle. This is a very rough approximation.
                dist_x = (c - start_col) - sphere_width / 2 + 0.5
                dist_y = ((r - start_row) - sphere_height / 2 + 0.5) * CHAR_ASPECT_RATIO # adjust for aspect ratio
                
                # Simple elliptical check for drawing characters
                # (dist_x / (sphere_width/2))^2 + (dist_y / (sphere_height*CHAR_ASPECT_RATIO/2))^2 <= 1
                # Simplified: if (dist_x**2 / (sphere_width/2)**2 if sphere_width > 0 else 0) + \
                #    (dist_y**2 / (sphere_height/2)**2 if sphere_height > 0 else 0) <= 1.2: # 1.2 for a bit more fill

                # Even simpler: rectangular fill for now
                if 0 <= r < TERMINAL_HEIGHT and 0 <= c < TERMINAL_WIDTH:
                    # A slightly more complex check for a more rounded appearance
                    # This creates an ellipse based on width and height
                    norm_x = (c - (screen_x - 0.5)) / (sphere_width / 2.0 if sphere_width > 0 else 1)
                    norm_y = (r - (screen_y - 0.5)) / (sphere_height / 2.0 if sphere_height > 0 else 1)
                    if norm_x**2 + norm_y**2 <= 1.0: # Inside ellipse
                         buffer[r][c] = sphere.color + sphere.char + COLOR_RESET


# --- Main Animation Loop ---
def main():
    sphere1 = Sphere(
        x=random.uniform(MIN_X, MAX_X), y=random.uniform(MIN_Y, MAX_Y), z=random.uniform(MIN_Z, MAX_Z),
        dx=random.uniform(-1.5, 1.5), dy=random.uniform(-1, 1), dz=random.uniform(-1, 1),
        color=COLOR_RED, base_diameter=BASE_DIAMETER
    )
    sphere2 = Sphere(
        x=random.uniform(MIN_X, MAX_X), y=random.uniform(MIN_Y, MAX_Y), z=random.uniform(MIN_Z, MAX_Z),
        dx=random.uniform(-1.5, 1.5), dy=random.uniform(-1, 1), dz=random.uniform(-1, 1),
        color=COLOR_GREEN, base_diameter=BASE_DIAMETER
    )
    all_spheres = [sphere1, sphere2]

    try:
        while True:
            # Update positions
            for s in all_spheres:
                s.update_position()

            # Create an empty screen buffer (list of lists of characters)
            screen_buffer = [[' ' for _ in range(TERMINAL_WIDTH)] for _ in range(TERMINAL_HEIGHT)]

            # Draw spheres to the buffer (handles depth)
            draw_spheres_to_buffer(all_spheres, screen_buffer)

            # Clear terminal and print buffer
            clear_terminal()
            for row in screen_buffer:
                print("".join(row))
            print(f"S1(Z:{sphere1.z:.1f}) S2(Z:{sphere2.z:.1f}) {COLOR_RESET}") # Debug info

            time.sleep(0.07) # Frame rate control

    except KeyboardInterrupt:
        clear_terminal()
        print("Animation stopped.")
    finally:
        print(COLOR_RESET) # Reset color on exit


if __name__ == "__main__":
    main()
