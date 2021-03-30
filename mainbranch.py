import matplotlib.pyplot as plt
Escuelas = []
Hospitales = []
Cemento = 50

for x in range(0, Cemento):
    Escuelas.append(x*0.1)
    Hospitales.append((50-x)*1/25)

print(Escuelas)
print(Hospitales)

plt.plot(Escuelas,Hospitales)
plt.xlabel("Escuelas")
plt.ylabel("Hospitales")
plt.show()