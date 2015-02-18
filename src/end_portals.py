endPortals = {
	"End Portal": {"x": 869, "z": 500, "y": 35},
}

def endPortalToPoi(name, info):
	return {
		"id": "end_portals",
		"x": info["x"],
		"y": 60,
		"z": info["z"],
		"text": name,
		"icon": "icons/end_portal.png",
	}

def endPortalsPois():
	return [endPortalToPoi(name, info) for name, info in endPortals.iteritems()]

def endPortalsFilter(poi):
	if poi["id"] == "end_portals":
		return poi
