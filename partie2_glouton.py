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

def construire_equipes_glouton(joueurs, key_func):
    joueurs_tries = sorted(joueurs, key=key_func, reverse=True)

    A, B = [], []
    budget = 0
    poids_A = 0
    poids_B = 0

    for j in joueurs_tries:
        if len(A) < 3 and poids_A + j["poids"] <= 250:
            if budget + j["salaire"] <= 8500:
                A.append(j)
                budget += j["salaire"]
                poids_A += j["poids"]
                continue

        if len(B) < 3 and poids_B + j["poids"] <= 250:
            if budget + j["salaire"] <= 8500:
                B.append(j)
                budget += j["salaire"]
                poids_B += j["poids"]

    return A, B

# 3 stratégies
A1, B1 = construire_equipes_glouton(joueurs, lambda j: j["score"])
A2, B2 = construire_equipes_glouton(joueurs, lambda j: j["score"] / j["salaire"])
A3, B3 = construire_equipes_glouton(joueurs, lambda j: j["score"] / j["poids"])

def score(equipe):
    return sum(j["score"] for j in equipe)

print("Stratégie 1")
print("Équipe A :", [j["nom"] for j in A1])
print("Équipe B :", [j["nom"] for j in B1])
print("Score total :", score(A1) + score(B1))

print("\nStratégie 2")
print("Équipe A :", [j["nom"] for j in A2])
print("Équipe B :", [j["nom"] for j in B2])
print("Score total :", score(A2) + score(B2))

print("\nStratégie 3")
print("Équipe A :", [j["nom"] for j in A3])
print("Équipe B :", [j["nom"] for j in B3])
print("Score total :", score(A3) + score(B3))