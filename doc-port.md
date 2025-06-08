# Ports Mapping and Localhost Access Documentation
Domain with which you intend to expose my home lab:
kpluslab.com.br
And for the internal network it should be:
kpluslab.local
Locaal IP 
192.168.18.16

------
This document provides a complete mapping 
of all ports used by the services 
in this repository, along with instructions 
for accessing each service via `localhost`.

------

## utils-docker-compose.yml
|--------------|-----------|-----------------|------------------------------------------|
| Service      | Host Port | Container Port  | Localhost URL                            |
|--------------|-----------|-----------------|------------------------------------------|
| portainer    | 9000      | 9000            | http://localhost:9000                    |
| organizr     | 890       | 80              | http://localhost:890                     |
| librespeed   | 9091      | 80              | http://localhost:9091                    |
| homepage     | 3000      | 3000            | http://localhost:3000                    |
|--------------|-----------|-----------------|------------------------------------------|

> Note: `zerotier` uses host networking, so it does not expose a 
web port by default. `watchtower` does not expose a web interface.

---

## rip-docker-compose.yml

|--------------|-----------|-----------------|------------------------------------------|
| Service      | Host Port | Container Port  | Localhost URL                            |
|--------------|-----------|-----------------|------------------------------------------|
| makemkv      | 5800      | 5800            | http://localhost:5800                    |           
| handbrake    | 5801      | 5800            | http://localhost:5801                    | 
|--------------|-----------|-----------------|------------------------------------------|


---

## net-docker-compose.yml
|----------------------|-----------|-----------------|----------------------------------|
| Service              | Host Port | Container Port  | Localhost URL                    |
|----------------------|-----------|-----------------|----------------------------------|
| cloudflared (DoH)    | 5054      | 5054 (host)    | n/a (DNS service)                 |
| cloudflared (metrics)| 8088      | 8088 (host)    | http://localhost:8088             |
| pihole (web)         | 8053      | 8053 (host)    | http://localhost:8053/admin       |
| nginx-proxy-manager  | 8040      | 80             | http://localhost:8040             |
| nginx-proxy-manager  | 8181      | 81             | http://localhost:8181             |
| nginx-proxy-manager  | 443       | 443            | https://localhost                 |
|----------------------|-----------|----------------|-----------------------------------|


> Note: `cloudflared` and `pihole` use host networking, 
so their ports are bound directly to the host.

---

## media-docker-compose.yml
|----------------------|-----------|----------------|---------------------------------|
| Service              | Host Port |Container Port  | Localhost URL                   | 
|----------------------|-----------|----------------|---------------------------------| 
| Metube               | 8881      | 8081           | bhttp://localhost:8081          |
| qbittorrent          | 8080      | 8080           | http://localhost:8080           | 
| qbittorrent          | 62609     | 62609          | (for torrenting, not web)       | 
| jackett              | 9117      | 9117           | http://localhost:9117           | 
| bazarr               | 6767      | 6767           | http://localhost:6767           | 
| overseerr            | 5055      | 5055           | http://localhost:5055           | 
| prowlarr             | 9696      | 9696           | http://localhost:9696           | 
| flaresolverr         | 8191      | 8191           | http://localhost:8191           | 
| sabnzbd              | 6789      | 6789           | http://localhost:6789           | 
| radarr               | 7878      | 7878           | http://localhost:7878           | 
| sonarr               | 8989      | 8989           | http://localhost:8989           | 
| plex                 | (various, host network)    | (see below)                     | 
|----------------------|----------------------------|---------------------------------|


> Note: `plex` uses host networking. By default, 
the web interface is at http://localhost:32400/web

---

## kaizoku-docker-compose.yml

|-----------------------|-------------|----------------|-------------------------------|
| Service               | Host Port   | Container Port | Localhost URL                 |
|-----------------------|-------------|----------------|-------------------------------|
| kaizoku               | 3010        | 3000           | http://localhost:3010         |
| kavita                | 5000        | 5000           | http://localhost:5000         |
|-----------------------|-------------|------------------------------------------------|


---

## Summary Table

