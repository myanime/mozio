There is also shell script setup.sh basically it is just these instructions.
Either run setup.sh:
sudo su
chmod 777 setup.sh
./setup.sh

or install as follows:

Installing Django, Python-pip, Virtualenv, Httpie
==========================================================================
In home directory:
------------------
sudo su

apt-get update
apt-get install -y httpie
apt-get install -y python-pip
apt-get install -y virtualenv

export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
locale-gen en_US.UTF-8
sudo dpkg-reconfigure locales

virtualenv crystal_knows
tar -xzf crystal_knows.tar.gz -C ./mozio/
source crystal_knows/bin/activate
cd mozio
pip install django
pip install selenium
pip install djangorestframework
xvfb-run python manage.py runserver 0.0.0.0:80

Making Requests on localhost
============================
http http://127.0.0.1:8000
curl http://127.0.0.1:8000

The script has been extensively tested using donald duck an barack obama as inputs
