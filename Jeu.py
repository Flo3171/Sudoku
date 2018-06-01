# coding: utf-8

import os
import csv
from random import randrange

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def test(colonneChoisie, ligneChoisie, valeurChoisie, sudoku):
	validite = 1
	for loop in range (1, 10):
		if (sudoku[loop ,ligneChoisie][0] == valeurChoisie) and (loop != colonneChoisie) :
			validite = 0
	for loop in range (1, 10):
		if (sudoku[colonneChoisie, loop][0] == valeurChoisie) and (loop != ligneChoisie):
			validite = 0
	col_carre = (colonneChoisie+2) // 3
	lig_carre = (ligneChoisie+2) // 3
	for loop in range (col_carre *3 -2 , col_carre *3 +1):
		for laap in range (lig_carre *3-2 , lig_carre *3+1):
			if (sudoku[loop , laap][0] == valeurChoisie) and (loop != colonneChoisie) and (laap != ligneChoisie):
				validite = 0
	return validite

def userInput(borne_low, borne_high, message):
	usrReturn = 0
	while usrReturn == 0:
		nombreChoisiSTR = input(message)
		try:
			nombreChoisi = int(nombreChoisiSTR)
			if (nombreChoisi >= borne_low) and (nombreChoisi <= borne_high) :
				usrReturn = 1
				return nombreChoisi
			else:
				print("Veuillez entrer un chiffre entre", borne_low, "et %d." % borne_high)
				print()
		except:
			print("Caractere invalide. Veuillez entrer un chiffre.")

