def subwaysFilter(dimension):
	def _filter(poi):
		if poi["id"] == "subways/" + dimension:
			return poi

	return _filter
