# Idee: Zip entpacken & alte Zip löschen, diese Prozedur jetzt wiederholen mittels while-Schleife. Nach einem Durchgang sollten
# wir also wie in der Ausgansposition sein, damit wir den gleichen Code immer wieder benutzen können.

import zipfile
import os

while True:

    # fmt: off
    x = zipfile.ZipFile("geschenk.zip")
    # fmt: on

    # Falls die Datei im Zip nicht auf .zip endet, dann beende meine Schleife.
    if not x.namelist()[0].endswith(".zip"):
        break

    # iterate through each file
    for y in x.infolist():
        # This will do the renaming
        y.filename = "a.zip"
        x.extract(y)

    os.remove("geschenk.zip")

    os.rename(
        "a.zip",
        "geschenk.zip",
    )

# Und noch ein letztes Mal unzippen, da wir die Schleife abgebrochen hatten:

# fmt: off
x = zipfile.ZipFile("geschenk.zip")
# fmt: on

x.extractall()

os.remove("geschenk.zip")
