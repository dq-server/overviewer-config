import sys
sys.path.insert(0, '')
import markers_config
from .observer import JSObserver

WORLD_DIR = os.environ['MINECRAFT_WORLD_DIR']
OUTPUT_DIR = os.environ['MINECRAFT_MAP_DIR']
CLIENT_PATH = os.environ['MINECRAFT_CLIENT_PATH']

worlds["default"] = WORLD_DIR
outputdir = OUTPUT_DIR

observer = JSObserver(OUTPUT_DIR, 10)

renders["north_day"] = {
    "world": "default",
    "texturepath": CLIENT_PATH,
    "northdirection": "upper-left",
    "title": "A regular render",
    "rendermode": "lighting",
    "manualpois": markers_config.manualpois(),
    "markers": markers_config.markers(),
}

renders["south_day"] = {
    "world": "default",
    "texturepath": CLIENT_PATH,
    "northdirection": "lower-right",
    "title": "Inverted",
    "rendermode": "lighting",
    "manualpois": markers_config.manualpois(),
    "markers": markers_config.markers(),
}

renders["north_night"] = {
    "world": "default",
    "texturepath": CLIENT_PATH,
    "northdirection": "upper-left",
    "title": "Night-time",
    "rendermode": "night",
    "manualpois": markers_config.manualpois(),
    "markers": markers_config.markers(),
}

renders["south_night"] = {
    "world": "default",
    "texturepath": CLIENT_PATH,
    "northdirection": "lower-right",
    "title": "Inverted night-time",
    "rendermode": "night",
    "manualpois": markers_config.manualpois(),
    "markers": markers_config.markers(),
}

renders["nether"] = {
    "world": "default",
    "texturepath": CLIENT_PATH,
    "northdirection": "upper-left",
    "title": "Nether",
    "rendermode": "nether",
    "dimension": "nether",
    "manualpois": markers_config.manualpois("nether"),
    "markers": markers_config.markers("nether"),
}
