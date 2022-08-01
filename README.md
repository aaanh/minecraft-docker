# Minecraft Docker Container

Version v0.1-dev

Docker hub: <https://hub.docker.com/repository/docker/aaanh/minecraft>

## Currently Supported Features

Very simple, no additional configs, minecraft server.

- Server version defaulted to latest
- Exposed localhost port 25565
- No persistent storage

## Usage

- Start the container

```
docker run -ditp 25565:25565 --name minecraft-server aaanh/minecraft:latest
```

- Attach to the container to perform administrative minecraft server stuff (a.k.a. the console)

```
docker attach minecraft-server
```

- Currently, the only way to "detach" from the CLI without killing the server process is to close the terminal window/instance from host.

## Planned Features

- Set custom port
- Set custom server version
- Persistent volume storage for server data
- Set resource usage
- Dynamic resource scaling
- Horizontal resource orchestration (multi-container)