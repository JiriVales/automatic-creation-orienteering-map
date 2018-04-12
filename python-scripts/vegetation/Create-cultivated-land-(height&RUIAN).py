##Create cultivated land (height&RUIAN)=name
##ruianparcelswithattributes=vector
##expressionforextractcorrespondingpolygonsfromruianbyattribute=string"druhpozemk" IN ('2')
##vegetationheightopenland=vector
##cultivatedland=output vector
outputs_QGISSELECTBYEXPRESSION_1=processing.runalg('qgis:selectbyexpression', ruianparcelswithattributes,expressionforextractcorrespondingpolygonsfromruianbyattribute,0)
outputs_QGISSAVESELECTEDFEATURES_1=processing.runalg('qgis:saveselectedfeatures', outputs_QGISSELECTBYEXPRESSION_1['RESULT'],None)
outputs_QGISEXTRACTBYLOCATION_1=processing.runalg('qgis:extractbylocation', vegetationheightopenland,outputs_QGISSAVESELECTEDFEATURES_1['OUTPUT_LAYER'],['intersects'],1.0,cultivatedland)