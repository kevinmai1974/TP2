from pulp import *

joueurs = [
    {"nom": "Alice", "score": 88, "salaire": 1200, "poids": 72},
    {"nom": "Bob", "score": 91, "salaire": 1800, "poids": 85},
    {"nom": "Clara", "score": 84, "salaire": 950, "poids": 68},
    {"nom": "David", "score": 93, "salaire": 2100, "poids": 90},
    {"nom": "Emma", "score": 79, "salaire": 800, "poids": 65},
    {"nom": "Frank", "score": 87, "salaire": 2400, "poids": 95},
    {"nom": "Grace", "score": 85, "salaire": 1050, "poids": 70},
    {"nom": "Hugo", "score": 89, "salaire": 1600, "poids": 80}
]

model = LpProblem("Optimisation", LpMaximize)

xA = LpVariable.dicts("A", range(len(joueurs)), 0, 1, LpBinary)
xB = LpVariable.dicts("B", range(len(joueurs)), 0, 1, LpBinary)

# Objectif
model += lpSum(joueurs[i]["score"] * (xA[i] + xB[i]) for i in range(len(joueurs)))

# Contraintes
model += lpSum(xA[i] for i in range(len(joueurs))) == 3
model += lpSum(xB[i] for i in range(len(joueurs))) == 3

for i in range(len(joueurs)):
    model += xA[i] + xB[i] <= 1

model += lpSum(joueurs[i]["salaire"] * (xA[i] + xB[i])) <= 8500
model += lpSum(joueurs[i]["poids"] * xA[i]) <= 250
model += lpSum(joueurs[i]["poids"] * xB[i]) <= 250
model.solve()

def afficher(equipe):
    score = sum(j["score"] for j in equipe)
    salaire = sum(j["salaire"] for j in equipe)
    poids = sum(j["poids"] for j in equipe)
    return score, salaire, poids

A, B = [], []

for i in range(len(joueurs)):
    if xA[i].value() == 1:
        A.append(joueurs[i])
    if xB[i].value() == 1:
        B.append(joueurs[i])

print("Equipe A:", [j["nom"] for j in A])
print("Equipe B:", [j["nom"] for j in B])

print("Score total:", afficher(A)[0] + afficher(B)[0])