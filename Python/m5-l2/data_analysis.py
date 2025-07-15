import pandas as pd

# Cargar los datos
df = pd.read_csv('kodland_data.csv')

# Tarea 1: Encontrar el mínimo número de puntos
min_points = df.points.min()
print(f'Tarea 1 - Mínimo número de puntos: {min_points}')

# Tarea 2: Encontrar el máximo porcentaje de tareas completadas
max_homework = df.homework.max()
print(f'Tarea 2 - Máximo porcentaje de tareas completadas: {max_homework}')

# Tarea 3: Encontrar estudiantes con menos puntos
min_points_students = df[df.points == df.points.min()]
print('\nTarea 3 - Estudiantes con menos puntos:')
print(min_points_students[['id', 'course']])

# Tarea 4: Contar estudiantes sin tareas completadas
no_homework_count = len(df[df.homework == 0])
print(f'\nTarea 4 - Número de estudiantes sin tareas completadas: {no_homework_count}')

# Tarea 5: Suma de puntos de estudiantes en Python Pro
python_pro_points = df[df.course == 'Python Pro'].points.sum()
print(f'\nTarea 5 - Suma total de puntos de estudiantes en Python Pro: {python_pro_points}')