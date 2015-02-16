subwayRailways = [
	# Red
	{"color": "red", "way": [
		{"station": "Inner Yard", "y": 54},
		{"station": "Supercomputer", "y": 54},
	]},
	{"color": "red", "way": [
		{"station": "Inner Yard", "y": 54},
		{"station": "Pankiss", "y": 54},
	]},
	{"color": "red", "way": [
		{"station": "Inner Yard", "y": 16},
		{"station": "Manyak's House", "y": 16},
	]},
	{"color": "red", "way": [
		{"station": "Inner Yard", "y": 16},
		{"station": "Titans' Hall (red)", "y": 16},
	]},
	{"color": "red", "way": [
		{"station": "Manyak's House", "y": 10},
		{"station": "Creeper Station", "y": 10},
	]},
	{"color": "red", "way": [
		{"station": "Manyak's House", "y": 10},
		{"station": "Respawn Castle", "y": 10},
	]},

	# Cyan
	{"color": "cyan", "way": [
		{"station": "Creeper Station", "y": 5},
		{"station": "Supercomputer", "y": 5},
	]},
	{"color": "cyan", "way": [
		{"station": "Old Catacombs", "y": 5},
		{"station": "Supercomputer", "y": 5},
	]},
	{"color": "cyan", "way": [
		{"station": "Old Catacombs", "y": 5},
		{"station": "Lava Columns", "y": 5},
	]},

	# Blue
	{"color": "blue", "way": [
		{"station": "Respawn Castle", "y": 40},
		{"station": "Pankiss", "y": 40},
	]},
	{"color": "blue", "way": [
		{"station": "Wild Mine", "y": 40},
		{"station": "Pankiss", "y": 40},
	]},
	{"color": "blue", "way": [
		{"station": "Wild Mine", "y": 40},
		{"station": "West Outpost", "y": 40},
	]},
	{"color": "blue", "way": [
		{"station": "Titans' Hall (blue)", "y": 11},
		{"x": 82, "z": 154, "y": 11},
		{"station": "Stone House", "y": 11},
	]},
	{"color": "blue", "way": [
		{"station": "Stone House", "y": 11},
		{"station": "Stone House Catacombs", "y": 11},
	]},
	{"color": "blue", "way": [
		{"station": "Stone House Catacombs", "y": 11},
		{"station": "Diamond Shaft", "y": 11},
	]},
	{"color": "blue", "way": [
		{"station": "Diamond Shaft", "y": 11},
		{"station": "Diamond Shaft - Far Side", "y": 11},
	]},
	{"color": "blue", "way": [
		{"station": "Diamond Shaft - Far Side", "y": 11},
		{"station": "South Outpost", "y": 11},
	]},
	{"color": "blue", "way": [
		{"station": "East Outpost", "y": 10},
		{"station": "Creeper Station", "y": 10},
	]},
	{"color": "blue", "way": [
		{"station": "Manyak's House", "y": 25},
		{"station": "Fake North Station", "y": 25},
	]},
	{"color": "blue", "way": [
		{"station": "Fake North Station", "y": 25},
		{"station": "Underground Canyon Station", "y": 25},
	]},
	{"color": "blue", "way": [
		{"station": "Underground Canyon Station", "y": 25},
		{"station": "Deep North Shaft", "y": 25},
	]},
	{"color": "blue", "way": [
		{"station": "Deep North Shaft", "y": 25},
		{"station": "North Harbor", "y": 25},
	]},
	{"color": "blue", "way": [
		{"station": "North Harbor", "y": 25},
		{"x": 170, "z": -1500, "y": 25},
		{"station": "North Outpost", "y": 25},
	]},

	# White
	{"color": "white", "way": [
		{"station": "South Outpost", "y": 51},
		{"x": 83, "z": 832, "y": 51},
		{"station": "Lucky's House", "y": 51},
	]},
	{"color": "white", "way": [
		{"station": "Lucky's House", "y": 51},
		{"x": 137, "z": 747, "y": 51},
		{"x": 137, "z": 715, "y": 19},
		{"x": 137, "z": 705, "y": 19},
		{"x": 620, "z": 705, "y": 19},
		{"x": 630, "z": 705, "y": 20},
		{"x": 789, "z": 705, "y": 20},
		{"x": 789, "z": 500, "y": 20},
		{"station": "TK's House", "y": 62},
	]},
	{"color": "white", "way": [
		{"station": "TK's House", "y": 62},
		{"x": 789, "z": 408, "y": 12},
		{"station": "East Outpost", "y": 12},
	]},
	{"color": "white", "way": [
		{"station": "North Harbor", "y": 14},
		{"x": 210, "z": -1333, "y": 14},
		{"x": 210, "z": -1489, "y": 14},
		{"x": 210, "z": -1500, "y": 25},
		{"station": "North Outpost", "y": 25},
	]},
	{"color": "white", "way": [
		{"station": "North Outpost", "y": 25},
		{"x": 512, "z": -1500, "y": 25},
		{"station": "North-East Watchtower", "y": 25},
	]},
]

import sys
from stations import subwayStations

def colorToRgb(color):
	predefinedColors = {
		"white": "#CCCCCC",
		"red": "#DD5858",
		"cyan": "#53CCC1",
		"blue": "#5369AF",
	}

	if color in predefinedColors:
		return predefinedColors[color]
	else:
		return color

def wayToPolyline(way):
	calculatedPoints = []

	for point in way:

		if "station" in point:

			if point["station"] in subwayStations:
				calculatedPoints.append({
					"x": subwayStations[point["station"]]["x"],
					"y": point["y"],
					"z": subwayStations[point["station"]]["z"],
				})

			else:
				raise KeyError("There's no subway station named " + point["station"])

		else:

			calculatedPoints.append({
				"x": point["x"],
				"y": point["y"],
				"z": point["z"],
			})

	return tuple(calculatedPoints)

def normalizePolyline(polyline):
	calculatedPoints = []

	for point in polyline:
		calculatedPoints.append({
			"x": point["x"],
			"y": 60,
			"z": point["z"],
		})

	return tuple(calculatedPoints)

def subwayRailwayToPois(railway):
	pois = []

	polyline = wayToPolyline(railway["way"])

	# pois = heightPoisFromPolyline(polyline)

	polyline = normalizePolyline(polyline)

	pois.append({
		"id": "subways",
		"x": sys.maxint,
		"y": sys.maxint,
		"z": sys.maxint,
		"text": "",
		"color": colorToRgb(railway["color"]),
		"polyline": polyline,
	})

	return pois

railwaysPois = [poi for pois in map(subwayRailwayToPois, subwayRailways) for poi in pois]
