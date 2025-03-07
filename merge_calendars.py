import ics

def merge_ics_files(base_ics, easter_ics, output_ics):
    """Unisce due file .ics: festività e Pasqua ortodossa"""
    with open(base_ics, "r") as f:
        base_calendar = ics.Calendar(f.read())
    
    with open(easter_ics, "r") as f:
        easter_calendar = ics.Calendar(f.read())

    # Aggiunge gli eventi della Pasqua ortodossa al calendario principale
    base_calendar.events.update(easter_calendar.events)

    # Salva il nuovo file .ics
    with open(output_ics, "w") as f:
        f.write(str(base_calendar))
    
    print(f"File combinato salvato come {output_ics}")

# Esempio di utilizzo
merge_ics_files("festivitati_Original.ics", "paste_ortodox.ics", "calendar_actualizat.ics")
