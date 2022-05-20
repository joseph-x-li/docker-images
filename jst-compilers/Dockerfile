FROM ubuntu:20.04

RUN apt-get update

# prevent user prompts
ENV DEBIAN_FRONTEND=noninteractive 

# build tools
RUN apt-get install -y make gcc g++ cmake

# utilities
RUN apt-get install -y vim git python3.8 autoconf sudo

# ocaml
RUN apt-get install -y opam

# llvm-13
RUN sudo apt-get install -y software-properties-common
RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key|sudo apt-key add -
RUN sudo add-apt-repository "deb http://apt.llvm.org/focal/ llvm-toolchain-focal-13 main"
RUN sudo apt-get update
RUN sudo apt-get install -y libllvm-13-ocaml-dev libllvm13 llvm-13 llvm-13-dev llvm-13-doc llvm-13-examples llvm-13-runtime
RUN sudo ln -s /usr/bin/llvm-config-13 /usr/bin/llvm-config
# RUN sudo add-apt-repository "deb-src http://apt.llvm.org/focal/ llvm-toolchain-focal-13 main"


# create a user
# RUN useradd --create-home --shell /bin/bash ubuntu
# USER ubuntu
# WORKDIR /home/ubuntu

# ocaml config
RUN mkdir -p /workspace
COPY dune.exe /workspace/dune.exe
RUN opam init -a --disable-sandboxing
RUN opam sw create dev --empty
RUN opam pin add -y ocaml-variants.4.12.0+dev https://github.com/joseph-x-li/flambda-backend.git#save_cfg_after_select
RUN opam install -y llvm.13.0.0
RUN opam install -y shexp bigstring
# core.v0.14.1 avoids some deprecations that appear in v0.15.0
RUN opam install -y core.v0.14.1

RUN apt-get clean