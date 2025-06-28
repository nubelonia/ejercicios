import numpy as np
import matplotlib.pyplot as plt

alumnos = np.array(["Juan", "Noelia", "Pedro", "Marta", "Antonio", "Carlos", "Patricia",
                    "Carmen", "Manuel", "Jorge", "Jose", "Sara", "María", "Rubén", "Bárbara"])

nota_mat = np.array([6.3, 9.1, 7.2 , 4.8, 7.2, 4.4, 5.5, 4.2, 6.9, 3.3, 4.5, 5.6, 5.4, 6.8, 5.1])
nota_len = np.array([7.1, 8.7, 6.5 , 7.5, 5.6, 6.2, 5.4, 4.8 , 8.6, 4.8, 6.4, 5.6, 5.1 , 8.4, 5.0])
nota_fis = np.array([7.4, 9.7, 7.8 , 5.4, 8.4, 3.2, 5.8, 6.4, 7.3, 3.5, 3.4, 5.6, 6.2, 7.1, 5.2])

# Media de cada alumno
medias = (nota_mat + nota_len + nota_fis) / 3

# Crear figura con dimensiones que eviten solapamientos
plt.figure(figsize=(8, 8))  # Altura

# 1. Histograma de notas medias (color azul)
plt.subplot(2, 2, 1)
plt.hist(medias, color='blue')
plt.title("Histograma Notas Medias")
plt.xlabel("Nota media", color='blue')
plt.ylabel("Frecuencia")

# 2. Scatter: Matemáticas vs Lengua (color rojo)
plt.subplot(2, 2, 2)
plt.scatter(nota_mat, nota_len, color='red')
plt.title("Mates vs Lengua")
plt.xlabel("Matemáticas", color='red')
plt.ylabel("Lengua", color='red')

# 3. Scatter: Matemáticas vs Física (color naranja)
plt.subplot(2, 2, 3)
plt.scatter(nota_mat, nota_fis, color='orange')
plt.title("Mates vs Física")
plt.xlabel("Matemáticas", color='orange')
plt.ylabel("Física", color='orange')

# 4. Scatter: Física vs Lengua (color verde)
plt.subplot(2, 2, 4)
plt.scatter(nota_fis, nota_len, color='green')
plt.title("Física vs Lengua")
plt.xlabel("Física", color='green')
plt.ylabel("Lengua", color='green')

# Ajustar márgenes entre filas y columnas
plt.tight_layout()
plt.show()