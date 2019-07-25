import sys
sys.path.append("src")
import markers_config

worlds["default"] = "~/minecraft/world"
outputdir = "~/overviewer/map"

renders["north_day"] = {
    "world": "default",
    "northdirection": "upper-left",
    "title": "A regular render",
    "rendermode": "lighting",
    "manualpois": overviewer_config.manualpois(),
    "markers": overviewer_config.markers(),
}

renders["south_day"] = {
    "world": "default",
    "northdirection": "lower-right",
    "title": "Inverted",
    "rendermode": "lighting",
    "manualpois": overviewer_config.manualpois(),
    "markers": overviewer_config.markers(),
}

renders["north_night"] = {
    "world": "default",
    "northdirection": "upper-left",
    "title": "Night-time",
    "rendermode": "night",
    "manualpois": overviewer_config.manualpois(),
    "markers": overviewer_config.markers(),
}

renders["south_night"] = {
    "world": "default",
    "northdirection": "lower-right",
    "title": "Inverted night-time",
    "rendermode": "night",
    "manualpois": overviewer_config.manualpois(),
    "markers": overviewer_config.markers(),
}

renders["nether"] = {
    "world": "default",
    "northdirection": "upper-left",
    "title": "Nether",
    "rendermode": "nether",
    "dimension": "nether",
    "manualpois": overviewer_config.manualpois("nether"),
    "markers": overviewer_config.markers("nether"),
}
