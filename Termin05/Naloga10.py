# Program, ki izvede osnovne operacije (seštevanje, odštevanje, množenje) med dvema 3x3 matrikama
# Opomba: Matrike so predstavljene kot seznam seznamov

#Input: Matrika1 [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
#Input: Matrika2 [[9, 8, 7], [6, 5, 4], [3, 2, 1]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]	
#Output (za seštevanje): [[10, 10, 10], [10, 10, 10], [10, 10, 10]]

def sestej_matriki(matrika1, matrika2):
    return [[matrika1[i][j] + matrika2[i][j] for j in range(len(matrika1[0]))] for i in range(len(matrika1))]

def odstej_matriki(matrika1, matrika2):
    return [[matrika1[i][j] - matrika2[i][j] for j in range(len(matrika1[0]))] for i in range(len(matrika1))]


