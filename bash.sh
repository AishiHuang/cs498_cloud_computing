#!/bin/bash
sudo apt-get update
sudo apt-get install stress-ng -y
sudo apt-get install htop -y
sudo apt-get install python3-pip -y
pip3 install flask
sudo apt-get install git -y
cd /home/ubuntu
git clone https://github.com/AishiHuang/cs498_cloud_computing.git
cd cs498_cloud_computing
python3 serve.py
