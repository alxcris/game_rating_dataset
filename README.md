## =====================ILIE Alexandru-Cristian GRUPA 313CC================= ##
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
## ===========Proiect PCLP3 - Analiza succesului jocurilor video============ ##

  Am ales tema aceasta pentru proiect deoarece imi place destul de mult partea
de gaming asa ca, bazat pe experiente aterioare, mi-a venit ideea sa antrenez
un model care poate prezice daca un joc va fi de succes sau nu, bazat pe notele
'metacritic' si alte categorii cum ar fi anul in care este lansat,sau recenzii
etc.

## ================================= Desciere ============================== ##

   Am utilizat API-ul celor de la RAWG(care e folosit de aplicatii precum 
discord) pentru a extrage cat mai multe date legate de jocuri.
   Am curatat datele de valorile care nu aduceau informatii relevante si am
tratat tipurile de date pentru a le face compatibile cu modelele de ML.
    Am definit coloana este_hit dupa  scorul metacritic.

## ========================== Structura Dataset-ului ======================= ##

Dataset-ul final contine 8 coloane:
1. nume(string) - Identificatorul jocului.
2. an_lansare(int) - Anul aparitiei jocului.
3. gen_principal(string) - Categoria jocului.
4. nr_platforme(int) - Numarul de platforme pe care este disponibil.
5. timp_joc_mediu(int) - Durata medie de terminare a jocului.
6. rating_utilizatori(float) - Ratingul oferit de comunitate.
7. nr_recenzii(int) - Numarul total de recenzii.
8. este_hit(int) - Coloana (1 pentru Hit, 0 pentru Non Hit).

## ============================== Antrenare Model ========================== ##

    In antrenarea modelului,ne-am folosit de regresia logistica din sci-kit learn
in care variabila x are rolul de a fi variabila analizata si y variabila de 
antrenare a modelului.Dupa ce verificam ca avem un numar de coloane egale 
(daca nu avem, umplem cu zero pana avem egalitate ca antrenarea sa fie valida)
iar apoi aplicam regresia lgoistica pentru antrenare.Dupa ce modelul s-a antrenat
ii analizam performanta si accuracy-ul,verificand aceste date cu matricea de
confuzie de unde reiese ca modelul nostru are 80% accuracy care e un procentaj
foarte ridicat pentru detectarea succesului jocurilor video.Modelul nostru,
asa cum se vede din matricea de confuzie, a detectat corect 83 de jocuri care
nu au fost Hit si a detectat corect 127 de jocuri care au fost Hit.Totusi,
acesta a prezis ca 27 de jocuri nu o sa fie Hit si au fost si a mai prezis ca
26 de jocuri o sa fie hit si nu au fost.Bazandu-ne pe realitate,destul de multe
jocuri foarte mari(cum ar fii Assassins Creed) cu ani de dezvoltare in spate,
ajung sa dezamageasca surprinzator desi sunt prezise ca fiind viitoare succese
ceea ce face acest scor al modelului sa fie si mai impresionant.

## ================================ Concluzii ============================== ##

    Din grafice, am observat faptul ca jocurile cu rating peste 3.9 tind sa fie
aproape mereu Hit, jocurile intre 3.5 si 4.2 sunt de obicei cele mai apreciate
de utilizatori,fapt care arata ca jocurile de la firmele mari si foarte
asteptate de comunitate tind sa fie mai dur criticate de catre utilizatori fata
de jocurile indie care surprins si ajung sa devina Hit.
    De asemenea observam ca modelul de regresie logistica din scikit-learn a
avut un succes foarte mare in prezicerea jocurilor de succes ceea ce ne arata
ca in general,desi sunt cazuri de exceptie ,comunitatea alaturi de notele date
de 'Metacritic' sunt relativ obiective,ceea ce face ca modelul sa poata prezice
bazat pe aceste informatii ce jocuri sunt de succes si de jocuri nu.

## ========================================================================= ##