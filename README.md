# Sărbători Moldova - Calendar .ICS 📅

Acest proiect îți permite să adaugi cu ușurință sărbătorile din Moldova (naționale și religioase) în calendarul tău digital, inclusiv sărbătorile schimbătoare bazate pe Paștele ortodox. Fișierul generat este compatibil cu aplicații populare precum Google Calendar, Apple Calendar și Outlook.

## Fișiere incluse în acest proiect 📂:

- **Festivitati Moldova.ics** – Fișierul final cu toate sărbătorile importante din Moldova, incluzând sărbătorile cu dată fixă și sărbătorile bazate pe Paștele ortodox.
- **HolidaysOriginal.ics** – Fișierul care conține doar sărbătorile cu dată fixă.
- **generate_Easter.py** – Script Python care calculează și generează datele sărbătorilor schimbătoare, legate de Paștele ortodox.
- **merge_calendars.py** – Script care combină sărbătorile din fișierele anterioare într-un singur fișier ICS pentru a-l importa rapid în calendarul tău.

---

## Cum să adaugi sărbătorile din Moldova în Google Calendar, Apple Calendar sau Outlook? 🗓️

### Partea 1: Pentru utilizatorii finali (adăugare rapidă în calendar) 🏃‍♂️

Dacă dorești doar să adaugi sărbătorile din Moldova direct în calendarul tău, urmează acești pași simpli:

1️⃣ **Descarcă fișierul Festivitati Moldova.ics**:
   - [Descarcă Festivitati Moldova.ics]([Descarcă Festivități Moldova.ics](https://github.com/storm167/Sarbatori_Moldova/raw/main/Festivități%20Moldova.ics)
)

2️⃣ **Importă fișierul în aplicația ta de calendar**:

   **Google Calendar 📅**:
   - Accesează [Google Calendar](https://calendar.google.com)
   - Mergi la „Setări” → „Import & Export”
   - Selectează fișierul Festivitati Moldova.ics și importă-l.

   **Apple Calendar (iPhone 🍎)**:
   - Trimite fișierul .ics pe iPhone prin e-mail sau AirDrop.
   - Apasă pe fișier și selectează „Adaugă în Calendar”.

   **Outlook Calendar 📧**:
   - Deschide Outlook și navighează la calendar.
   - Selectează „Importă” și alege fișierul Festivitati Moldova.ics.

### Partea 2: Pentru dezvoltatori (vizualizează și modifică codul sursă 💻)

Dacă ești un dezvoltator și dorești să explorezi sau să modifici codul sursă, urmează acești pași:

1️⃣ **Generează sărbătorile mobile 📆**:
   - În terminal, rulează următorul cod Python pentru a calcula sărbătorile bazate pe Paștele ortodox:
     ```bash
     python3 generate_easter.py
     ```

2️⃣ **Combină toate sărbătorile într-un singur fișier 🔗**:
   - Rulează scriptul pentru a crea fișierul ICS complet cu toate sărbătorile:
     ```bash
     python3 merge_calendars.py
     ```

3️⃣ **Importă fișierul generat 📥**:
   - Fișierul final „Festivitati Moldova.ics” poate fi acum importat în calendarul tău digital.

### Observații importante ⚠️:

- Este necesar să ai Python 3 instalat pe sistemul tău.
- Dacă vrei să modifici numărul de ani pentru care generezi sărbătorile, editează fișierul `generate_Easter.py`.
- Dacă întâmpini probleme sau ai întrebări, deschide un „Issue” pe [GitHub](https://github.com/storm167/Sarbatori_Moldova/issues).

### Contribuie la proiect 🙌:

Vrei să adaugi noi sărbători sau să îmbunătățești proiectul? Poți contribui pe GitHub și să împărtășești sugestiile tale cu comunitatea!

---

## Căutări populare 🔍:

- Calendar Moldova 2025 📅
- Sărbători religioase Moldova ☦️
- Paște ortodox Moldova 🕊️
- Adaugă sărbători în Google Calendar 📲
- Calendar național Moldova ICS 🗓️
