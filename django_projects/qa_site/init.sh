#!/bin/bash
echo "Installations"
sudo apt-get update
sudo apt-get install -y python3.5
sudo apt-get install -y python3.5-dev
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install --upgrade pip
sudo pip3 install --upgrade django==2.1
sudo pip3 install --upgrade gunicorn

echo "Nginx update"
cd etc
sudo cp nginx.conf /etc/nginx/nginx.conf
sudo /etc/init.d/nginx restart
cd ..

echo "Django project"
mkdir /home/box/web
cp -r uploads /home/box/web
cp -r public /home/box/web
cp hello.py /home/box/web
cp run_hello_gunicorn.sh /home/box/web
export MYROOT = $(pwd)
cd /home/box/web
django-admin startproject ask
cd ask 
django-admin startapp qa
cd $(MYROOT)
cp ask/ask/settings.py /home/box/web/ask/settings.py
cp ask/ask/urls.py /home/box/web/ask/urls.py
cp ask/qa/views.py /home/box/web/ask/qa/views.py

cd /home/box/web
sudo chmod +x run_hello_gunicorn.sh
./run_hello_gunicorn.sh && cd ask
gunicorn ask.wsgi:application
#python3 manage.py runserver 127.0.0.1:8000
