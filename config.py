# Add the following lines to the top of your config file:
# =====
import sys
sys.path.append("subways")
sys.path.append("end_portals")

from common import subwaysFilter
from stations import stationsPois
from railways import railwaysPois
from end_portals import endPortalsPois, endPortalsFilter
# =====


renders["normalrender"] = {
	"world": "My world",
	# ...
	# Add these two keys to every render where you want the subways to be:
	# =====
	"manualpois": stationsPois + railwaysPois + endPortalsPois,
	"markers": [
		{"name": "Subways", "filterFunction": subwaysFilter, "checked": True},
		{"name": "End Portals", "filterFunction": endPortalsFilter, "checked": True},
	],
	# =====
}

# That's all.
