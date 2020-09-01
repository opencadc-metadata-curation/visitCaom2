#!/bin/bash

COLLECTION="visit"
IMAGE="opencadc/${COLLECTION}Caom2"

echo "Get a proxy certificate"
cp $HOME/.ssl/cadcproxy.pem ./ || exit $?

echo "Get image ${IMAGE}"
docker pull ${IMAGE}

echo "Run image ${IMAGE}"
docker run --rm --name ${COLLECTION}_todo -v ${PWD}:/usr/src/app/ ${IMAGE} ${COLLECTION}_run || exit $?

date
exit 0
