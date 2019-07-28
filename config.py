import os
import sys
sys.path.insert(0, '')
import markers_config

WORLD_DIR = os.environ['MINECRAFT_WORLD_DIR']
OUTPUT_DIR = os.environ['MINECRAFT_MAP_DIR']
CLIENT_PATH = os.environ['MINECRAFT_CLIENT_PATH']

worlds["DQ Server"] = WORLD_DIR
outputdir = OUTPUT_DIR

renders["north_day"] = {
    "world": "DQ Server",
    "texturepath": CLIENT_PATH,
    "northdirection": "upper-left",
    "title": "Day",
    "rendermode": "smooth_lighting",
    "manualpois": markers_config.manualpois(),
    "markers": markers_config.markers(),
}

renders["south_day"] = {
    "world": "DQ Server",
    "texturepath": CLIENT_PATH,
    "northdirection": "lower-right",
    "title": "Day (opposite view)",
    "rendermode": "smooth_lighting",
    "manualpois": markers_config.manualpois(),
    "markers": markers_config.markers(),
}

renders["north_night"] = {
    "world": "DQ Server",
    "texturepath": CLIENT_PATH,
    "northdirection": "upper-left",
    "title": "Night",
    "rendermode": "smooth_night",
    "manualpois": markers_config.manualpois(),
    "markers": markers_config.markers(),
}

renders["south_night"] = {
    "world": "DQ Server",
    "texturepath": CLIENT_PATH,
    "northdirection": "lower-right",
    "title": "Night (opposite view)",
    "rendermode": "smooth_night",
    "manualpois": markers_config.manualpois(),
    "markers": markers_config.markers(),
}

renders["nether"] = {
    "world": "DQ Server",
    "texturepath": CLIENT_PATH,
    "northdirection": "upper-left",
    "title": "Nether",
    "rendermode": "nether",
    "dimension": "nether",
    "manualpois": markers_config.manualpois("nether"),
    "markers": markers_config.markers("nether"),
}

renders["nether"] = {
    "world": "DQ Server",
    "texturepath": CLIENT_PATH,
    "northdirection": "lower-right",
    "title": "Nether (opposite view)",
    "rendermode": "nether",
    "dimension": "nether",
    "manualpois": markers_config.manualpois("nether"),
    "markers": markers_config.markers("nether"),
}
