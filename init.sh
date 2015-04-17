# We're gonna install Minecraft server, create a new world,
# then install Minecraft client which Overviewer uses for textures,
# then install Overviewer, generate the map,
# then watch for changes in code and generate POIs when they occur.

# Install `add-apt-repository` command
sudo apt-get update
sudo apt-get install -y python-software-properties

# Install Java
sudo apt-add-repository -y ppa:webupd8team/java
sudo apt-get update
# http://askubuntu.com/a/190674
echo "debconf shared/accepted-oracle-license-v1-1 select true" | sudo debconf-set-selections
echo "debconf shared/accepted-oracle-license-v1-1 seen true" | sudo debconf-set-selections
sudo apt-get install -y oracle-java7-installer

# Generate a new world for testing
sudo mkdir /opt/minecraft-server
sudo chmod a+rw /opt/minecraft-server
cd /opt/minecraft-server
wget "https://s3.amazonaws.com/Minecraft.Download/versions/1.8.1/minecraft_server.1.8.1.jar"
echo "eula=true" | sudo tee eula.txt
sudo java -Xms1G -Xmx1600M -jar ./minecraft_server.1.8.1.jar nogui &
sleep 120
sudo kill $!

# Install Python 2.6 for Overviewer
sudo add-apt-repository -y ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install -y python2.6 python2.6-dev

# Install Overviewer
echo "deb http://overviewer.org/debian ./" | sudo tee -a /etc/apt/sources.list
wget -O - http://overviewer.org/debian/overviewer.gpg.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y minecraft-overviewer
# Install Minecraft client which Overviewer uses for textures
# http://docs.overviewer.org/en/latest/running/#installing-the-textures
wget https://s3.amazonaws.com/Minecraft.Download/versions/1.8/1.8.jar -P ~/.minecraft/versions/1.8/

# Generate a test map
sudo mkdir /opt/minecraft-map
sudo chmod a+rw /opt/minecraft-map
overviewer.py --config=/vagrant/test-config.py

# Serve as http://localhost:8080 on host machine and watch for changes
sudo apt-get install -y inotify-tools
sudo apt-get install -y unison
