##Removal of collisions of knolls with large boulders=name
##layerofcliffspolygons=vector
##radiusofknoll=number3.0
##layerofsmallknollspoints=vector
##radiusoflargeboulders=number4.5
##knolls=output vector
outputs_QGISFIXEDDISTANCEBUFFER_2=processing.runalg('qgis:fixeddistancebuffer', layerofcliffspolygons,radiusoflargeboulders,5.0,False,None)
outputs_QGISFIXEDDISTANCEBUFFER_1=processing.runalg('qgis:fixeddistancebuffer', layerofsmallknollspoints,radiusofknoll,5.0,False,None)
outputs_QGISEXTRACTBYLOCATION_1=processing.runalg('qgis:extractbylocation', outputs_QGISFIXEDDISTANCEBUFFER_1['OUTPUT'],outputs_QGISFIXEDDISTANCEBUFFER_2['OUTPUT'],['intersects'],0.1,None)
outputs_QGISDIFFERENCE_1=processing.runalg('qgis:difference', outputs_QGISFIXEDDISTANCEBUFFER_1['OUTPUT'],outputs_QGISEXTRACTBYLOCATION_1['OUTPUT'],True,None)
outputs_QGISPOLYGONCENTROIDS_1=processing.runalg('qgis:polygoncentroids', outputs_QGISDIFFERENCE_1['OUTPUT'],knolls)