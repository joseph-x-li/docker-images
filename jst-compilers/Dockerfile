FROM ubuntu:20.04

# WORKDIR /home/ubuntu

CMD ["bash"]

RUN apt-get update

# prevent user prompts
ENV DEBIAN_FRONTEND=noninteractive 

# build tools
RUN apt-get install -y make gcc g++ cmake ninja-build

# utilities
RUN apt-get install -y vim git python3.8 autoconf

# ocaml
RUN apt-get install -y opam 

RUN apt-get clean