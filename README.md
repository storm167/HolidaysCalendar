# 📅 Sarbatori Moldova - Calendar .ICS

## 📝 Descriere

Acest proiect generează și combină un calendar `.ICS` care conține:
✅ **Sărbători naționale și religioase cu dată fixă**
✅ **Sărbători schimbătoare bazate pe Paștele ortodox**

Fișierul final rezultat poate fi importat direct în aplicațiile de calendar (Google Calendar, Apple Calendar, Outlook etc.).

## 📂 Fișiere incluse

- **HolidaysOriginal.ics** – conține sărbătorile cu dată fixă.
- **generate_Easter.py** – script Python care generează datele sărbătorilor schimbătoare bazate pe Paștele ortodox.
- **merge_calendars.py** – combină sărbătorile din `HolidaysOriginal.ics` cu cele din `generate_Easter.py`.
- **Festivitati Moldova.ics** – 📌 **fișierul final** care trebuie descărcat de utilizatorii care nu vor să modifice codul sursă.

## 🚀 Cum se folosește

1️⃣ **Generează sărbătorile mobile**:
```sh
python3 generate_easter.py
```
2️⃣ **Combină toate sărbătorile într-un singur fișier**:
```sh
python3 merge_calendars.py
```
3️⃣ **Importă fișierul final în calendar**:
   - Descarcă **Festivitati Moldova.ics**
   - Deschide-l pe telefon sau PC și adaugă-l în aplicația de calendar.

## 📌 Import în Google Calendar / Apple Calendar

📱 **Google Calendar:**
1. Accesează [calendar.google.com](https://calendar.google.com)
2. Mergi la „Setări” → „Import & Export”
3. Alege fișierul `Festivitati Moldova.ics` și importă-l

📱 **iPhone (Apple Calendar):**
1. Trimite fișierul `.ics` pe iPhone prin e-mail/AirDrop
2. Apasă pe fișier și selectează „Adaugă în Calendar”

## ℹ️ Observații

- Necesită **Python 3** instalat.
- Poți modifica numărul de ani generați editând `generate_Easter.py`.
- Dacă ai întrebări, deschide un „Issue” pe GitHub! 😊

---

🌍 **Contribuie:** Dacă ai sugestii sau vrei să adaugi alte sărbători, contribuie la proiect! 💡

