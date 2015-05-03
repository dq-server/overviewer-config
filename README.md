# overviewer-config
Minecraft Overviewer config files for DQ Server.

## How to use

- Copy icons from `icons/` to your `rendered_map/icons/`
- Copy the `src/` to the same directory as your config.
- Add PoIs and markers to your config:
  - Add this to the top of your config:
  ```python
  import sys
  sys.path.append("src")
  import overviewer_config
  ```
  - Add this to every render where needed:
  ```python
  # By default PoIs are returned for Overworld.
  "manualpois": overviewer_config.manualpois(),
  "markers": overviewer_config.markers(),
  
  # For Nether provide dimension as an argument:
  "manualpois": overviewer_config.manualpois("nether"),
  "markers": overviewer_config.markers("nether"),
  ```
  - If you want to add some other PoIs or markers, just use `+`, e.g.:
  ```python
  "manualpois": overviewer_config.manualpois() + [ /*..*/ ],
  "markers": overviewer_config.markers() + [ /*..*/ ],
  ```
- Run `overviewer --config=config.py --genpoi`.

All done, open `index.html` from your rendered map.

See `test-config.py` for an example. That config is actually used during development.

## Is it any good?

[Yes](https://news.ycombinator.com/item?id=3067434).

## Contribute

- Install [Vagrant](http://www.vagrantup.com/downloads.html).
- In terminal/command line in this directory: `vagrant up`. Wait 5-20 minutes for it to finish, depending on network speed.
It will create a virtual machine with Ubuntu 12.04, install Minecraft server there, create a new world,
then install Minecraft client which Overviewer uses for textures,
then install Overviewer and generate a map.
- `vagrant ssh`, then in the guest machine: `sudo /vagrant/run.sh`.
- In host machine, go to `localhost:8080`. You'll see a map generated for testing.
It will watch for changes, so you can now write code, reload the page and see the changes there.

To stop, exit from the guest machine, then in the host machine: `vagrant halt`.

To launch again, use `vagrant up`, `vagrant ssh`, and `sudo /vagrant/run.sh` again. It will be much faster after the first start.

In lieu of a formal styleguide, take care to maintain the existing coding style.

Please use [these Git commit message conventions](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#heading=h.em2hiij8p46d).

## I'm some guy from the Internet, can I use the code too?

[Yes](LICENSE).
