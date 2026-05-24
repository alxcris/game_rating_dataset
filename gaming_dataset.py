import requests
import pandas as pd
from dotenv import load_dotenv

#ca sa nu dam reveal la api_key(ca sa il pun pe github)
load_dotenv()

API_KEY = "c5f0fbc2e0f74b24842f4a29c129b927" 
URL = "https://api.rawg.io/api/games?key=" + "c5f0fbc2e0f74b24842f4a29c129b927"
+ "&page_size=40"

toate_jocurile = [] #o lista goala cu jocurile rand pe rand

#trecem prin primele 25 de pagini (25 * 40 = 1000 de jocuri)
for pagina in range(1, 26):
    #cerere catre site
    link_pagina = f"{URL}&page={pagina}"
    raspuns = requests.get(link_pagina)
    
    #daca statusul e 200,inseamna ca e ok
    if(raspuns.status_code == 200):
        #incepem formarea unui hashtable pentru jocul curent
        date_dictionar = raspuns.json()
        
        #results este cheia sub care se află lista cu jocurile de pe pagina curentă
        for joc in date_dictionar['results']:
            
            #verificam daca jocul are o nota de la metacritic
            if(joc.get('metacritic') != 0):
                
                # Extragem genul cu if/else normal ca să fie ușor de înțeles
                if len(joc.get('genres', [])) > 0:
                    gen = joc['genres'][0]['name']
                else:
                    gen = "Unknown"
                
                #luam anul lansarii jocului
                if(joc.get('released') != 0):
                    an = int(joc['released'][:4]) 
                else:
                    an = 0
                
                #facem un hashtable cu datele fiecarui jocului
                joc_curent = {
                    'nume': joc.get('name'),
                    'an_lansare': an,
                    'gen_principal': gen,
                    'nr_platforme': len(joc.get('platforms', [])),
                    'timp_joc_mediu': joc.get('playtime', 0),
                    'rating_utilizatori': joc.get('rating', 0),
                    'metacritic': joc['metacritic']
                }
                
                #salvam hashtableul in lista de jocuri
                toate_jocurile.append(joc_curent)
                
        print(f"Am terminat de citit pagina {pagina}.")

#facem lista de hashtable intr-un dataframe
df = pd.DataFrame(toate_jocurile)

#daca scorul metacritic e mai mare ca 80,salvam 1 pentru hit,altfel 0
df['este_hit'] = (df['metacritic'] >= 80).astype(int)

# Ștergem coloana metacritic initiala ca trainingul sa nu fie biased
df = df.drop(columns=['metacritic'], axis=1) 

#facem un fisier csv pentru tabel
df.to_csv("dataset_jocuri.csv", index=False)

print(f"\nAu fost salvate {len(df)} jocuri cu succes.")