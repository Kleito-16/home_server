# Home Lab Media Server

A self-hosted media server and home lab environment for managing and streaming movies, TV shows, manga, and more.

## Overview

This project sets up a comprehensive home media server using Docker containers, with services organized into different stacks:

- **Media Stack**: Plex, Sonarr, Radarr, and related services for managing media
- **Manga Stack**: Kaizoku and Kavita for manga collection
- **Network Stack**: DNS, proxy, and networking services
- **Utility Stack**: System monitoring and management tools
- **Ripping Stack**: Tools for digitizing physical media

## Services

### Media Management
- **Plex**: Media server for streaming videos
- **Sonarr**: TV show management and automation
- **Radarr**: Movie management and automation
- **Bazarr**: Subtitle management
- **Overseerr**: Media request management
- **SABnzbd**: Usenet downloader
- **qBittorrent**: Torrent client
- **Prowlarr/Jackett**: Indexer management
- **FlareSolverr**: Bypass Cloudflare protection

### Manga Management
- **Kaizoku**: Manga collection manager
- **Kavita**: Manga/comic reader server

### Network & Security
- **Cloudflared**: DNS-over-HTTPS proxy
- **Pi-hole**: Network-wide ad blocking
- **Nginx Proxy Manager**: Reverse proxy and SSL management

### Utilities
- **Portainer**: Docker management UI
- **Homepage**: Dashboard for services
- **Organizr**: Service organization
- **Librespeed**: Network speed testing
- **Watchtower**: Automatic container updates
- **Zerotier**: VPN for remote access

### Media Ripping
- **MakeMKV**: Blu-ray/DVD ripping
- **Handbrake**: Video transcoding

## Port Configuration

See [doc-port.md](doc-port.md) for a complete list of service ports and access URLs.

## Installation

1. Clone this repository
2. Copy `.env.example` to `.env` and configure variables
3. Create required directories:
```bash
mkdir -p /home/kleito/config-docker/{organizr,zerotier,librespeed,homepage,handbrake,makemkv,dnsmasq.d,pihole,qbittorrent,jackett,bazarr,overseerr,prowlarr,flaresolverr,nzbget,radarr,sonarr,plex,kavita}
```
4. Start the stacks:
```bash
docker compose -f utils-docker-compose.yml up -d
docker compose -f net-docker-compose.yml up -d
docker compose -f media-docker-compose.yml up -d
docker compose -f rip-docker-compose.yml up -d
docker compose -f kaizoku-docker-compose.yml up -d
```

## Configuration

- Set up Nginx Proxy Manager for secure external access
- Configure Cloudflare Tunnel using `config.yml`
- Set up SSL certificates for services
- Configure media paths in each service

## Storage

The system uses the following main storage locations:
- `/mnt/terachad/Videos`: Movies and TV shows
- `/mnt/terachad/Manga`: Manga library
- `/mnt/terachad/Downloads`: Download management
- `/home/kleito/config-docker`: Service configurations

## Security Notes

- Change default passwords immediately
- Use SSL for all external access
- Configure firewall rules appropriately
- Keep containers updated using Watchtower
- Store sensitive data in `.env` file (not in git)

## Future Plans

- Expose services securely via Cloudflare Tunnel
- Implement automated backup solution
- Add monitoring and alerting
- Expand media library capabilities

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.