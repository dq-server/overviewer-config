#End Portal POI:

endPortals = {
	"End Portal": { "x" : 869, "z" : 500 },
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

endPortalsPois = [endPortalToPoi(name, info) for name, info in endPortals.iteritems()]

def endPortalsFilter(poi):
	if poi["id"] == "end_portals":
		return poi
