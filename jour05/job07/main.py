def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note < 40:
            
            notes_arrondies.append(note)
        else:
            
            difference = 5 - (note % 5)
            if difference < 3:
                notes_arrondies.append(note + difference)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

notes_originales = [78, 42, 65, 91, 37]
notes_arrondies = arrondir_notes(notes_originales)

for i in range(len(notes_originales)):
    print(f"Note originale : {notes_originales[i]}, Note arrondie : {notes_arrondies[i]}")