#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json as JSON
from ast import literal_eval


# In[2]:


API_TOKEN = 'dcceb75c3d9b14edf2ab6f3fb63a302fe3baf873'


# In[3]:


API_URL = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=dcceb75c3d9b14edf2ab6f3fb63a302fe3baf873'


# In[4]:


import requests
import json as JSON
from ast import literal_eval


# In[5]:


response = requests.get(API_URL)


# In[6]:


resultado_json = (response.content)


# In[7]:


json = resultado_json.decode('utf8').replace("'", '"')


# In[19]:


import os


# In[28]:


arquivo = open (os.path.expanduser("Documents/python/answer.json"), 'w')
arquivo.write(str(json))


# In[42]:


cifrado = (objeto['cifrado'])
casas = (objeto['numero_casas'])


# In[43]:


mensagem = (cifrado)


# In[44]:


key = int(1)


# In[45]:


Alfabeto = 'abcdefghijklmnopqrstuvwxyz'


# In[46]:


mensagem = mensagem.lower()


# In[47]:


decifrado = ''


# In[58]:


for caracter in mensagem:
    if caracter not in '!@#$%.,;123456789 ':
      posicao = Alfabeto.find(caracter)
      novaposicao = (posicao - key) % 26
      novocaracter = Alfabeto[novaposicao]
      decifrado += novocaracter
    else:
      decifrado += (caracter)
else:
    print('Nova mensagem criptografada:', decifrado)


# In[49]:


objeto['decifrado']= decifrado


# In[50]:


arquivo = open (os.path.expanduser("Documents/python/answer.json"), 'w')
arquivo.write(str(objeto))


# In[51]:


import hashlib
hash_object = hashlib.sha1()
hash_object.update(decifrado.encode('utf8')) 
print('Resumo Criptográfico:', hash_object.hexdigest())


# In[52]:


objeto['resumo_criptografico'] = hash_object.hexdigest()


# In[53]:


arquivo = open (os.path.expanduser("Documents/python/answer.json"), 'w')
arquivo.write(str(objeto))


# In[54]:


json_final = JSON.dumps(objeto)
arquivo = open (os.path.expanduser("Documents/python/answer.json"), 'w')
arquivo.write(str(objeto))


# In[69]:


answer = {'answer': open (os.path.expanduser('Documents/python/answer.json'), 'rb')}
url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=dcceb75c3d9b14edf2ab6f3fb63a302fe3baf873'
response = requests.post(url = url, files = answer)
print (response.text)
print (response.status_code)


# In[71]:


import requests
answer = {'numero_casas', 'token', 'cifrado', 'decifrado', 'resumo criptografico'}
resposta = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=dcceb75c3d9b14edf2ab6f3fb63a302fe3baf873', data=answer)
print (response.text)
print (response.status_code)


# In[ ]:




