#!/usr/bin/env bash
#This script sets up my web servers
DATA="/data/"
WEBSTATIC="/data/web_static/"
RELEASES="/data/web_static/releases/"
SHARED="/data/web_static/shared/"
RELEASETEST="/data/web_static/releases/test/"
HTMLF="/data/web_static/releases/test/index.html"
CURRENT="/data/web_static/current"
sudo apt-get install nginx -y
if [ ! -d "$DATA" ];
  then
    sudo mkdir "$DATA"
fi
if [ ! -d "$WEBSTATIC" ];
   then
    sudo mkdir "$WEBSTATIC"
fi
if [ ! -d "$RELEASES" ];
   then
    sudo mkdir "$RELEASES"
fi
if [ ! -d "$SHARED" ];
   then 
    sudo mkdir "$SHARED"
fi
if [ ! -d "$RELEASETEST" ];
   then
    sudo mkdir "$RELEASETEST"
fi
sudo touch "$HTMLF"
echo -e "<html>\n \t<head>\n \t</head>\n \t<body>\n \t This is a test page\n \t</body>\n</html>" |sudo tee -a "$HTMLF"
if [ -L "$CURRENT" ];
   then 
    sudo rm "$CURRENT"
fi
sudo ln -s "$RELEASETEST" "$CURRENT"
sudo chown -R  ubuntu:ubuntu "$DATA"
sudo sed -i "50i \\\tlocation /hbnb_static {\n \t \t alias /data/web_static/current/;\n \t}" /etc/nginx/sites-available/default
sudo service nginx restart
