import zipfile

# Das ist für eine schöne Anzeige, wie viel Prozent ich noch durchgehen muss von der Datei
from tqdm import tqdm

wordlist = "rockyou.txt"
zip_file = "geschenk.zip"


zip_file = zipfile.ZipFile(zip_file)
n_words = len(list(open(wordlist, "rb")))

print("Total passwords to test:", n_words)

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        # Falls das Passwort falsch ist, wird ein Fehler aufgerufen, deswegen try
        try:
            # Tipp war: Passwort ist 96 lang, man könnte aber einfach alle Passwörter durchgehen.
            if len(word.strip()) == 96:
                zip_file.extractall(pwd=word.strip())
            else:
                continue
        except:
            continue
        # Wird ausgeführt, falls er ohne Probleme durch try durchkommt, wenn er also das Passwort gefunden hat!
        else:
            # decode für b-string zu normalem string.
            print("[!] Password found:", word.decode().strip())
            # 0 steht für success, 1 bis 255 steht für failurein exit().
            exit(0)
print("[!] Password not found, try other wordlist.")
