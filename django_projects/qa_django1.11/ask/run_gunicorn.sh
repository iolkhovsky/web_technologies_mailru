#!/bin/bash
sudo gunicorn -c gunicorn-django.conf ask.wsgi:application
