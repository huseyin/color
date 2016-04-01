# Build image:
#       docker build -t color .
# Run container:
#       docker run -it color
#
FROM python:latest
MAINTAINER Hüseyin Tekinaslan <htaslan@bil.omu.edu.tr> (@htaslan)

RUN apt-get update && apt-get install -y \
        ca-certificates \
        git-core \
        --no-install-recommends

RUN rm -rf /var/lib/apt/lists/* \
        && git clone --recursive https://github.com/htaslan/color.git /src

WORKDIR /src

RUN pip install -q enum34
RUN python setup.py -q install

RUN rm -rf /src
