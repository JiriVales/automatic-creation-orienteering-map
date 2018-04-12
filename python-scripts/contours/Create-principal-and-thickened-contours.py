##Create principal and thickened contours=name
##digitalterrainmodelraster=raster
##vzorec=stringif(("ELEV" % 25)=0,1,0)
##contourinterval=number5.0
##contours=output vector
outputs_GDALOGRCONTOUR_1=processing.runalg('gdalogr:contour', digitalterrainmodelraster,contourinterval,'ELEV',None,None)
outputs_QGISFIELDCALCULATOR_2=processing.runalg('qgis:fieldcalculator', outputs_GDALOGRCONTOUR_1['OUTPUT_VECTOR'],'thick',1,1.0,0.0,True,vzorec,contours)