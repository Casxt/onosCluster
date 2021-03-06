#!/bin/bash

# Destroys ONOS cluster running as ONOS docker images
SSH_KEY=$(cut -d\  -f2 ~/.ssh/id_rsa.pub)

for i in {1..4}; do
    echo "Destroying onos-$i..."
    docker stop onos-$i
done

docker container prune --force
