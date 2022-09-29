#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

# install nginx
apt update -y >/dev/null 2>&1
apt install nginx -y >/dev/null 2>&1

# create folders
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# create index.html page
echo -e "<html>\n\t<body>\n\t<p>Fake HTML Page</p>\n\t</body>\n</html>" > /data/web_static/releases/test/index.html

# create symbolic link
ln -sf /data/web_static/releases/test /data/web_static/current

# change ownership
chown -hR ubuntu:ubuntu /data

# add alias
sed -i '51i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart the nginx service
service nginx restart
