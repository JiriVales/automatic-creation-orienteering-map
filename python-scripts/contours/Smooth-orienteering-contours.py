##Smooth orienteering contours=name
##minimumanglebetweentwoconsecutivesegmentsinhermitesplineinterpolation=number3
##contours=vector
##distancebetweenthecreatedpointshermitesplineinterpolation=number3
##smoothedcontours=output vector
outputs_GRASS7V.GENERALIZE.SMOOTH_1=processing.runalg('grass7:v.generalize.smooth', contours,4,distancebetweenthecreatedpointshermitesplineinterpolation,7.0,0.5,minimumanglebetweentwoconsecutivesegmentsinhermitesplineinterpolation,1.0,1.0,False,True,None,-1.0,0.0001,0,smoothedcontours)