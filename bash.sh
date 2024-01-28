#!/bin/bash
sudo apt-get update
sudo apt-get install stress-ng -y
sudo apt-get install htop -y
sudo apt-get install python3-pip -y
pip3 install flask
sudo apt-get install git -y
cd /home/ubuntu
git clone YOUR_GITHUB_REPO_LINK
cd /home/ubuntu/YOUR_GITHUB_REPO_NAME
python3 serve.py