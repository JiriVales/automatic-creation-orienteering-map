##Find depression area=name
##dem=raster
##polygonsofdepression=output vector
outputs_SAGAFILLSINKS_1=processing.runalg('saga:fillsinks', dem,0.01,None)
outputs_GDALOGRRASTERCALCULATOR_1=processing.runalg('gdalogr:rastercalculator', dem,'1',outputs_SAGAFILLSINKS_1['RESULT'],'1',None,'1',None,'1',None,'1',None,'1','A-B',None,5,None,None)
outputs_GDALOGRPOLYGONIZE_1=processing.runalg('gdalogr:polygonize', outputs_GDALOGRRASTERCALCULATOR_1['OUTPUT'],'DN',None)
outputs_QGISEXTRACTBYATTRIBUTE_1=processing.runalg('qgis:extractbyattribute', outputs_GDALOGRPOLYGONIZE_1['OUTPUT'],'DN',1,'0',polygonsofdepression)