|----------------------|---------------|-----------------------------------------------|
| Service              | Host Port     |Localhost URL                                  |
|----------------------|---------------|-----------------------------------------------|
| Portainer            | 9000          | http://localhost:9000                         |
| Organizr             | 890           | http://localhost:890                          |
| Librespeed           | 9091          | http://localhost:9091                         |
| Homepage             | 3000          | http://localhost:3000                         |
| MakeMKV              | 5800          | http://localhost:5800                         |
| Handbrake            | 5801          | http://localhost:5801                         |
| Cloudflared (metrics)| 8088          | http://localhost:8088                         |
| Pi-hole              | 8053          | http://localhost:8053/admin                   |
| Nginx Proxy Manager  | 80,81,443     | http://localhost:8040, :8181, :443            |
| qBittorrent          | 8080          | http://localhost:8080                         |
| Jackett              | 9117          | http://localhost:9117                         |
| Bazarr               | 6767          | http://localhost:6767                         |
| Overseerr            | 5055          | http://localhost:5055                         |
| Prowlarr             | 9696          | http://localhost:9696                         |
| FlareSolverr         | 8191          | http://localhost:8191                         |
| SABnzbd              | 6789          | http://localhost:6789                         |
| Radarr               | 7878          | http://localhost:7878                         |
| Sonarr               | 8989          | http://localhost:8989                         |
| Plex                 | 32400         | http://localhost:32400/web                    |
| Kaizoku              | 3010          | http://localhost:3010                         |
| Kavita               | 5000          | http://localhost:5000                         |
|----------------------|---------------|-----------------------------------------------|

---

> For any service not listed above, check the respective 
  docker-compose file for additional ports or configuration.

---

**How to access:**
- Open your browser and navigate to the listed `http://localhost:PORT` 
  for the desired service.
- For HTTPS services, use `https://localhost:PORT`.
- Some services (like DNS or torrent ports) are not web-accessible 
  and are used by applications directly.

---



|----------------------|-----------------------------|------------------------------------|
| Service              | Host Port                   |Localhost URL                       |
|----------------------|-----------------------------|------------------------------------|
| Portainer            | 192.168.18.16:9000          | portainer.kpluslab.local           |
| Organizr             | 192.168.18.16:890           | organizr.kpluslab.local            |
| Librespeed           | 192.168.18.16:9091          | speed.kpluslab.local               |
| Homepage             | 192.168.18.16:3000          | home.kpluslab.local                |
| MakeMKV              | 192.168.18.16:5800          | makemkv.kpluslab.local             |
| Handbrake            | 192.168.18.16:5801          | handbrake.kpluslab.local           |
| Cloudflared (metrics)| 192.168.18.16:8088          | metrics.kpluslab.local             |
| Pi-hole              | 192.168.18.16:8053          | pihole.kpluslab.local              |
| Nginx Proxy Manager  | 192.168.18.16:80,81,443     | npm.kpluslab.local                 |
| qBittorrent          | 192.168.18.16:8080          | qbit.kpluslab.local                |
| Metube               | 192.168.18.16:8881          | metube.kpluslab.local              |
| Jackett              | 192.168.18.16:9117          | jackett.kpluslab.local             |
| Bazarr               | 192.168.18.16:6767          | bazarr.kpluslab.local              |
| Overseerr            | 192.168.18.16:5055          | request.kpluslab.local             |
| Prowlarr             | 192.168.18.16:9696          | prowlarr.kpluslab.local            |
| FlareSolverr         | 192.168.18.16:8191          | solver.kpluslab.local              |
| SABnzbd              | 192.168.18.16:6789          | sabnzbd.kpluslab.local             |
| Radarr               | 192.168.18.16:7878          | radarr.kpluslab.local              |
| Sonarr               | 192.168.18.16:8989          | sonarr.kpluslab.local              |
| Plex                 | 192.168.18.16:32400         | plex.kpluslab.local                |
| Kaizoku              | 192.168.18.16:3010          | kaizoku.kpluslab.local             |
| Kavita               | 192.168.18.16:5000          | kavita.kpluslab.local              |
|----------------------|-----------------------------|------------------------------------|