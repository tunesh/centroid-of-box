def centroid(bbox):

	startX, startY, endX, endY = bbox
	cX = int((startX + endX) / 2.0)
	cY = int((startY + endY) / 2.0)

	return(cX, cY)
	