rejouer = 1
while rejouer == 1:
	difficulteeChoisie = userInput(1,3,"""Choisissez une difficulté :
1 --> Facile
2 --> Moyen
3 --> Difficile
""")
	
	clear()
	
	inputWay = userInput(1,3,"""De quelle façon souhaitez-vous entrer les valeurs dans le sudoku ?
1 --> Valeur à mettre dans la case, puis coordonnées (recommandé)
2 --> Coordonnées, puis valeur à mettre dans la case (non recommandé)
3 --> Valeur à mettre dans la case, puis choix du carré, puis choix de la case dans le carré (joueurs expérimentés)
""")
	
	if difficulteeChoisie == 1:
		sudokuChoisi = randrange(1,5)

	elif difficulteeChoisie == 2:
		sudokuChoisi = 6

	else:
		sudokuChoisi = 5

	clear()

	sudoku = {}
	colTemp = 1
	ligTemp = 0
	with open('grille_%d.csv' % sudokuChoisi) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=';')
		for row in readCSV:
			ligTemp += 1
			if ligTemp == 10:
				colTemp += 1
				ligTemp = 1

			sudoku[colTemp , ligTemp] = [row[0], int(row[1]), int(row[2])]

	game = 1
	while game == 1:
	
		nbValides = 81
	
		for col in range(1, 10):
			for lig in range(1, 10):
				nbValides -= sudoku[col , lig][2]
	
		print("""             1 2 3   4 5 6   7 8 9
	   +-------+-------+-------+
	1  |""",sudoku[1 , 1][0],sudoku[2 , 1][0],sudoku[3 , 1][0],"""|""",sudoku[4 , 1][0],sudoku[5 , 1][0],sudoku[6 , 1][0],"""|""",sudoku[7 , 1][0],sudoku[8 , 1][0],sudoku[9 , 1][0],"""|
	2  |""",sudoku[1 , 2][0],sudoku[2 , 2][0],sudoku[3 , 2][0],"""|""",sudoku[4 , 2][0],sudoku[5 , 2][0],sudoku[6 , 2][0],"""|""",sudoku[7 , 2][0],sudoku[8 , 2][0],sudoku[9 , 2][0],"""|
	3  |""",sudoku[1 , 3][0],sudoku[2 , 3][0],sudoku[3 , 3][0],"""|""",sudoku[4 , 3][0],sudoku[5 , 3][0],sudoku[6 , 3][0],"""|""",sudoku[7 , 3][0],sudoku[8 , 3][0],sudoku[9 , 3][0],"""|
	   +-------+-------+-------+
	4  |""",sudoku[1 , 4][0],sudoku[2 , 4][0],sudoku[3 , 4][0],"""|""",sudoku[4 , 4][0],sudoku[5 , 4][0],sudoku[6 , 4][0],"""|""",sudoku[7 , 4][0],sudoku[8 , 4][0],sudoku[9 , 4][0],"""|
	5  |""",sudoku[1 , 5][0],sudoku[2 , 5][0],sudoku[3 , 5][0],"""|""",sudoku[4 , 5][0],sudoku[5 , 5][0],sudoku[6 , 5][0],"""|""",sudoku[7 , 5][0],sudoku[8 , 5][0],sudoku[9 , 5][0],"""|
	6  |""",sudoku[1 , 6][0],sudoku[2 , 6][0],sudoku[3 , 6][0],"""|""",sudoku[4 , 6][0],sudoku[5 , 6][0],sudoku[6 , 6][0],"""|""",sudoku[7 , 6][0],sudoku[8 , 6][0],sudoku[9 , 6][0],"""|
	   +-------+-------+-------+
	7  |""",sudoku[1 , 7][0],sudoku[2 , 7][0],sudoku[3 , 7][0],"""|""",sudoku[4 , 7][0],sudoku[5 , 7][0],sudoku[6 , 7][0],"""|""",sudoku[7 , 7][0],sudoku[8 , 7][0],sudoku[9 , 7][0],"""|
	8  |""",sudoku[1 , 8][0],sudoku[2 , 8][0],sudoku[3 , 8][0],"""|""",sudoku[4 , 8][0],sudoku[5 , 8][0],sudoku[6 , 8][0],"""|""",sudoku[7 , 8][0],sudoku[8 , 8][0],sudoku[9 , 8][0],"""|
	9  |""",sudoku[1 , 9][0],sudoku[2 , 9][0],sudoku[3 , 9][0],"""|""",sudoku[4 , 9][0],sudoku[5 , 9][0],sudoku[6 , 9][0],"""|""",sudoku[7 , 9][0],sudoku[8 , 9][0],sudoku[9 , 9][0],"""|
	   +-------+-------+-------+

	Il reste""",nbValides,"""cases invalides.
	""")
	
		if nbValides > 0:
			if inputWay == 1:
				valeurChoisie = userInput(0,9,"Valeur à écrire dans la case (0 si vous souhaitez laisser la case vide) :")
				colonneChoisie = userInput(1,9,"Choisissez une colonne :")
				ligneChoisie = userInput(1,9,"Choisissez une ligne :")
				
			elif inputWay == 2:
				colonneChoisie = userInput(1,9,"Choisissez une colonne :")
				ligneChoisie = userInput(1,9,"Choisissez une ligne :")
				valeurChoisie = userInput(0,9,"Valeur à écrire dans la case (0 si vous souhaitez laisser la case vide) :")
			
			else:
				valeurChoisie = userInput(0,9,"Valeur à écrire dans la case (0 si vous souhaitez laisser la case vide) :")
				carreChoisi = userInput(1,9,"Carré choisie, utilisez le pavé numérique :")
				caseChoisie = userInput(1,9,"Case choisie, utilisez le pavé numérique :")
				
				if carreChoisi == (7 or 4 or 1):
					if caseChoisie == (7 or 4 or 1):
						colonneChoisie = 1
					elif caseChoisie == (8 or 5 or 2):
						colonneChoisie = 2
					else:
						colonneChoisie = 3
				
				elif carreChoisi == (8 or 5 or 2):
					if caseChoisie == (7 or 4 or 1):
						colonneChoisie = 4
					elif caseChoisie == (8 or 5 or 2):
						colonneChoisie = 5
					else:
						colonneChoisie = 6
				
				else:
					if caseChoisie == (7 or 4 or 1):
						colonneChoisie = 7
					elif caseChoisie == (8 or 5 or 2):
						colonneChoisie = 8
					else:
						colonneChoisie = 9
				
				if carreChoisi == (7 or 8 or 9):
					if caseChoisie == (7 or 8 or 9):
						ligneChoisie = 1
					elif caseChoisie == (4 or 5 or 6):
						ligneChoisie = 2
					else:
						ligneChoisie = 3
						
				elif carreChoisi == (4 or 5 or 6):
					if caseChoisie == (7 or 8 or 9):
						ligneChoisie = 4
					elif caseChoisie == (4 or 5 or 6):
						ligneChoisie = 5
					else:
						ligneChoisie = 6
				
				else:
					if caseChoisie == (7 or 8 or 9):
						ligneChoisie = 7
					elif caseChoisie == (4 or 5 or 6):
						ligneChoisie = 8
					else:
						ligneChoisie = 9
				print(colonneChoisie)
				print(ligneChoisie)
				input()
				
			if sudoku[colonneChoisie , ligneChoisie][1] == 1:
				print("Cette case n'est pas modifiable. Veuillez en choisir une autre.")
				input("Appuyez sur entrée pour continuer.")
		
			elif valeurChoisie == 0:
				sudoku[colonneChoisie , ligneChoisie][2] = 0
				sudoku[colonneChoisie , ligneChoisie][0] = " "
		
			else:
				validite = test(colonneChoisie, ligneChoisie, valeurChoisie, sudoku)
				sudoku[colonneChoisie , ligneChoisie][2] = validite
				sudoku[colonneChoisie , ligneChoisie][0] = valeurChoisie
		else:
			game = 0
		clear()

	rejouer = userInput(1,2,"""Félicitations ! Vous avez gagné (rien du tout) !

Voulez-vous rejouer ?
1 --> Volontiers !
2 --> Au revoir!""")
