import pandas as pd
import matplotlib.pyplot as plt


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


data = pd.read_csv("CardData.csv")
data = data[data["Converted Mana Cost"] >= 0]

counts = data["Converted Mana Cost"].value_counts()

barlist = plt.barh(counts.index.sort_values(), counts.tolist())
plt.show()