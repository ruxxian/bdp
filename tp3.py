def chercher_pivot(M, l, c):
    max_val = abs(M[l][c])
    max_row = l
    for i in range(l + 1, len(M)):
        if abs(M[i][c]) > max_val:
            max_val = abs(M[i][c])
            max_row = i
    return max_row

def echange_lignes(M, i, j):
    M[i], M[j] = M[j], M[i]

def remplace_par_combinaison(M, i, j, mu):
    n = len(M[j])
    for k in range(n):
        M[j][k] += mu * M[i][k]

def echelonner(M):
    M = [row.copy() for row in M]
    n_lignes = len(M)
    n_colonnes = len(M[0]) if n_lignes > 0 else 0
    ligne_pivot = 0
    colonne_pivot = 0
    
    while ligne_pivot < n_lignes and colonne_pivot < n_colonnes:
        i_max = chercher_pivot(M, ligne_pivot, colonne_pivot)
        
        if M[i_max][colonne_pivot] == 0:
            colonne_pivot += 1
        else:
            if i_max != ligne_pivot:
                echange_lignes(M, ligne_pivot, i_max)
            
            for i in range(ligne_pivot + 1, n_lignes):
                mu = -M[i][colonne_pivot] / M[ligne_pivot][colonne_pivot]
                remplace_par_combinaison(M, ligne_pivot, i, mu)
            
            ligne_pivot += 1
            colonne_pivot += 1
    
    return M

# Matrice de test
M = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

# Transformation en forme échelonnée
M_echelon = echelonner(M)

# Affichage du résultat
for ligne in M_echelon:
    print(ligne)