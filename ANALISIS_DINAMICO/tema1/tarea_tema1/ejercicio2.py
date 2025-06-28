import numpy as np

# Arrays con los datos
alumnos = np.array(["Juan", "Noelia", "Pedro", "Marta", "Antonio", "Carlos", "Patricia",
                    "Carmen", "Manuel", "Jorge", "Jose", "Sara", "María", "Rubén", "Bárbara"])
nota_len = np.array([7.1, 8.7, 6.5 , 7.5, 5.6, 6.2, 5.4, 4.8 , 8.6, 4.8, 6.4, 5.6, 5.1 , 8.4, 5.0])
nota_mat = np.array([6.3, 9.1, 7.2 , 4.8, 7.2, 4.4, 5.5, 4.2, 6.9, 3.3, 4.5, 5.6, 5.4, 6.8, 5.1])

# 1. Alumnos que han suspendido matemáticas (nota < 5)
print("Suspendidos en mates:", alumnos[nota_mat < 5])

# 2. Alumnos que sacaron nota superior a la media en matemáticas
media_mates = np.mean(nota_mat)  # Calculamos la media
print("Notas superiores a la media en mates:", alumnos[nota_mat > media_mates])

# 3. Alumnos con mejor nota en matemáticas que en lengua
print("Mates > Lengua:", alumnos[nota_mat > nota_len])

# 4. Alumnos que han suspendido tanto matemáticas como lengua
cond = (nota_mat < 5) & (nota_len < 5)  # Condición compuesta
print("Suspendidos en mates y lengua:", alumnos[cond])
