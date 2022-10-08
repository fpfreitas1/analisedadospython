#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python

# In[1]:


import pandas as pd


# In[2]:


dados = pd.read_excel("vendas.xlsx")


# In[3]:


dados


# # Análise Exploratória

# In[4]:


dados.shape


# In[9]:


dados.head()


# In[13]:


dados.tail()


# In[14]:


dados.describe()


# In[15]:


dados.head()


# In[17]:


dados.loja.value_counts()


# In[19]:


dados.tamanho.value_counts()


# In[20]:


dados.forma_pagamento.value_counts()


# In[21]:


dados.head()


# In[27]:


dados.groupby(["estado","loja"]).sum()


# # Gráficos

# In[28]:


get_ipython().system('pip install plotly_express')


# In[29]:


import plotly_express as px


# In[30]:


dados.head()


# In[33]:


px.histogram(dados, x="estado")


# In[39]:


px.histogram(dados, x="forma_pagamento",color="estado", text_auto=True)


# In[65]:


grafico = px.histogram(dados, x="regiao", y="preco", color="forma_pagamento", text_auto=True)
grafico.show()
grafico.write_html("grafico.html")


# In[66]:


lista_nomes = ["Felipe","Sueli","Juvencio", "Nathalia","Luna","Bia"]


# In[67]:


print(lista_nomes)


# In[68]:


for nome in lista_nomes:
    
    print(nome)


# In[73]:


lista_colunas = ["loja","cidade","estado","regiao","tamanho","local_consumo"]
for coluna in lista_colunas: 
    grafico = px.histogram(dados, x = coluna, y = "preco", color="forma_pagamento", text_auto=True)
    grafico.show()
    grafico.write_html(f"grafico-{coluna}.html")


# In[ ]:




