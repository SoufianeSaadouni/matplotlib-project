#!/usr/bin/env python
# coding: utf-8

# # Informations préliminaires
# 
# ## Affichage des tracés dans Matplotlib
# 
# L'affichage du tracé Matplotlib est basé sur le contexte. La meilleure utilisation de Matplotlib diffère selon la façon dont nous l'utilisons. Il existe trois contextes applicables pour visualiser les tracés. Les trois contextes applicables utilisent le traçage à partir d'un script, le traçage à partir d'un shell IPython ou le traçage à partir d'un bloc-notes Jupyter.
# 
# ### Tracer à partir d'un script
# 
# Si nous utilisons Matplotlib à partir d'un script, la commande plt.show() est d'une grande utilité. Il démarre une boucle d'événements, recherche tous les objets de figure actuellement actifs et ouvre une ou plusieurs fenêtres interactives qui affichent la ou les figures.
# 
# La commande plt.show() ne doit être utilisée qu'une seule fois par session Python. Il ne doit être utilisé qu'à la fin du script. Plusieurs commandes plt.show() peuvent conduire à des résultats imprévisibles et doivent généralement être évitées.
# 
# ### Tracer à partir d'un shell IPython
# 
# Nous pouvons utiliser Matplotlib de manière interactive dans un shell IPython. IPython fonctionne bien avec Matplotlib si nous spécifions le mode Matplotlib. Pour activer ce mode, nous pouvons utiliser la commande %matplotlib après avoir démarré iPython. Toute commande plt plot entraînera l'ouverture d'une fenêtre de figure et d'autres commandes peuvent être exécutées pour mettre à jour le tracé.
# 
# ### Tracer à partir de Jupyter Notebook
# 
# Le Jupyter Notebook (anciennement connu sous le nom de IPython Notebook) est un outil d'analyse et de visualisation de données qui fournit plusieurs outils sous un même toit. Il fournit l'exécution de code, des tracés graphiques, un affichage de texte riche et multimédia, des formules mathématiques et bien d'autres fonctionnalités dans un seul document exécutable.
# 
# Le traçage interactif dans un Jupyter Notebook peut être effectué avec la commande %matplotlib. Il existe deux options possibles pour travailler avec des graphiques dans Jupyter Notebook. Ce sont les suivants :
# 
# • %matplotlib notebook – Cette commande produira des tracés interactifs intégrés dans le notebook.
# 
# • %matplotlib inline – Il produira des images statiques du tracé intégré dans le cahier.
# 
# Après cette commande (elle ne doit être effectuée qu'une seule fois par noyau et par session), toute cellule du bloc-notes qui crée un tracé intégrera une image PNG du graphique.
# 
# ## Hiérarchie des objets Matplotlib
# 
# Dans Matplotlib, un tracé est une hiérarchie d'objets Python imbriqués. Ahierarch signifie qu'il existe une structure arborescente d'objets Matplotlib sous-jacente à chaque tracé.
# 
# Un objet Figure est le conteneur le plus externe pour un tracé Matplotlib. L'objet Figure contient plusieurs objets Axes. Ainsi, la figure est le graphique final qui peut contenir un ou plusieurs axes. Les Axes représentent une parcelle individuelle.
# 
# Ainsi, nous pouvons considérer l'objet Figure comme un conteneur en forme de boîte contenant un ou plusieurs Axes. L'objet Axes contient des objets plus petits tels que des graduations, des lignes, des légendes, des titres et des zones de texte.
# 
# ## API Matplotlib
# 
# Matplotlib a deux API avec lesquelles travailler. Une interface basée sur l'état de style MATLAB et une interface orientée objet (OO) plus puissante. L'ancienne interface basée sur l'état de style MATLAB est appelée interface pyplot et la seconde est appelée interface orientée objet.
# 
# Il existe une troisième interface également appelée interface pyLab. Il fusionne pyplot (pour le traçage) et NumPy (pour les fonctions mathématiques) dans un environnement plus proche de MATLAB. Ceci est considéré comme une mauvaise pratique de nos jours. Ainsi, l'utilisation de pyLab est fortement déconseillée et par conséquent, je n'en discuterai pas plus avant.
# 
# 
# ## API Pyplot
# 
# `matplotlib.pyplot` est une collection de fonctions qui font fonctionner matplotlib comme MATLAB. Chaque fonction pyplot apporte des modifications à une figure : par exemple, crée une figure, crée une zone de traçage dans une figure, trace certaines lignes dans une zone de traçage, décore le tracé avec des étiquettes, etc.
# 
# Dans `matplotlib.pyplot`, divers états sont conservés à travers les appels de fonction, de sorte qu'il garde une trace de choses comme la figure actuelle et la zone de traçage, et les fonctions de traçage sont dirigées vers les axes actuels (veuillez noter que les "axes" ici et dans la plupart des endroits dans la documentation fait référence à la partie des axes d'une figure et non au terme mathématique strict pour plus d'un axe).
# 
# Le code suivant produit des courbes sinus et cosinus à l'aide de l'API Pyplot:

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


x1 = np.linspace(0, 10, 100)

# create a plot figure
plt.figure()


