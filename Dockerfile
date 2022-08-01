FROM ubuntu:latest

RUN export DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y
RUN apt install -y openjdk-18-jre-headless python3 curl
RUN apt install -y python3-pip
RUN apt install -y tmux

WORKDIR /server
COPY . .

RUN python3 -m pip install requests
RUN python3 get-latest-version.py

RUN curl -O $(cat set_latest_version.txt)
RUN echo "eula=true" > eula.txt
EXPOSE 25565

RUN tmux new-session -s root -d

CMD ["java", "-Xmx1024M", "-Xms1024M", "-jar", "server.jar", "nogui"]