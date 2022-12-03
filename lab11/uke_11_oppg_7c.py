from cmath import pi
import matplotlib.pyplot as plt
from math import sin
from matplotlib.ticker import (MultipleLocator)
#Oppgave 7c

# liste med x-verdier
xs = [n / 10 for n in range(101)]
# 2 ulike lister med y-verdier
ys_1 = [sin(x) for x in xs]
ys_2 = [3 * sin(x) for x in xs]


fig, ax = plt.subplots()

ax.plot(xs, ys_1, ".y") #. og gul
ax.plot(xs, ys_2, "-g") #- grønn

ax.annotate('Første interseksjonen', xy=(pi, 0), xytext=(2, 1), #Tekst,punktlokasjon, tekstlokasjon
             arrowprops=dict(arrowstyle='-' ,facecolor='black'), #pil, piltype(strek), pilfarge
             )

ax.tick_params(which='minor', length=5, width=1.2, color='r') #definerer underticks
ax.xaxis.set_minor_locator(MultipleLocator(0.5)) #plasseres hver 0.5 på xakse
ax.yaxis.set_minor_locator(MultipleLocator(0.25)) #plasseres hver 0.25 på yakse

# savefig lagrer filene
plt.savefig("uke_11_oppg_7c.png")
plt.savefig("test.pdf")

# interaktivt vindu
plt.show() # Hva skjer om vi ikke har med den raden: plt.show()?
