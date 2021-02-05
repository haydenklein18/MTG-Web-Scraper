import pandas as pd
import matplotlib.pyplot as plt


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


data = pd.read_csv("CardData.csv")

data = data.drop(columns=['_id'])

colors = []
wubrg = ["White", "Blue", "Black", "Red", "Green"]
no_white = ["Blue", "Black", "Red", "Green"]
no_blue = ["White", "Black", "Red", "Green"]
no_black = ["White", "Blue", "Red", "Green"]
no_red = ["White", "Blue", "Black", "Green"]
no_green = ["White", "Blue", "Black", "Red"]
abzan = ["White", "Black" "Green"]
mardu = ["White", "Black", "Red"]
sultai = ["Blue", "Black", "Green"]
jeskai = ["White", "Blue", "Red"]
temur = ["Blue", "Red", "Green"]
esper = ["Blue", "Black", "White"]
naya = ["White", "Red", "Green"]
grixis = ["Red", "Black", "Blue"]
bant = ["White", "Blue", "Green"]
jund = ["Black", "Green", "Red"]
simic = ["Blue", "Green"]
rakdos = ["Black", "Red"]
selesnya = ["Green", "White"]
azorious = ["Blue", "White"]
boros = ["White", "Red"]
izzet = ["Red", "Blue"]
dimir = ["Blue", "Black"]
gruul = ["Red", "Green"]
golgari = ["Green", "Black"]
orzhov = ["White", "Black"]

four_colors = [no_green, no_red, no_blue, no_black, no_white]
three_colors = [abzan, jeskai, mardu, temur, sultai, grixis, esper, naya, jund, bant]
two_colors = [azorious, gruul, dimir, golgari, simic, selesnya, izzet, orzhov, boros, rakdos]

for string in data["Mana Cost"]:
    if all(x in string for x in wubrg) and not is_number(string):
        colors.append("All Colors")
        print(string)
    if not any(x in string for x in wubrg):
        colors.append("Colorless")
        print(string)
    for z in four_colors:
        if all(x in string for x in z) and not is_number(string):
            colors.append(" ".join(z))
            print(string)
    for z in three_colors:
        if all(x in string for x in z) and not is_number(string):
            colors.append(" ".join(z))
            print(string)
    for z in two_colors:
        if all(x in string for x in z) and not is_number(string):
            colors.append(" ".join(z))
            print(string)
    # TODO: Triple colors are being used for double colors as well casing more than one to be added
    if not any(x in string for x in no_white) and string != 'false' and not is_number(string):
        colors.append("White")
        print(string)
    if not any(x in string for x in no_blue) and string != 'false' and not is_number(string):
        colors.append("Blue")
        print(string)
    if not any(x in string for x in no_black) and string != 'false' and not is_number(string):
        colors.append("Black")
        print(string)
    if not any(x in string for x in no_green) and string != 'false' and not is_number(string):
        colors.append("Green")
        print(string)
    if not any(x in string for x in no_red) and string != 'false' and not is_number(string):
        colors.append("Red")
        print(string)

print(len(colors))

data["Color"] = colors

print(data["Color"].value_counts())
