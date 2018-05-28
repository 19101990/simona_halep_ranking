import datetime as dt
import matplotlib.pyplot as plt
import csv

plt.style.use('seaborn-darkgrid')

str_date = []
date = []
singles = []


# reads from file
with open('simo_ranking.txt', 'r') as csvfile:
    file = list(csv.reader(csvfile, delimiter='\t'))

# appends values to str_date and singles
for row in file[:250]:
    str_date.append(row[0])
    singles.append(int(row[1]))
    
# converts string to date
for i in str_date:
    d = dt.datetime.strptime(i, "%m-%d-%Y")
    date.append(d)

# locates index of the first occurence of '1' in singles
rev_singles = singles[::-1]
no_1 = rev_singles.index(1)
no_1_index = len(singles) - no_1 - 1


plt.plot(date,singles, label='Ranking', color="#000000", linewidth=1.0,
         zorder=1)
plt.scatter(date[no_1_index], singles[no_1_index],
            color='#fdbf00', marker="*", s=100, label="World's No. 1!",
            zorder=10)

plt.xlabel('Y E A R', color="#d7d7d7", size=12)
plt.ylabel('R A N K I N G', color="#d7d7d7", size=12)
plt.title('S I M O N A   H A L E P\n', size=16, color='#d3d3d3')
plt.ylim(max(singles), min(singles))
plt.axis('auto')

plt.legend()
plt.show()
