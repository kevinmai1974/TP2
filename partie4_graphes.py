import matplotlib.pyplot as plt

# 1. Comparaison
labels = ["Strat1", "Strat2", "Strat3", "PuLP"]
values = [510, 516, 520, 524]

plt.bar(labels, values)
plt.axhline(524)
plt.title("Comparaison des scores")
plt.show()

# 2. Fibonacci appels
# (déjà vu dans code précédent avec compteur)

# 3. Budget / poids
# (tu peux utiliser les résultats de A et B)