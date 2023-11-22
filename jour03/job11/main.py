def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60
        minutes_restantes = minutes % 60

        if heures == 1:
            heures_str = "1 heure"
        else:
            heures_str = f"{heures} heures"

        if minutes_restantes == 1:
            minutes_str = "1 minute"
        else:
            minutes_str = f"{minutes_restantes} minutes"

        print(f"{heures_str} et {minutes_str}")
    else:
        print("Veuillez entrer un nombre entier positif.")

time_to_text(120)
time_to_text(75)
time_to_text(90)
time_to_text(50)
time_to_text(130)