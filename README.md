# README

## Descriere

Acest proiect permite generarea și combinarea unui calendar care conține atât sărbători cu dată fixă, cât și sărbători care depind de Paștele ortodox.

## Fișiere incluse

- **HolidaysOriginal.ics**: Conține sărbătorile cu dată fixă, care nu se schimbă în fiecare an.
- **generate_Easter.py**: Un algoritm care generează un fișier `.ics` cu datele Paștelui ortodox și ale sărbătorilor asociate pentru următorii ani. Numărul exact de ani generați depinde de parametrii scriptului.
- **merge_calendars.py**: Script care combină sărbătorile din `HolidaysOriginal.ics` cu cele generate de `generate_Easter.py` într-un singur fișier de calendar.
- **Festivitati Moldova.ics**: Fișierul final care conține calendarul complet, inclusiv sărbătorile fixe și cele legate de Paște. Acest fișier poate fi descărcat și utilizat direct de către utilizatori care nu doresc să modifice codul sursă.

## Instrucțiuni de utilizare 

1. Rulează **generate_Easter.py** în terminal pentru a genera fișierul `.ics` cu datele Paștelui și ale sărbătorilor asociate.
   ```sh
   python3 generate_Easter.py
   ```
2. Rulează **merge_calendars.py** pentru a uni sărbătorile fixe cu cele cu dată variabilă.
   ```sh
   python3 merge_calendars.py
   ```
3. Fișierul generat trebuie salvat pe telefon.
4. Deschide fișierul pe telefon și adaugă-l la aplicația de calendar pentru a vedea toate sărbătorile într-un singur loc.

## Observații

- Asigură-te că ai un mediu Python instalat.
- Poți personaliza numărul de ani generați modificând scriptul `generate_Easter.py`.
- Pentru a importa fișierul `.ics` pe iPhone, se recomandă utilizarea iCloud sau a unei aplicații compatibile cu formatul `.ics`.

