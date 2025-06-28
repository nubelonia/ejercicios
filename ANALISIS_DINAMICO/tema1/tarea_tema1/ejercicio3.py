import numpy as np

alumnos = np.array(["Juan", "Noelia", "Pedro", "Marta", "Antonio", "Carlos", "Patricia",
                    "Carmen", "Manuel", "Jorge", "Jose", "Sara", "María", "Rubén", "Bárbara"])

nota_mat = np.array([6.3, 9.1, 7.2 , 4.8, 7.2, 4.4, 5.5, 4.2, 6.9, 3.3, 4.5, 5.6, 5.4, 6.8, 5.1])
nota_len = np.array([7.1, 8.7, 6.5 , 7.5, 5.6, 6.2, 5.4, 4.8 , 8.6, 4.8, 6.4, 5.6, 5.1 , 8.4, 5.0])
nota_fis = np.array([7.4, 9.7, 7.8 , 5.4, 8.4, 3.2, 5.8, 6.4, 7.3, 3.5, 3.4, 5.6, 6.2, 7.1, 5.2])

# 1. Contamos los alumnos aprobados y suspensos en matemáticas
aprobados = np.sum(nota_mat >= 5)   # np.sum cuenta los True
suspensos = np.sum(nota_mat < 5)
print("Aprobados en mates:", aprobados)
print("Suspensos en mates:", suspensos)

# 2. Buscamos el índice de la menor nota en lengua
indice_min_len = np.argmin(nota_len)
print("Peor en lengua:", alumnos[indice_min_len])

# 3. Nombre del alumno con la mejor nota entre matemáticas y lengua
max_mat = np.max(nota_mat)  # Mejor nota en mates
max_len = np.max(nota_len)  # Mejor nota en lengua

if max_mat >= max_len:
    alumno_max = alumnos[np.argmax(nota_mat)]
else:
    alumno_max = alumnos[np.argmax(nota_len)]

print("Mejor nota entre mates/lengua:", alumno_max)

# 4. Indicamos para cada alumno si sacó mejor nota en mates o lengua
asignatura_mejor = np.where(nota_mat > nota_len, "mates", "lengua")
print("Asignatura con mejor nota:", asignatura_mejor)

# 5. Calculamos la media de las tres asignaturas por alumno
medias = (nota_mat + nota_len + nota_fis) / 3
print("Media de las 3 asignaturas:", medias.round(2))  # Redondeamos a 2 decimales
