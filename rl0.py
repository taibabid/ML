# -*- coding: utf-8 -*-
"""RL0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jd6DRuGIbbc0NckZZdrjIxmdvY3TH07U

# Importer les librairies
"""

import numpy as np #Numpy pour manipuler notre Dataset en tant que matrice
import matplotlib.pyplot as plt #Matplotlib.pyplot pour visualiser nos données
from sklearn.datasets import make_regression #La fonction make_regression de Sklearn pour générer un nuage de point (ici on va simuler des données)
from sklearn.linear_model import SGDRegressor #SGDRegressor (qui signifie Stochastic Gradient Descent Regressor) et qui contient le calcul de la Fonction Coût, des gradients, de l’algorithme de minimisation

"""# Créer un Dataset"""

np.random.seed(0) #Pour maitriser l’aléatoire, nous allons générer un tableau de données (𝒙, 𝒚) aléatoires
x, y = make_regression(n_samples=100, n_features=1, noise=10) #La fonction prend comme arguments le nombre d’échantillons à générer, le nombre de variables et le bruit puis nous retourne deux vecteurs 𝒙 et 𝒚.
plt.scatter(x, y) #pour visualiser nos données

"""# Développer le modèle et l’entraîner"""

model = SGDRegressor(max_iter=100, eta0=0.0001) #On défini nos model depuis le générateur SGDRegressor en entrant le nombre d’itérations que le Gradient Descent doit effectuer ainsi que le Learning Rate
model.fit(x,y) #On utilise la fonction fit pour l’entraîner

print('Coeff R2 =', model.score(x, y)) #On utilise la fonction score qui calcule le coefficient de détermination entre le modèle et les valeurs 𝒚 de notre Dataset pour observer la précision de notre modèle
plt.scatter(x, y) #pour visualiser nos données
plt.plot(x, model.predict(x), c='red', lw = 3) #On utilise notre modèle pour faire de nouvelles prédictions avec la fonction predict et tracer ces résultats avec la fonction plt.plot

"""Notre modèle semble vraiment mauvais. C’est parce que nous ne l’avons pas entraîné suffisamment longtemps et parce que le Learning rate était trop faible. Aucun problème, il est possible de le ré-entraîner avec de meilleurs hyper-paramètres.

En Machine Learning, les valeurs qui fonctionnent bien pour la plupart 
des entraînements sont :

• Nombre d’itérations = 1000

• Learning rate = 0.001
"""

model = SGDRegressor(max_iter=1000, eta0=0.001) 
model.fit(x,y)

print('Coeff R2 =', model.score(x, y)) 
plt.scatter(x, y) 
plt.plot(x, model.predict(x), c='red', lw = 3)

"""Notre modèle de Machine Learning fonctionne vraiment bien avec un coefficient 𝑅2 = 94%. Maintenant on peut en servir pour faire de bonnes prédictions ! """