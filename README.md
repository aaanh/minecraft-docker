# Minecraft Docker Container

![Docker Build](https://github.com/aaanh/minecraft-docker/actions/workflows/docker-build-test.yml/badge.svg)

Version v1.1-beta

Docker Hub: <https://hub.docker.com/repository/docker/aaanh/minecraft>

## Currently Supported Features

Very simple, no additional configs, minecraft server.

- Server version defaulted to latest
- Exposed localhost port 25565
- No persistent storage

## Usage

- Start the container

amd64 / x86_64

```
docker run -ditp 25565:25565 --name minecraft-server aaanh/minecraft:latest
```

arm64 (tested on Mac M1 Pro)

```
docker run -ditp 25565:25565 --name minecraft-server aaanh/minecraft:arm64-latest
```

- Attach to the container to perform administrative minecraft server stuff (a.k.a. the console)

```
docker attach minecraft-server
```

- Currently, the only way to "detach" from the CLI without killing the server process is to close the terminal window/instance from host.

## Build It Yourself

```
docker build . --tag image-name:tag
```

## Planned Features

- Set custom port
- Set custom server version
- Persistent volume storage for server data
