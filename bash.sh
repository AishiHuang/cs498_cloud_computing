#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip3 install flask
sudo yum install git -y
# cd /home/ubuntu
git clone https://github.com/AishiHuang/cs498_cloud_computing.git
cd cs498_cloud_computing
python3 serve.py
