FROM ubuntu:22.04 as base

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y \
    python3 \
    libpython3-dev \
    python3-distutils \
    python3-numpy \
    python3-scipy \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

FROM base as build-taco

RUN git clone https://github.com/tensor-compiler/taco.git /tools/taco
WORKDIR /tools/taco/build
RUN cmake -DCMAKE_BUILD_TYPE=Release -DPYTHON=ON ..
RUN make -j4

FROM base as container
COPY --from=build-taco /tools/taco/build /tools/taco/build
ENV PYTHONPATH "/tools/taco/build/lib:${PYTHONPATH}"
