#  Ich lese die ''Cyber''-Wörter (=0) und ''Cyber-''-Wörter (=1).

with open("Cyber.txt", "r") as f:

    str1 = f.read().lower()
    a = "cyber"  # steht für 0
    b = "cyber-"  # steht für 1

    # Gibt mir die Position aller Wörter an, wo 'cyber' vorkommt
    res = [i for i in range(len(str1)) if str1.startswith(a, i)]
    # print(res, "\n")

    # Analog, nur mit 'cyber-'
    res2 = [i for i in range(len(str1)) if str1.startswith(b, i)]
    # print(res2, "\n")

    # Unsere 0en und 1en nacheinander in x hinzugefügt.
    x = ""

    # Ab 8 bits immer Lücke lassen
    counter = 0

    for i in res:
        if counter == 8:
            counter = 0
            x = x + " "

        if i in res2:
            x = x + "1"
            counter += 1
        else:
            x = x + "0"
            counter += 1

    print(x)


def to_ascii(char):
    # int(char, 2): char = "01010111" wird zu 87
    # chr() gibt den Ascii-256 Symbol zurück für Zahlen von 0 bis 255
    return chr(int(char, 2))


def translate(txt):
    result = ""
    letters = txt.split(" ")
    for letter in letters:
        result += to_ascii(letter)
    return result


print("Hier ist das Passwort: " + translate(x))
