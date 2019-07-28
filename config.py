import os
import sys
sys.path.insert(0, '')
import markers_config

WORLD_DIR = os.environ['MINECRAFT_WORLD_DIR']
OUTPUT_DIR = os.environ['MINECRAFT_MAP_DIR']
CLIENT_PATH = os.environ['MINECRAFT_CLIENT_PATH']

worlds["default"] = WORLD_DIR
outputdir = OUTPUT_DIR

renders["north_day"] = {
    "world": "default",
    "texturepath": CLIENT_PATH,
    "northdirection": "upper-left",
    "title": "A regular render",
    "rendermode": "smooth_lighting",
    "manualpois": markers_config.manualpois(),
    "markers": markers_config.markers(),
}

renders["south_day"] = {
    "world": "default",
    "texturepath": CLIENT_PATH,
    "northdirection": "lower-right",
    "title": "Inverted",
    "rendermode": "smooth_lighting",
    "manualpois": markers_config.manualpois(),
    "markers": markers_config.markers(),
}

renders["north_night"] = {
    "world": "default",
    "texturepath": CLIENT_PATH,
    "northdirection": "upper-left",
    "title": "Night-time",
    "rendermode": "smooth_night",
    "manualpois": markers_config.manualpois(),
    "markers": markers_config.markers(),
}

renders["south_night"] = {
    "world": "default",
    "texturepath": CLIENT_PATH,
    "northdirection": "lower-right",
    "title": "Inverted night-time",
    "rendermode": "smooth_night",
    "manualpois": markers_config.manualpois(),
    "markers": markers_config.markers(),
}

renders["nether"] = {
    "world": "default",
    "texturepath": CLIENT_PATH,
    "northdirection": "upper-left",
    "title": "Nether",
    "rendermode": "nether_smooth_lighting",
    "dimension": "nether",
    "manualpois": markers_config.manualpois("nether"),
    "markers": markers_config.markers("nether"),
}
