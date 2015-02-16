subwayStations = {
	"Lucky's House": { "x": 142, "z": 832, "color": "white" },
	"North-East Watchtower": { "x": 512, "z": -1333, "color": "white" },
	"TK's House": { "x": 789, "z": 458, "color": "white" },

	"Creeper Station": { "x": 289, "z": -87, "color": "red" },
	"Inner Yard": { "x": 178, "z": -7, "color": "red" },
	"Manyak's House": { "x": 178, "z": -87, "color": "red" },
	"Pankiss": { "x": 108, "z": -7, "color": "red" },
	"Respawn Castle": { "x": 110, "z": -87, "color": "red" },
	"Supercomputer": { "x": 289, "z": -7, "color": "red" },
	"Titans' Hall (red)": { "x": 178, "z": 61, "color": "red" },

	"Lava Columns": { "x": 203, "z": 48, "color": "cyan" },
	"Old Catacombs": { "x": 289, "z": 48, "color": "cyan" },

	"Deep North Shaft": { "x": 170, "z": -830, "color": "blue" },
	"Diamond Shaft - Far Side": { "x": 82, "z": 510, "color": "blue" },
	"Diamond Shaft": { "x": 82, "z": 412, "color": "blue" },
	"East Outpost": { "x": 770, "z": -105, "color": "blue" },
	"Fake North Station": { "x": 170, "z": -381, "color": "blue" },
	# "North Bridge": { "x": 71, "z": -1339, "color": "blue" },
	"North Harbor": { "x": 170, "z": -1333, "color": "blue" },
	"North Outpost": { "x": 250, "z": -1500, "color": "blue" },
	# "Nyan Cat Base": { "x": 0, "z": -1339, "color": "blue" },
	"South Outpost": { "x": 83, "z": 705, "color": "blue" },
	"Stone House Catacombs": { "x": 82, "z": 340, "color": "blue" },
	"Stone House": { "x": 82, "z": 293, "color": "blue" },
	"Titans' Hall (blue)": { "x": 192, "z": 154, "color": "blue" },
	"Underground Canyon Station": { "x": 170, "z": -543, "color": "blue" },
	"West Outpost": { "x": -329, "z": -12, "color": "blue" },
	"Wild Mine": { "x": 75, "z": -12, "color": "blue" },
}

def subwayStationToPoi(name, info):
	return {
		"id": "subways",
		"x": info["x"],
		"y": 60,
		"z": info["z"],
		"text": name,
		"icon": "icons/station_" + info["color"] + ".png"
	}

stationsPois = [subwayStationToPoi(name, info) for name, info in subwayStations.iteritems()]
