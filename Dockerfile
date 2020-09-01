FROM opencadc/astropy:3.8-slim

RUN apt-get update
RUN apt-get install -y \
    build-essential \
    git
    
RUN pip install cadcdata \
    cadctap \
    caom2 \
    caom2repo \
    caom2utils \
    deprecated \
    ftputil \
    importlib-metadata \
    pytz \
    PyYAML \
    spherical-geometry \
    vos

WORKDIR /usr/src/app

ARG OMC_REPO=opencadc-metadata-curation

RUN git clone https://github.com/${OMC_REPO}/caom2pipe.git && \
  pip install ./caom2pipe
  
RUN git clone https://github.com/${OMC_REPO}/visitCaom2.git && \
  cp ./visitCaom2/scripts/config.yml / && \
  cp ./visitCaom2/scripts/docker-entrypoint.sh / && \
  pip install ./visitCaom2

ENTRYPOINT ["/docker-entrypoint.sh"]
