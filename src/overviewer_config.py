from subways_common import subwaysFilter
from end_portals import endPortalsFilter

from stations import stationsPois
from railways import railwaysPois
from end_portals import endPortalsPois

def manualpois(dimension = "overworld"):
	result = stationsPois(dimension) + railwaysPois(dimension)
	if dimension == "overworld":
		result += endPortalsPois()
	return result

def markers(dimension = "overworld"):
	result = [
		{"name": "Subways", "filterFunction": subwaysFilter, "checked": True},
	]
	if dimension == "overworld":
		result.append({"name": "End Portals", "filterFunction": endPortalsFilter, "checked": True})
	return result
