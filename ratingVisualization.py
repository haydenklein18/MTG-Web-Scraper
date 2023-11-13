import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

ratings = [0,1, 2, 3, 4, 5]

zeros = []

ones = []

twos = []

threes = []

fours = []

fives = []

data = pd.read_csv("CardData.csv")

data = data.drop(columns=['_id'])

data = data.loc[(data != 0).any(axis=1)]

numbers = data["Community Rating"]

sorted_data = sorted(numbers)

for x in sorted_data:

    rounded = round(x)
    if rounded == 0:
        zeros.append(1)
    elif rounded == 1:
        ones.append(1)
    elif rounded == 2:
        twos.append(1)
    elif rounded == 3:
        threes.append(1)
    elif rounded == 4:
        fours.append(1)
    elif rounded == 5:
        fives.append(1)

zeros = sum(zeros)
ones = sum(ones)
twos = sum(twos)
threes = sum(threes)
fours = sum(fours)
fives = sum(fives)

totals = [zeros,ones,twos,threes,fours,fives]

plt.xticks(rotation=90)
plt.xticks(fontsize=5)

plt.bar(ratings,totals)

figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

plt.show()


