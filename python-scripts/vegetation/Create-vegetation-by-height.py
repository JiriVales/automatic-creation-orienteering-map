##Create vegetation by height=name
##minimumareaofholesinvegetationslowrunningpolygonsmeters=number225
##formulaforheightdifferentiation=stringifelse(a<1, 1,ifelse(a<6, 2, ifelse(a<10, 3, 4)))
##numberoftheminimumareaofvegetationpolygons=string225
##minimumareaofholesinopenlandpolygons=number110
##maximumdistancemetersbetweentheoriginalandthesimplifiedpolygonboundary=number3.0
##normaliseddigitalsurfacemodelraster=raster
##distancemetersbetweenthecreatedpointsatthepolygonboundarychaikenalgorithm=number2.0
##minimumareaofholesinvegetationwalkfightpolygonsmeters=number110
##vegetationopenland=output vector
##vegetationslowrunning=output vector
##vegetationwalkfight=output vector
outputs_SAGARASTERCALCULATOR_1=processing.runalg('saga:rastercalculator', normaliseddigitalsurfacemodelraster,[],formulaforheightdifferentiation,3,False,7,None)
outputs_GDALOGRPOLYGONIZE_1=processing.runalg('gdalogr:polygonize', outputs_SAGARASTERCALCULATOR_1['RESULT'],'type',None)
outputs_QGISEXTRACTBYATTRIBUTE_1=processing.runalg('qgis:extractbyattribute', outputs_GDALOGRPOLYGONIZE_1['OUTPUT'],'type',4,'4',None)
outputs_QGISFIELDCALCULATOR_1=processing.runalg('qgis:fieldcalculator', outputs_QGISEXTRACTBYATTRIBUTE_1['OUTPUT'],'area',0,10.0,3.0,True,'$area',None)
outputs_QGISEXTRACTBYATTRIBUTE_2=processing.runalg('qgis:extractbyattribute', outputs_QGISFIELDCALCULATOR_1['OUTPUT_LAYER'],'area',3,numberoftheminimumareaofvegetationpolygons,None)
outputs_GRASS7V.GENERALIZE.SIMPLIFY_1=processing.runalg('grass7:v.generalize.simplify', outputs_QGISEXTRACTBYATTRIBUTE_2['OUTPUT'],0,maximumdistancemetersbetweentheoriginalandthesimplifiedpolygonboundary,7.0,50.0,False,True,None,-1.0,0.0001,0,None)
outputs_GRASS7V.GENERALIZE.SMOOTH_1=processing.runalg('grass7:v.generalize.smooth', outputs_GRASS7V.GENERALIZE.SIMPLIFY_1['output'],3,distancemetersbetweenthecreatedpointsatthepolygonboundarychaikenalgorithm,7.0,0.5,3.0,1.0,1.0,False,True,None,-1.0,0.0001,0,None)
outputs_QGISEXTRACTBYATTRIBUTE_3=processing.runalg('qgis:extractbyattribute', outputs_GRASS7V.GENERALIZE.SMOOTH_1['output'],'type',0,'1',None)
outputs_QGISEXTRACTBYATTRIBUTE_5=processing.runalg('qgis:extractbyattribute', outputs_GRASS7V.GENERALIZE.SMOOTH_1['output'],'type',0,'2',None)
outputs_QGISEXTRACTBYATTRIBUTE_4=processing.runalg('qgis:extractbyattribute', outputs_GRASS7V.GENERALIZE.SMOOTH_1['output'],'type',0,'3',None)
outputs_QGISFILLHOLES_3=processing.runalg('qgis:fillholes', outputs_QGISEXTRACTBYATTRIBUTE_3['OUTPUT'],minimumareaofholesinopenlandpolygons,vegetationopenland)
outputs_QGISFILLHOLES_2=processing.runalg('qgis:fillholes', outputs_QGISEXTRACTBYATTRIBUTE_4['OUTPUT'],minimumareaofholesinvegetationslowrunningpolygonsmeters,vegetationslowrunning)
outputs_QGISFILLHOLES_1=processing.runalg('qgis:fillholes', outputs_QGISEXTRACTBYATTRIBUTE_5['OUTPUT'],minimumareaofholesinvegetationwalkfightpolygonsmeters,vegetationwalkfight)