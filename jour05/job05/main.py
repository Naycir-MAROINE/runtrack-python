def chiffre_cesar(message, decalage):
    resultat = ""

    for char in message:
    
        if char.isalpha():
        
            est_majuscule = char.isupper()
            
            char_decale = chr((ord(char) - ord('A' if est_majuscule else 'a') + decalage) % 26 + ord('A' if est_majuscule else 'a'))

            resultat += char_decale
        else:
            
            resultat += char

    return resultat
message_original = "Hello, World!"
decalage = 3
message_chiffre = chiffre_cesar(message_original, decalage)

print(f"Message original: {message_original}")
print(f"Message chiffré : {message_chiffre}")