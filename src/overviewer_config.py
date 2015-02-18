from subways_common import subwaysFilter
from end_portals import endPortalsFilter

from stations import stationsPois
from railways import railwaysPois
from end_portals import endPortalsPois

def manualpois():
	return stationsPois() + railwaysPois() + endPortalsPois()

def markers():
	return [
		{"name": "Subways", "filterFunction": subwaysFilter, "checked": True},
		{"name": "End Portals", "filterFunction": endPortalsFilter, "checked": True},
	]
