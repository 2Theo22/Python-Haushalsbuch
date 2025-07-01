from storage import loaddata, savedata
from tracker import transaktion, transshow, export_csv
data = loaddata()


while True:
    print("1. Transaktion hinzufügen\n2. Transaktionen anzeigen\n3. Zu CSV konvertieren\n4. Beenden")
    x = int(input("Eingabe: "))

    if x == 1:
        transaktion(data)
    elif x == 2:
        transshow(data)

    elif x == 3:
        export_csv(data)
    else:
        savedata(data)
        quit()





