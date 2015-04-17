import sys
sys.path.append("/vagrant/src")
import overviewer_config

worlds["Test Server"] = "/opt/minecraft-server/world"

renders["normal"] = {
	"world": "Test Server",
	"title": "Normal",
	"rendermode": "lighting",
	"manualpois": overviewer_config.manualpois(),
	"markers": overviewer_config.markers(),
}

renders["night"] = {
	"world": "Test Server",
	"title": "Night",
	"rendermode": "night",
}

outputdir = "/opt/minecraft-map"
