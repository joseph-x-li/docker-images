FROM ubuntu:20.04

# WORKDIR /home/ubuntu

CMD ["bash"]

RUN apt-get update

# prevent user prompts
ENV DEBIAN_FRONTEND=noninteractive 

# build tools
RUN apt-get install -y make gcc g++ cmake

# utilities
RUN apt-get install -y vim git python3.8 python3-pip sudo

# install z3-solver
RUN pip3 install z3-solver

RUN apt-get clean