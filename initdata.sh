#!/bin/sh

echo "Creation d'un compute :"
curl -i --data "name=prime&vcpu=8&memory=64&disk=144&ctype=xen" http://127.0.0.1:8000/compute/
curl http://127.0.0.1:8000/compute/prime

echo
echo
echo "Creation d'un flavour :"
curl -i --data "name=small&vcpu=1&memory=1&disk=4" http://127.0.0.1:8000/flavour/
curl http://127.0.0.1:8000/flavour/small

echo
echo
echo "Creation d'une instance :"
curl -i --data "name=fubar&desc=\"Instance de test pour le compute prime\"&flavour=small" http://127.0.0.1:8000/compute/prime/instance/

echo
echo
