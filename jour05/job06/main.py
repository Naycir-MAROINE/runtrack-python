def distance_toilettes_par_semaine(nombre_marches, hauteur_marche):
    nombre_jours_semaine = 7
    nombre_allers_retours_par_jour = 2

    distance_parcourue_par_marche = (nombre_allers_retours_par_jour - 1) * hauteur_marche  # La première montée n'est pas comptée
    distance_totale_par_semaine = nombre_jours_semaine * nombre_marches * distance_parcourue_par_marche / 100  # Convertir en mètres

    return distance_totale_par_semaine

nombre_marches = 100
hauteur_marche = 20
distance_parcourue = distance_toilettes_par_semaine(nombre_marches, hauteur_marche)

print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_parcourue:.2f} m par semaine.")