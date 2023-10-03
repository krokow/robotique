# -*- coding: utf-8 -*-

def executer_requete_SQL(chemin_base_de_donnees, requete):
    try:
        conn = sqlite3.connect(chemin_base_de_donnees)
        cur = conn.cursor()
        
        cur.execute(requete)
        resultat = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        
        return resultat
    
    
    except sqlite3.Error as error:
        print("Erreur lors de la connexion à SQLite", error)


def ajouter_ligne (numero_badgeuse, chemin_bdd, tuple_nom_colonnes, tab_informations): #tab_informations est un tableau contenant chaque élément à ajouter sur la ligne
	nom_table = "nouveau"
	#nom_table = ... en fonction du numéro de badgeuse
	
	
	#On doit convertir le tableau en chaine de caractere de la bonne manière pour ensuite lancer la requete
	str_informations = '('
	for elt in tab_informations[:-1]:
		str_informations += '"' + elt + '",'

	str_informations += '"' + tab_informations[-1] + '")'
	
	requete = f"INSERT INTO {nom_table} {tuple_nom_colonnes} VALUES {str_informations}"
	
	executer_requete_SQL(chemin_bdd, requete)



def retirer_ligne (numero_badgeuse, chemin_bdd, id_autorisation):
	nom_table = "nouveau"
	#nom_table = ... en fonction du numéro de badgeuse
	
	requete = f"DELETE FROM {nom_table} WHERE id={id_autorisation}"
	
	executer_requete_SQL(chemin_bdd, requete)

