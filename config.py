# Add the following lines to the top of your config file:
# =====
import sys
sys.path.append("subways")

from common import subwaysFilter
from stations import stationsPois
from railways import railwaysPois
# =====


renders["normalrender"] = {
    "world": "My world",
    # ...
	# Add these two keys to every render where you want the subways to be:
	# =====
    "manualpois": stationsPois + railwaysPois,
    "markers": [
        {"name": "Subways", "filterFunction": subwaysFilter, "checked": True}
    ]
	# =====
}

# That's all.
