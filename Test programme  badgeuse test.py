import sqlite3
import pandas as pd

test_csv="C:/Users/Maxime/OneDrive/Bureau/iris.csv" #On choisit le csv auquel on aura besoin d'accéder
db_name="test.db"    #Permet de créer et de choisir le nom de la base de données
nom_table="iris_test" #nom de la table dans la base de données

conn=sqlite3.connect(db_name) #permet de "connecter" la base de données et python
cursor=conn.cursor() #Le curseur permet de donner une instruction à la base de données
cursor.execute(f"CREATE TABLE {nom_table} (sepal_length TEXT, sepal_width TEXT, petal_length TEXT, petal_width TEXT, species TEXT)")

""""Cette commande nous permet de créer la table. Il faut préciser entre accolades le nom de la table
défini avant. Entre les parenthèses, on définit une par une les colonnes en précisant les noms 
des colonnes en premier suivi du type de données que l'on met en majuscule. Il faut qu'il y ait 
exactement les mêmes noms de colonnes entre le csv et la base de données, le même nombre.

Si on veut ajouter une colonne à une base de données qui n'existe pas encore 
-> cursor.execute("ALTER TABLE nom_table ADD COLUMN colonne4 TEXT") """

conn.commit() #Permet de rendre effective la commande précédente dans la base de données

df=pd.read_csv(test_csv) #On lit le csv

df.to_sql(nom_table,conn,if_exists="append",index=False) 

"""le to_sql permet d'inscrire dans la base de données. Le if_exists="append" remplace la
base de données si elle existe déjà (par exemple si on la modifie et qu'on veut éviter les doublons)
et index=False permet d'éviter d'ajouter une colonne d'index dans la base de données"""

conn.close() #Permet de "déconnecter" la base de données et le csv.

"""Très important de déconnecter car cela nous permet ensuite d'accéder à la base de données
et de la changer d'emplacement
Attention si le programme plante avant la déconnexion, la base de données sera considérée ouverte
il faudra alors la supprimer manuellement et corriger le programme avant de le refaire tourner"""

"""test de petite modification pour voir ce qu'il se passe"""

"""je rajoute encore qqchose"""
