FROM ubuntu:20.04

CMD ["bash"]

RUN apt-get update

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get install -y git make cmake gcc g++

RUN apt-get install -y vim sudo 

RUN sudo apt-get install -y pkg-config libgtk-3-dev libsdl2-dev

RUN apt-get clean