cd /opt/minecraft-map

sudo overviewer.py --config=/vagrant/test-config.py --genpoi

sudo mkdir /home/vagrant/overviewer-config
sudo unison /home/vagrant/overviewer-config /vagrant \
  -ignore "Path .git" \
  -ignore "Path .vagrant" \
  -ignore "Regex .*\.sublime.*" \
  -fat \
  -repeat 1 > /dev/null 2>&1 &

sudo python -m SimpleHTTPServer 80 &

/vagrant/watch.sh &
