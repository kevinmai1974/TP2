import matplotlib.pyplot as plt

# =========================
# Données du problème
# =========================
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

# =========================
# Résultats réels
# =========================
score_strat1 = 446
score_strat2 = 516
score_strat3 = 516
score_pulp = 524

# Solution PuLP valide
equipe_A_pulp = ["Alice", "Bob", "Clara"]
equipe_B_pulp = ["David", "Emma", "Hugo"]

# =========================
# Fonctions utiles
# =========================
def trouver_joueur(nom):
    for j in joueurs:
        if j["nom"] == nom:
            return j
    return None

def total_salaire(equipe):
    return sum(trouver_joueur(nom)["salaire"] for nom in equipe)

def total_poids(equipe):
    return sum(trouver_joueur(nom)["poids"] for nom in equipe)

def total_score(equipe):
    return sum(trouver_joueur(nom)["score"] for nom in equipe)

# =========================
# GRAPHE 1
# Comparaison des algorithmes
# =========================
labels = ["Stratégie 1", "Stratégie 2", "Stratégie 3", "PuLP"]
scores = [score_strat1, score_strat2, score_strat3, score_pulp]

plt.figure()
plt.bar(labels, scores)
plt.axhline(score_pulp, linestyle="--", label="Score optimal PuLP")
plt.title("Comparaison des scores")
plt.xlabel("Méthodes")
plt.ylabel("Score total")
plt.legend()
plt.tight_layout()
plt.savefig("graphe1_comparaison_scores.png")
plt.show()

# =========================
# GRAPHE 2
# Nombre d'appels récursifs
# =========================
compteur_naif = 0
compteur_memo = 0

def fib_naif(n):
    global compteur_naif
    compteur_naif += 1
    if n <= 1:
        return n
    return fib_naif(n - 1) + fib_naif(n - 2)

def fib_memo(n, memo=None):
    global compteur_memo
    if memo is None:
        memo = {}

    compteur_memo += 1

    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

valeurs_n = []
appels_naif = []
appels_memo = []

for n in range(1, 26):
    compteur_naif = 0
    compteur_memo = 0

    fib_naif(n)
    fib_memo(n)

    valeurs_n.append(n)
    appels_naif.append(compteur_naif)
    appels_memo.append(compteur_memo)

plt.figure()
plt.plot(valeurs_n, appels_naif, marker="o", label="fib_naif")
plt.plot(valeurs_n, appels_memo, marker="o", label="fib_memo")
plt.yscale("log")
plt.title("Nombre d'appels récursifs")
plt.xlabel("n")
plt.ylabel("Nombre d'appels (échelle log)")
plt.legend()
plt.tight_layout()
plt.savefig("graphe2_appels_recursifs.png")
plt.show()

# =========================
# GRAPHE 3
# Budget et poids par équipe (solution PuLP)
# =========================
budget_max = 8500
poids_max = 250

budget_A = total_salaire(equipe_A_pulp)
budget_B = total_salaire(equipe_B_pulp)

poids_A = total_poids(equipe_A_pulp)
poids_B = total_poids(equipe_B_pulp)

equipes = ["Équipe A", "Équipe B"]

budgets = [budget_A, budget_B]
poids = [poids_A, poids_B]

x = [0, 1]
largeur = 0.35

plt.figure()
plt.bar([i - largeur / 2 for i in x], budgets, width=largeur, label="Budget utilisé")
plt.bar([i + largeur / 2 for i in x], poids, width=largeur, label="Poids total")

plt.axhline(budget_max, linestyle="--", label="Budget maximal (8500)")
plt.axhline(poids_max, linestyle=":", label="Poids maximal (250)")

plt.xticks(x, equipes)
plt.title("Répartition du budget et du poids par équipe")
plt.ylabel("Valeur")
plt.legend()
plt.tight_layout()
plt.savefig("graphe3_budget_poids.png")
plt.show()

# =========================
# GRAPHE 4
# Profil des joueurs sélectionnés
# =========================
joueurs_selectionnes = equipe_A_pulp + equipe_B_pulp

noms = []
scores_sel = []
salaires_sel = []
poids_sel = []

for nom in joueurs_selectionnes:
    j = trouver_joueur(nom)
    noms.append(j["nom"])
    scores_sel.append(j["score"])
    salaires_sel.append(j["salaire"])
    poids_sel.append(j["poids"])

def normaliser(liste):
    minimum = min(liste)
    maximum = max(liste)
    return [(val - minimum) / (maximum - minimum) for val in liste]

scores_norm = normaliser(scores_sel)
salaires_norm = normaliser(salaires_sel)
poids_norm = normaliser(poids_sel)

x = range(len(noms))
largeur = 0.25

plt.figure()
plt.bar([i - largeur for i in x], scores_norm, width=largeur, label="Score normalisé")
plt.bar(x, salaires_norm, width=largeur, label="Salaire normalisé")
plt.bar([i + largeur for i in x], poids_norm, width=largeur, label="Poids normalisé")

plt.xticks(list(x), noms)
plt.title("Profil des joueurs sélectionnés (solution PuLP)")
plt.ylabel("Valeur normalisée")
plt.legend()
plt.tight_layout()
plt.savefig("graphe4_profil_joueurs.png")
plt.show()