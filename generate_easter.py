from datetime import date, timedelta
import ics

def orthodox_easter(year):
    """Calcola la data della Pasqua ortodossa in calendario gregoriano"""
    equinox = date(year, 3, 21)
    
    # Determinarea primei luni pline după echinocțiu
    a = year % 19
    b = year % 7
    c = year % 4
    d = (19 * a + 15) % 30
    e = (2 * c + 4 * b + 6 * d + 6) % 7
    f = d + e

    if f <= 26:
        day = f + 4
    else:
        day = f - 26

    # Luna plină pe care o dorim
    lunar_full_moon = date(year, 4, day)

    # Paștele ortodox va fi duminica imediat următoare lunii pline
    # Dacă luna plină cade într-o duminică, Paștele va fi în următoarea duminică
    easter_day = lunar_full_moon + timedelta(days=(6 - lunar_full_moon.weekday()))
    
    return easter_day



def generate_orthodox_easter_ics(start_year, end_year, filename="paste_ortodox.ics"):
    """Genera un file .ics con le date della Pasqua ortodossa e altre festività collegate"""
    calendar = ics.Calendar()
    
    for year in range(start_year, end_year + 1):
        easter = orthodox_easter(year)
        
        events = [
            ("Paște Ortodox", easter),
            ("Intrarea Domnului în Ierusalim", easter - timedelta(days=7)),  # 7 giorni prima di Pasqua
            ("Înălțarea Domnului", easter + timedelta(days=40)), # 40 giorni dopo Pasqua
            ("Ziua Sfintei Treimi", easter + timedelta(days=50))  # 50 giorni dopo Pasqua
        ]
        
        for name, date_event in events:
            event = ics.Event()
            event.name = name
            event.begin = date_event.strftime("%Y%m%d")
            event.description = f"Sărbătoare ortodoxă - {name}"
            calendar.events.add(event)
    
    with open(filename, "w") as f:
        f.write(str(calendar))
    
    print(f"File {filename} generato correttamente!")

# Esempio di utilizzo
generate_orthodox_easter_ics(2025, 2050)
