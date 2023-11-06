import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Problemas_Graficos\\ingresos.csv")

#creando grafico de barra
sns.barplot(x="fuente",y="ingreso",data=df)

#obteniendo el total de ingresos
total_ingresos=df["ingreso"].sum()

#mostrando el total de ingresos
print(f"El total de ingresos es de: ${total_ingresos}")
plt.show()