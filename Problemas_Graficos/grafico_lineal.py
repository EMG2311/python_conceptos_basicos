import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Problemas_Graficos\\pedos.csv")

sns.lineplot(x="fecha",y="pedos",data=df)

#creando un punto en a cordenada (01-02 y 20). La o es el punto
plt.plot("01-09",20,"o")

plt.show()