#!/usr/bin/env bash
# This script sets up the filestructure and basic NGINX config for a static
# AirBNB web server

sudo apt-get -y update
sudo apt-get -y install nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "Simple Content" >> /data/web_static/releases/test/index.html

ln -fs /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data

sed -i "/listen 80 default_server;/a location /hbnb_static {alias /data/web_static/current/;}" /etc/nginx/sites-available/default

sudo ufw allow "Nginx HTTP"
sudo service nginx restart
