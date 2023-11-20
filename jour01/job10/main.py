montant_initial = 10000.0
taux_rendement_annuel = 5.0 

gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print("Gain annuel initial :", gain_annuel)

montant_initial += 5000
taux_rendement_annuel += 2

gain_annuel_augmente = (taux_rendement_annuel / 100) * montant_initial
print("\nGain annuel après l'augmentation du capital et du taux de rendement :", gain_annuel_augmente)

retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1

nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print("\nNouveau gain annuel après le retrait et la diminution du taux de rendement :", nouveau_gain_annuel)

montant_final = montant_initial + nouveau_gain_annuel
print("\nMontant final de l'investissement après le retrait :", montant_final)