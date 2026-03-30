import time

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

# Trier une seule fois
joueurs_tries = sorted(joueurs, key=lambda j: j["score"], reverse=True)

def score_cumule(joueurs, k):
    if k == 0:
        print("score_cumule(joueurs, 0) = 0")
        return 0

    precedent = score_cumule(joueurs, k - 1)
    resultat = precedent + joueurs[k - 1]["score"]
    print(f'score_cumule(joueurs, {k}) = {precedent} + {joueurs[k - 1]["score"]} ({joueurs[k - 1]["nom"]}) = {resultat}')
    return resultat

# Fibonacci modifié
fib0 = joueurs_tries[0]["score"]   # meilleur score
fib1 = joueurs_tries[1]["score"]   # deuxième meilleur score

def fib_naif(n):
    if n == 0:
        return fib0
    if n == 1:
        return fib1
    return fib_naif(n - 1) + fib_naif(n - 2)

memo = {}

def fib_memo(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return fib0
    if n == 1:
        return fib1

    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

# Test score_cumule
print("Test score_cumule :")
score_cumule(joueurs_tries, 3)

# Mesure du temps
print("\nMesure du temps pour n = 35")

debut = time.perf_counter()
resultat = fib_naif(35)
fin = time.perf_counter()
print(f"fib_naif(35) = {resultat}    Temps : {fin - debut:.3f} s")

debut = time.perf_counter()
resultat = fib_memo(35)
fin = time.perf_counter()
print(f"fib_memo(35) = {resultat}    Temps : {fin - debut:.6f} s")