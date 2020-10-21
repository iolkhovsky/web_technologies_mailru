#!/bin/bash
cd /home/box
git clone https://github.com/iolkhovsky/web_technologies_mailru.git
cd web_technologies_mailru
cp -r nginx_test/web /home/box/web
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
