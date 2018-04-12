##Create open land (height&RUIAN)=name
##ruianparcelswithattributes=vector
##expressionforextractcorrespondingpolygonsfromruianbyattribute=string"druhpozemk" IN ('5','7','8')
##vegetationheightopenland=vector
##openland=output vector
outputs_QGISSELECTBYEXPRESSION_1=processing.runalg('qgis:selectbyexpression', ruianparcelswithattributes,expressionforextractcorrespondingpolygonsfromruianbyattribute,0)
outputs_QGISSAVESELECTEDFEATURES_1=processing.runalg('qgis:saveselectedfeatures', outputs_QGISSELECTBYEXPRESSION_1['RESULT'],None)
outputs_QGISEXTRACTBYLOCATION_1=processing.runalg('qgis:extractbylocation', vegetationheightopenland,outputs_QGISSAVESELECTEDFEATURES_1['OUTPUT_LAYER'],['intersects'],1.0,openland)