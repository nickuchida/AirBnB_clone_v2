#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static.

sudo apt-get -y update
sudo apt-get install -y nginx
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
echo "
<!DOCTYPE html>
<html>
<head>
</head>
<body>
Holberton School
</body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ {alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
