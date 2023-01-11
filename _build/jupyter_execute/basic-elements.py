#!/usr/bin/env python
# coding: utf-8

# ## Pie chart
# 

# In[1]:


import matplotlib.pyplot as plt

x1 = [20, 35, 30, 15]
fruit_labels = ["Banana", "Apple", "Strawberry", "Blueberry"]

plt.figure(figsize=(8, 8))
plt.pie(x1, labels=fruit_labels)
plt.legend(fruit_labels)

plt.show()


# ## Bar chart

# In[2]:


import matplotlib.pyplot as plt

d1 = [5.,10.,40.,30]

plt.bar(range(len(d1)),d1)

plt.show()


# ## Histogram

# In[3]:


import matplotlib.pyplot as plt
import numpy as np 

d1 = np.random.randn(1000)

plt.hist(d1)


# ## Line plot

# In[4]:


import matplotlib.pyplot as plt
import numpy as np 

# Create a figure
figure1 = plt.figure()
# Create the axe
axe1 = plt.axes()

x1 = np.linspace(0,10,1000)

axe1.plot(x1,np.sin(x1),'b-')

