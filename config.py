import sys
sys.path.insert(0, '')
import markers_config

worlds["default"] = "~/minecraft/world"
outputdir = "~/overviewer/map"

renders["north_day"] = {
    "world": "default",
    "northdirection": "upper-left",
    "title": "A regular render",
    "rendermode": "lighting",
    "manualpois": markers_config.manualpois(),
    "markers": markers_config.markers(),
}

renders["south_day"] = {
    "world": "default",
    "northdirection": "lower-right",
    "title": "Inverted",
    "rendermode": "lighting",
    "manualpois": markers_config.manualpois(),
    "markers": markers_config.markers(),
}

renders["north_night"] = {
    "world": "default",
    "northdirection": "upper-left",
    "title": "Night-time",
    "rendermode": "night",
    "manualpois": markers_config.manualpois(),
    "markers": markers_config.markers(),
}

renders["south_night"] = {
    "world": "default",
    "northdirection": "lower-right",
    "title": "Inverted night-time",
    "rendermode": "night",
    "manualpois": markers_config.manualpois(),
    "markers": markers_config.markers(),
}

renders["nether"] = {
    "world": "default",
    "northdirection": "upper-left",
    "title": "Nether",
    "rendermode": "nether",
    "dimension": "nether",
    "manualpois": markers_config.manualpois("nether"),
    "markers": markers_config.markers("nether"),
}
