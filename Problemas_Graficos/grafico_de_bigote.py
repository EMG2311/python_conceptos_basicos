import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Problemas_Graficos\\grafico_de_bigote.csv")

#creando grafico de barra
sns.boxplot(x="categoria",y="valor",data=df)


plt.show()