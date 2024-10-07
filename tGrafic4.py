import matplotlib.pyplot as plt

#Grafico de pastel

#Años juntos con su respectiva cantidad y porcentaje
x = ["2018\n91.84k(21.8%)",
     "2019\n86.52k(20.6%)",
     "2020\n84.08k(19.9%)",
     "2021\n81.16k(19.3%)","2022\n77.07k(17.32%)"]
y = [21.8,20.6,19.9,19.3,17.32]
plt.title("Nacimientos en Japon del 2018 al 2022(en miles 'k')\nTotal: 420.67k")
plt.pie(y,labels=x)
plt.show()