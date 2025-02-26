Class Player:
	PosNumber
	Color
	Symbol

Class Board:
	# Loadders and Snakes
	Board_Entities = {
		SrcPosNumber : DstPosNumber,
	}
	VictoryOrder = []

	# While random genrating Board_Entities, avoid infinite loops
	# Avoid baord_Entities at 0 and 100



RNG():
	[x,y], Steps



main():
	NumberPlayers = Input()
	Init_Board()
	PlayersList = InitPlayers(NumberPlayers)
	NumPlayersinGame = NumberPlayers


	While NumPlayersinGame !=0 :
		for Player in PlayersList:
			Steps = RNG() # 1 - 6 # if Number 6 should give another chance for same player
			ChangePlayerPosbySteps(Player, Steps) # saerch recursively in board entities and avoid out of bound
			if Player.getPos = 100:
				NumPlayersinGame-=1
				baordClass.VictoryOrder.append(Player)


	# Outside While
	for Player in baordClass.VictoryOrder:



