#!/usr/bin/env python
# coding: utf-8

# # Exemples basiques de tracé avec Matplotlib
# 
# Matplotlib fournit de nombreuses options de traçage pour visualiser les données. Vous pouvez également personnaliser vos graphiques en offrant une variété d'options de thème, de couleur et de palette que les utilisateurs peuvent utiliser pour interagir avec leurs graphiques.
# 
# ## Premier tracé avec Matplotlib
# 
# Maintenant, nous allons commencer à produire des tracés. Voici le premier exemple :
# 

# In[1]:


import matplotlib.pyplot as plt

plt.plot([1, 3, 2, 4], 'b-')

plt.show( )


# `plt.plot([1, 3, 2, 4], 'b-')`
# 
# Cette ligne de code est la commande de traçage proprement dite. Seule une liste de valeurs a été tracée qui représente les coordonnées verticales des points à tracer. Matplotlib utilisera une liste de valeurs horizontales implicites, de 0 (la première valeur) à N-1 (où N est le nombre d'éléments dans la liste).
# 
# **Spécifier les deux listes**
# 
# De plus, nous pouvons spécifier explicitement les deux listes comme suit :
# 
# `x3 = range(6)`
# 
# `plt.plot(x3, [xi**2 for xi in x3])`
# 
# `plt.show()`

# In[2]:


import matplotlib.pyplot as plt
import numpy as np

x3 = np.arange(0.0, 6.0, 0.01) 

plt.plot(x3, [xi**2 for xi in x3], 'b-') 

plt.show()


# ## Tracés multilignes
# 
# Les Tracés multilignes signifient tracer plus d'une parcelle sur la même figure. Nous pouvons tracer plus d'un graphique sur la même figure.
# Cela peut être réalisé en traçant toutes les lignes avant d'appeler show(). Cela peut être fait comme suit :

# In[3]:


import matplotlib.pyplot as plt

x4 = range(1, 5)

plt.plot(x4, [xi*1.5 for xi in x4])

plt.plot(x4, [xi*3 for xi in x4])

plt.plot(x4, [xi/3.0 for xi in x4])

plt.show()


# ## Line plot
# 
# Un tracé linéaire visualise les informations sous la forme d'une série de points de données appelés marqueurs reliés par des segments de ligne droite.

# In[4]:


import matplotlib.pyplot as plt
import numpy as np 

# Create a figure
figure1 = plt.figure()
# Create the axe
axe1 = plt.axes()

x1 = np.linspace(0,10,1000)

axe1.plot(x1,np.sin(x1),'b-')


# ## Scatter Plot
# 
# Un autre type de graphique couramment utilisé est le nuage de points. Ici, les points sont représentés individuellement par un point ou un cercle.
# 
# **Scatter Plot avec plt.plot()**
# 
# Nous avons utilisé plt.plot/ax.plot pour produire des tracés linéaires. Nous pouvons utiliser les mêmes fonctions pour produire les nuages de points comme suit :

# In[5]:


import matplotlib.pyplot as plt
import numpy as np 

x7 = np.linspace(0, 10, 30)

y7 = np.sin(x7)

plt.plot(x7, y7, 'o', color = 'black');


# ## Histogram
# 
# Les histogrammes sont un affichage graphique des fréquences. Ils sont représentés sous forme de barres. Ils montrent quelle partie de l'ensemble de données appartient à chaque catégorie, généralement spécifiée sous forme d'intervalles sans chevauchement. Ces catégories sont appelées bacs.
# 
# La fonction plt.hist() peut être utilisée pour tracer un histogramme simple comme suit :

# In[6]:


import matplotlib.pyplot as plt
import numpy as np 

d1 = np.random.randn(1000)

plt.hist(d1)


# ## Bar chart
# 
# Les graphiques à barres affichent des barres rectangulaires sous forme verticale ou horizontale. Leur longueur est proportionnelle aux valeurs qu'ils représentent. Ils sont utilisés pour comparer deux ou plusieurs valeurs.
# 
# Nous pouvons tracer un graphique à barres en utilisant la fonction plt.bar(). Nous pouvons tracer un graphique à barres comme suit :

# In[7]:


import matplotlib.pyplot as plt

d1 = [5.,10.,40.,30]

plt.bar(range(len(d1)),d1)

plt.show()


# ## Horizontal Bar Chart
# 
# Nous pouvons produire un graphique à barres horizontales en utilisant la fonction plt.barh(). C'est l'équivalent strict de la fonction plt.bar().

# In[8]:


import matplotlib.pyplot as plt

data2 = [5. , 25. , 50. , 20.]

plt.barh(range(len(data2)), data2)

plt.show() 


# ## Pie chart
# 
# Pie charts sont des représentations circulaires, divisées en secteurs. Les secteurs sont également appelés coins. La longueur d'arc de chaque secteur est proportionnelle à la quantité que nous décrivons. C'est un moyen efficace de représenter des informations lorsque nous nous intéressons principalement à comparer le coin à l'ensemble du gâteau, plutôt que les coins les uns contre les autres.
# 
# Matplotlib fournit la fonction pie() pour tracer des camemberts à partir d'un tableau X. Les coins sont créés proportionnellement, de sorte que chaque valeur x du tableau X génère un coin proportionnel à x/sum(X).
# 

# In[9]:


import matplotlib.pyplot as plt

x1 = [20, 35, 30, 15]
fruit_labels = ["Banana", "Apple", "Strawberry", "Blueberry"]

plt.figure(figsize=(8, 8))
plt.pie(x1, labels=fruit_labels)
plt.legend(fruit_labels)

plt.show()


# ## Ajouter des étiquettes
# 
# Une autre information importante à ajouter à un tracé est les étiquettes des axes, car elles spécifient le type de données que nous traçons.

# In[10]:


import matplotlib.pyplot as plt

plt.plot([1, 3, 2, 4])

plt.xlabel('This is the X axis')

plt.ylabel('This is the Y axis')

plt.show()


# ## Ajouter un titre
# 
# Matplotlib fournit une simple fonction title() pour ajouter un titre à une image.

# In[11]:


import matplotlib.pyplot as plt

plt.plot([1, 3, 2, 4])

plt.title('First Plot')

plt.show()


# ## Ajout d'une légende
# 
# Les légendes sont utilisées pour décrire la signification de chaque ligne ou courbe dans le tracé.
# 
# Les légendes des courbes d'une figure peuvent être ajoutées de deux manières. Une méthode consiste à utiliser la méthode legend de l'objet axis et à passer une liste/tuple de textes de légende comme suit :

# In[12]:


import matplotlib.pyplot as plt
import numpy as np

x15 = np.arange(1, 5)

fig, ax = plt.subplots()

ax.plot(x15, x15*1.5)
ax.plot(x15, x15*3.0)
ax.plot(x15, x15/3.0)

ax.legend(['Normal','Fast','Slow']);

