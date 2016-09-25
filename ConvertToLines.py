			
			
def convertToLines():
	g = CurrentGlyph()	
	if g and g.selection != []:
		g.prepareUndo()
		a_list_x = []
		a_list_y = []
		insertAttributes = []
		
		for c_index in range(len(g.contours)):
			c = g.contours[c_index]
			for s_index in range(len(c.segments)):
				s = c.segments[s_index]
				if s.selected and s.type == "curve":
				    s.type = "line"
		g.update()

				
convertToLines()

