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
abzan = ["White", "Black", "Green"]
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
    isall = False
    isnone = False
    is4 = False
    is3 = False
    is2 = False
    is1 = False
    isOther = False
    mana_cost = str.split(string)

    if all(item in mana_cost for item in wubrg):
        colors.append("All Colors")
        isall = True
    if not any(item in mana_cost for item in wubrg) and isall is False and "false" in mana_cost or len(mana_cost) == 1 and is_number(mana_cost[0]):
        colors.append("Colorless")
        isnone = True
    for nephilim in four_colors:
        if all(item in mana_cost for item in nephilim) and isall is False and isnone is False:
            colors.append(" ".join(nephilim))
            is4 = True
    for shardOrClan in three_colors:
        if all(item in mana_cost for item in shardOrClan) and isall is False and isnone is False and is4 is False:
            colors.append(" ".join(shardOrClan))
            is3 = True
    for guild in two_colors:
        if all(item in mana_cost for item in
               guild) and isall is False and isnone is False and is4 is False and is3 is False:
            colors.append(" ".join(guild))
            is2 = True
    if "White" in mana_cost and isall is False and isnone is False and is4 is False and is3 is False and is2 is False and is1 is False:
        colors.append("White")
        is1 = True
    if "Blue" in mana_cost and isall is False and isnone is False and is4 is False and is3 is False and is2 is False and is1 is False:
        colors.append("Blue")
        is1 = True
    if "Black" in mana_cost and isall is False and isnone is False and is4 is False and is3 is False and is2 is False and is1 is False:
        colors.append("Black")
        is1 = True
    if "Red" in mana_cost and isall is False and isnone is False and is4 is False and is3 is False and is2 is False and is1 is False:
        colors.append("Red")
        is1 = True
    if "Green" in mana_cost and isall is False and isnone is False and is4 is False and is3 is False and is2 is False and is1 is False:
        colors.append("Green")
        is1 = True
    if isall is False and isnone is False and is4 is False and is3 is False and is2 is False and is1 is False:
        isOthers = True
        colors.append("Other")
        print(mana_cost)

data["Color"] = colors

counts = data["Color"].value_counts()

barlist = plt.barh(counts.index, counts.tolist())
plt.show()
