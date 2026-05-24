import requests
import pandas as pd
import os

from sklearn.model_selection import train_test_split
from dotenv import load_dotenv

#ca sa nu dam reveal la api_key(ca sa il pun pe github)
load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = f"https://api.rawg.io/api/games?key={API_KEY}&page_size=40"

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
        
        #results este locul unde se afla lista cu jocurile de pe pagina
        for joc in date_dictionar['results']:
            
            #verificam daca jocul are o nota de la metacritic
            if(joc.get('metacritic') is not None):
                
                #vedem ce gen e jocul
                if(len(joc.get('genres', [])) > 0):
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
                    'nr_recenzii': joc.get('reviews_count', 0),
                    'nr_realizari': joc.get('achievements_count', 0),
                    'metacritic': joc['metacritic']
                }
                
                #salvam hashtableul in lista de jocuri
                toate_jocurile.append(joc_curent)
                
        print(f"pagina {pagina}.")

#facem lista de hashtable intr-un dataframe
df = pd.DataFrame(toate_jocurile)

#daca scorul metacritic e mai mare ca 80,salvam 1 pentru hit,altfel 0
df['este_hit'] = (df['metacritic'] >= 80).astype(int)

#adaugam df.drop pe metacritic ca modelul sa nu dea train doar pe metacritic
df = df.drop(columns=['metacritic'])

#impartim dataset-ul pentru tin si test
df_train, df_test = train_test_split(df, test_size=0.3, random_state=42)

#afisam numarul de date de train si de test pentru verificare
print(f"\nSet antrenare: {len(df_train)} instante.")
print(f"Set testare: {len(df_test)} instante.")

#punem dataset-ul de training si cel de test in fisiere diferite
df_train.to_csv("train_dataset.csv", index=False)
df_test.to_csv("test_dataset.csv", index=False)

print("Fisierele CSV s au format cu succes")