# create the first of two panels and set current axis
plt.subplot(2, 1, 1)   # (rows, columns, panel number)
plt.plot(x1, np.sin(x1))


# create the second of two panels and set current axis
plt.subplot(2, 1, 2)   # (rows, columns, panel number)
plt.plot(x1, np.cos(x1));


# ### Visualisation avec Pyplot
# 
# Générer une visualisation avec Pyplot est très simple. Les valeurs de l'axe des x vont de 0 à 3 et l'axe des y de 1 à 4. Si nous fournissons une seule liste ou un seul tableau à la commande plot(), matplotlib suppose qu'il s'agit d'une séquence de valeurs y et génère automatiquement les valeurs x. Étant donné que les plages python commencent par 0, le vecteur x par défaut a la même longueur que y mais commence par 0. Par conséquent, les données x sont [0,1,2,3] et les données y sont [1,2,3,4].

# In[2]:


import matplotlib.pyplot as plt


plt.plot([1, 2, 3, 4])
plt.ylabel('Numbers')
plt.show()


# ### plot() - Une commande polyvalente
# 
# plot() est une commande polyvalente. Il faudra un nombre arbitraire d'arguments. Par exemple, pour tracer x par rapport à y, nous pouvons émettre la commande suivante:

# In[3]:


import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()


# ### Interface de machine d'état
# 
# Pyplot fournit l'interface de machine d'état à la bibliothèque de traçage orientée objet sous-jacente. La machine à états crée implicitement et automatiquement des figures et des axes pour obtenir le tracé souhaité. Par example:

# In[4]:


import matplotlib.pyplot as plt

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()


# ### Formatage du style de tracé
# 
# Pour chaque paire d'arguments x, y, il existe un troisième argument facultatif qui est la chaîne de format qui indique la couleur et le type de ligne du tracé. Les lettres et symboles de la chaîne de format proviennent de MATLAB. Nous pouvons concaténer une chaîne de couleur avec une chaîne de style de ligne. La chaîne de format par défaut est 'b-', qui est une ligne bleue continue. Par exemple, pour tracer la ligne ci-dessus avec des cercles rouges, nous lancerions la commande suivante :

# In[5]:


import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()


# La commande axis() dans l'exemple ci-dessus prend une liste de [xmin, xmax, ymin, ymax] et spécifie la fenêtre d'affichage des axes.
# 
# ## API orientée objet
# 
# L'API orientée objet est disponible pour les situations de traçage plus complexes. Cela nous permet d'exercer plus de contrôle sur la figure. Dans l'API Pyplot, nous dépendons d'une notion de figure ou d'axes "actifs". Mais, dans l'API orientée objet, les fonctions de traçage sont des méthodes d'objets Figure et Axes explicites.
# 
# La figure est le conteneur de niveau supérieur pour tous les éléments de tracé. Nous pouvons considérer l'objet Figure comme un conteneur en forme de boîte contenant un ou plusieurs Axes.
# 
# Les Axes représentent une parcelle individuelle. L'objet Axes contient des objets plus petits tels que des axes, des graduations, des lignes, des légendes, des titres et des zones de texte.
# 
# Le code suivant produit des courbes sinus et cosinus à l'aide de l'API orientée objet.

# In[6]:


import matplotlib.pyplot as plt

# First create a grid of plots
# ax will be an array of two Axes objects
fig, ax = plt.subplots(2)


# Call plot() method on the appropriate object
ax[0].plot(x1, np.sin(x1), 'b-')
ax[1].plot(x1, np.cos(x1), 'b-');


# ### Objets et référence
# 
# L'idée principale avec l'API orientée objet est d'avoir des objets sur lesquels on peut appliquer des fonctions et des actions. Le véritable avantage de cette approche devient apparent lorsque plus d'une figure est créée ou lorsqu'une figure contient plus d'une sous-parcelle.
# 
# Nous créons une référence à l'instance figure dans la variable fig. Ensuite, nous créons une nouvelle instance d'axe axes en utilisant la méthode add_axes dans l'instance de classe Figure fig comme suit :

# In[7]:


import matplotlib.pyplot as plt

fig = plt.figure()

x2 = np.linspace(0, 5, 10)
y2 = x2 ** 2

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes.plot(x2, y2, 'r')

axes.set_xlabel('x2')
axes.set_ylabel('y2')
axes.set_title('title');


# ### Figure et Subplots
# 
# nous commençons par créer une figure et un axe. Une figure et des axes peuvent être créés comme suit :
# 
# `fig = plt.figure()`
# 
# `hache = plt.axes()`
# 
# Dans Matplotlib, la figure (une instance de la classe plt.Figure) est un conteneur unique qui contient tous les objets représentant les axes, les graphiques, le texte et les étiquettes. Les axes (une instance de la classe plt.Axes) est une boîte englobante avec des graduations et des étiquettes. Il contiendra les éléments de tracé qui composent la visualisation. J'ai utilisé le nom de variable fig pour faire référence à une instance de figure et ax pour faire référence à une instance d'axes ou à un groupe d'instances d'axes.

# In[8]:


import matplotlib.pyplot as plt

fig = plt.figure()

ax = plt.axes()

