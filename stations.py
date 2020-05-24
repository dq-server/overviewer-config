subwayStations = {}


subwayStations["overworld"] = {
	"Lucky's House": {"x": 142, "z": 832, "color": "white"},
	"North Bridge": {"x": 66, "z": -1340, "color": "white"},
	"North-East Watchtower": {"x": 512, "z": -1333, "color": "white"},
	"Nyan Cat Base": {"x": 0, "z": -1340, "color": "white"},
	"Pole of Cold": {"x": -336, "z": -1001, "color": "white"},
	"Spawn Station": {"x": -336, "z": 510, "color": "white"},
	"Spider Nest": {"x": 802, "z": -1125, "color": "white"},
	"Winter Garden": {"x": 802, "z": 182, "color": "white"},
	"TK's House": {"x": 789, "z": 458, "color": "white"},

	"Creeper Station": {"x": 281, "z": -112, "color": "red"},

	"Deep North Shaft": {"x": 170, "z": -830, "color": "blue"},
	"Diamond Shaft - Far Side": {"x": 82, "z": 510, "color": "blue"},
	"Diamond Shaft": {"x": 82, "z": 412, "color": "blue"},
	"East Outpost": {"x": 802, "z": -107, "color": "blue"},
	"Fake North Station": {"x": 170, "z": -381, "color": "blue"},
	"North Harbor": {"x": 170, "z": -1333, "color": "blue"},
	"North Outpost": {"x": 250, "z": -1500, "color": "blue"},
	"South Outpost": {"x": 83, "z": 705, "color": "blue"},
	"Stone House Catacombs": {"x": 82, "z": 340, "color": "blue"},
	"Stone House": {"x": 82, "z": 293, "color": "blue"},
	"Underground Canyon Station": {"x": 170, "z": -543, "color": "blue"},
	"West Outpost": {"x": -329, "z": -12, "color": "blue"},
}

subwayStations["nether"] = {
	"Nether Residence": {"x": 49, "z": 4, "color": "red"},
	"Cliff's Edge": {"x": 172, "z": 59, "color": "red"},
}

subwayStations["end"] = {}

def subwayStationToPoi(dimension):
	def _subwayStationToPoi(name, info):
		return {
			"id": "subways/" + dimension,
			"x": info["x"],
			"y": 64,
			"z": info["z"],
			"text": name,
			"icon": "icons/station_" + info["color"] + ".png",
		}
	return _subwayStationToPoi

def stationsPois(dimension):
	stationToPoi = subwayStationToPoi(dimension)
	return [stationToPoi(name, info) for name, info in subwayStations[dimension].items()]
