apt-get update
apt-get install -y httpie
apt-get install -y python-pip
apt-get install -y virtualenv
export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
locale-gen en_US.UTF-8
sudo dpkg-reconfigure locales
virtualenv mozio
tar -xzf mozio.tar.gz -C ./mozio/
source mozio/bin/activate
cd mozio
pip install django
pip install geojson
pip install djangorestframework
python manage.py runserver 0.0.0.0:80
