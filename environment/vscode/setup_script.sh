#!/bin/bash

sudo apt-get update
sudo apt-get install curl -y

curl -fsSL https://code-server.dev/install.sh | sh -s --
pip3 install pandas # install your dependecies