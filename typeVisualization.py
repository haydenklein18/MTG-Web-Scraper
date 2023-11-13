import pandas as pd
import matplotlib.pyplot as plt


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


data = pd.read_csv("CardData.csv")

counts = data["Card Type"].value_counts()

print(counts.index)

# barlist = plt.barh(counts.index.sort_values(), counts.tolist())
# plt.show()