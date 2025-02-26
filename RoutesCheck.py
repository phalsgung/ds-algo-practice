
RoutesDict
SFO --> LAX, NYC, AUS
NYC --> BOS
LAX --> SFO
AUS --> SFO,NYC
SYD → LON
LON → SYD


SFO,BOS → TRUE
SFO,AUS → TRUE
SFO,SYD → FALSE


Data Structure
set(“SFO”, “LAX”, “NYC”, “AUS”, “BOS”)

# RouterRequestList = [SFO, BOS]
StartPoint = “SFO”
EndPoint = “BOS”

CheckRoutePresent(PointstoVisitList, StartPoint, EndPoint)

Code
Def CheckRoutePresent(PointstoVisitList, StartPoint, EndPoint):
	RouteSet = set()
	PointstoVisitList = [StartPoint]
	
	For StartPoint in RoutesDict:
		If StartPoint == RouterRequestList[0]:
PointstoVisitList.append(RouterRequestList[0])
PointFound =  CheckRoutePresent(PointstoVisitList, StartPoint, EndPoint)
		Elif PointFound == False:
			# Point not found in any keys
			Return True
			
		



		
	





