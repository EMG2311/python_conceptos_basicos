import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Problemas_Graficos\\dinero.csv")

#creando grafico de barra
sns.scatterplot(x="tiempo",y="dinero",data=df)



plt.show()