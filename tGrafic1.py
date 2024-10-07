import matplotlib.pyplot as plt
#Grafico de barras
plt.title("Animes mejor puntuados")
#
animes = ["Kimetsu no\n Yaiba","Fruits Basket","Mo Dao \nZu Shi 3","FullMetal \nAlchemist","Shingeki no \nKyojin S3-P2"]
coloracion = ["black","red","blue","silver","brown"]
puntuacion = [4.6,4.6,4.58,4.57,4.56]
plt.bar(animes,puntuacion,color=coloracion)
plt.xlabel("Animes")
plt.ylabel("Puntuacion 0-5")
plt.show()