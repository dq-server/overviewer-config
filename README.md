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
  "manualpois": overviewer_config.manualpois(),
  "markers": overviewer_config.markers(),
  ```
  - If you want to add some other PoIs or markers, just use `+`, e.g.:  
  ```python
  "manualpois": overviewer_config.manualpois() + [/*..*/],
  "markers": [/*..*/] + overviewer_config.markers(),
  ```
- Run `overviewer --config=config.py --genpoi`.

All done, open `index.html` from your rendered map.

## Is it any good?

[Yes](https://news.ycombinator.com/item?id=3067434).

## Contribute

In lieu of a formal styleguide, take care to maintain the existing coding style.

Please use [these Git commit message conventions](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#heading=h.em2hiij8p46d).

## I'm some guy from the Internet, can I use the code too?

[Yes](LICENSE).
