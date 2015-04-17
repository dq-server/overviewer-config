# See https://docs.vagrantup.com/v2/
Vagrant.configure(2) do |config|
  config.vm.box = "precise32"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.provision :shell, path: "init.sh"
  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.customize ["modifyvm", :id, "--cpuexecutioncap", "90"]
  end
end
