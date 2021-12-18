#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[15]:


import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="",
  database='schooldb'
)
cursor = dataBase.cursor()

query = ("select * from studentteacher")

cursor.execute(query)
 
#print(dataBase)
for (name) in cursor:
  print(name)
# Disconnecting from the server
cursor.close()
dataBase.close()


# In[ ]:




