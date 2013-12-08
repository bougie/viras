#!/bin/sh
 [ -f db.sqlite ] && rm db.sqlite
python manage.py syncdb
python manage.py loaddata keystore/fixtures/*
