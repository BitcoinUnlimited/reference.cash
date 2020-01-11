#!/usr/bin/env sh
docker stop buwiki
docker rm buwiki
docker run \
    -d \
    --name buwiki \
    --publish 80:8000 \
    -v "$PWD/mkdocs.yml:/workdir/mkdocs.yml" \
    -v "$PWD/docs:/workdir/docs" \
    buwiki:latest
