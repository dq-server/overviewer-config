import sys
sys.path.append("/vagrant/src")
import overviewer_config

worlds["Test Overworld"] = "/opt/minecraft-server/world"
worlds["Test Nether"] = "/opt/minecraft-server/world"

renders["normal"] = {
	"world": "Test Overworld",
	"title": "Normal",
	"rendermode": "lighting",
	"manualpois": overviewer_config.manualpois(),
	"markers": overviewer_config.markers(),
}

renders["nether"] = {
	"world": "Test Nether",
	"title": "Nether",
	"rendermode": "lighting",
	"manualpois": overviewer_config.manualpois("nether"),
	"markers": overviewer_config.markers("nether"),
}

outputdir = "/opt/minecraft-map"
