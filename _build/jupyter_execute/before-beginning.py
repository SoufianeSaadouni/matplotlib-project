#!/usr/bin/env python
# coding: utf-8

# # Avant de commencer
# 
# ## Informations préliminaires
# 
# `matplotlib.pyplot` est une collection de fonctions qui font fonctionner Matplotlib comme MATLAB. Chaque fonction pyplot apporte des modifications à une figure : par exemple, crée une figure, crée une zone de traçage dans une figure, trace certaines lignes dans une zone de traçage, décore le tracé avec des étiquettes, etc.
# 
# exemple d'un simple diagram:

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

x_point = np.array([0,6])
y_point = np.array([0,150])

plt.plot(x_point, y_point)
plt.show()

