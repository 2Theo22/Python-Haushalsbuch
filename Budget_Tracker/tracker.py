import time
import datetime
from datetime import date, datetime
from storage import loaddata
import csv

def transaktion(data):
    Betrag = float(input("Betrag: "))
    Kategorie = str(input("Kategorie: "))
    Beschreibung = str(input("Beschreibung: "))
    Datum = str(date.today())
    Uhrzeit = str(datetime.now().strftime("%H:%M:%S"))

    data.append({
        "Betrag": Betrag,
        "Kategorie": Kategorie,
        "Beschreibung": Beschreibung,
        "Datum": Datum,
        "Uhrzeit": Uhrzeit
    })

def transshow(data):
    if not data:
        print("Keine Transaktionen vorhanden.")
        return
    print("Datum       | Betrag   | Kategorie | Beschreibung     | Uhrzeit")
    print("-" * 75)
    for trans in data:
        datum = trans["Datum"]
        betrag = f"{trans['Betrag']:>8.2f}€"
        kategorie = trans["Kategorie"].ljust(14)
        beschreibung = trans["Beschreibung"].ljust(20)
        uhrzeit = trans["Uhrzeit"]

        print(f"{datum} | {betrag} | {kategorie} | {beschreibung} | {uhrzeit}")



def export_csv(data):
    with open('haushalt.csv', mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames = ["Betrag", "Kategorie", "Beschreibung", "Datum", "Uhrzeit"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)




