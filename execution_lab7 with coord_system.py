from math import ceil
import matplotlib.pyplot as plt

# Начальные данные размещения столов
tables_row_length = 7.2  # 6 столов в ряд
table_width = 0.8  # ширина столов (рядов)
table_distance = 2  # расстояние между рядами
tables_row_sum = 8  # количество рядов столов
edge_x = 20.4
edge_y = 7.2
mid_x = 10.2
mid_y = 3.6

# Координаты предполагаемого расположения точки раздачи
distrib_coords = [(0, 0), (10.2, 0), (10.2, 3.6)]

# Генерация всех координат мест для сидения вдоль осей X и Y
coords_x = [0]
x = 0
c = 0
while x < edge_x:
    if c % 2 == 0:
        x += 0.8
    else:
        x += 2
    x = round(x, 1)
    c += 1
    coords_x.append(x)
coords_y = [0.3]
y = 0.3
while y < (edge_y - 0.3):
    y += 0.6
    y = round(y, 1)
    coords_y.append(y)

# Первая визуализация
plt.figure()
fig, ax = plt.subplots()
ax.set_xlim(0, edge_x)
ax.set_ylim(0, edge_y)
ax.set_aspect('equal')

# Добавление точек раздачи
for coord in distrib_coords:
    ax.plot(coord[0], coord[1], 'ro')  # 'ro' - красные точки

# Добавление координат сидячих мест
for x in coords_x:
    for y in coords_y:
        ax.plot(x, y, 'bo')  # 'bo' - синие точки

plt.xlabel('X координаты')
plt.ylabel('Y координаты')
plt.title('Декартовая система координат')
plt.show()

# Вторая визуализация
plt.figure()
fig, ax = plt.subplots()
ax.set_xlim(0, edge_x)
ax.set_ylim(0, edge_y)
ax.set_aspect('equal')

# Прокладывание пути от точек раздачи к местам для сидения
for coord in distrib_coords:
    ax.plot(coord[0], coord[1], 'ro')  # 'ro' - красные точки

# Добавление координат сидячих мест
for x in coords_x:
    for y in coords_y:
        ax.plot(x, y, 'bo')  # 'bo' - синие точки
for d in distrib_coords:
    for x in coords_x:
        for y in coords_y:
            # Исключение для соседнего ряда
            if d[0] - 1 <= x <= d[0] + 1:
                ax.plot([d[0], x], [d[1], y], 'g--', linewidth=0.5)  # Прямая линия к соседнему ряду
            else:
                if y > 0.3:
                    ax.plot([d[0], d[0]], [d[1], 0.3], 'g--', linewidth=0.5)  # Вертикальная линия до y = 0.3
                    ax.plot([d[0], x], [0.3, 0.3], 'g--', linewidth=0.5)  # Горизонтальная линия на y = 0.3
                    ax.plot([x, x], [0.3, y], 'g--', linewidth=0.5)  # Вертикальная линия до места назначения

plt.xlabel('X координаты')
plt.ylabel('Y координаты')
plt.title(f'Путь от точки раздачи к местам для сидения ')
plt.show()

#   Высчитываем расстояние по осям X и Y от точки раздачи до сидячего места
distance_sum_list = []
for d in range(len(distrib_coords)):
    distance_sum = 0
    for x in coords_x:
        for y in coords_y:
            distance_x = abs(x - distrib_coords[d][0])
            distance_y = abs(y - distrib_coords[d][1])
            distance_sum += (distance_x + distance_y)
            distance_sum = round(distance_sum)
    distance_sum_list.append([distance_sum, distrib_coords[d]])
print(distance_sum_list)

#   Оптимальное место точки раздачи
distrib_coords = min(distance_sum_list)[1]
distance_sum = min(distance_sum_list)[0]
print(distance_sum, distrib_coords)

#   Матрица измерений
matrix = [["Координаты места", "Расстояние от точки раздачи до сидячего места"],]
for x in coords_x:
    for y in coords_y:
        distance_sum = 0
        distance_x = abs(x - distrib_coords[0])
        distance_y = abs(y - distrib_coords[1])
        distance_sum += (distance_x + distance_y)
        distance_sum = round(distance_sum, 2)
        matrix.append([(x, y), distance_sum])
print("\n>>>>>Матрица расстояний<<<<<", *matrix, sep="\n")

#   Матрица расстояний

dist_matrix = [[""],]
for i in range(1, len(matrix)):
    dist_matrix[0].append(matrix[i][0])
    dist_matrix.append([matrix[i][0]])

for i1 in range(1, len(matrix)):
    for i2 in range(1, len(matrix)):
        arg1 = matrix[i1][1]
        arg2 = matrix[i2][1]
        dist = abs(arg1-arg2)
        dist = round(dist, 2)
        dist_matrix[i2].append(dist)

print("\n>>>>>Матрица расстояний<<<<<", *dist_matrix, sep="\n")

#   Матрица остовного дерева

tree_matrix = [[""],]
for i in range(1, len(matrix)):
    tree_matrix[0].append(matrix[i][0])
    tree_matrix.append([matrix[i][0]])

for i1 in range(1, len(dist_matrix)):
    for i2 in range(1, len(dist_matrix)):
        tree_matrix[i2].append(0)

for i1 in range(1, len(dist_matrix)):
    i1_list = []
    for i2 in range(1, len(dist_matrix)):
        arg = dist_matrix[i1][i2]
        if i1 != i2 and arg != 0:
            i1_list.append(arg)
    min_arg = min(i1_list)
    indexes = [i for i, value in enumerate(dist_matrix[i1]) if value == min_arg]
    for index in indexes:
        tree_matrix[i1][index] = min_arg
        tree_matrix[index][i1] = min_arg
print("\n>>>>>Матрица остовного дерева<<<<<", *tree_matrix, sep="\n")


#   Результат кластерного анализа
print("\n>>>>>Результат кластерного анализа<<<<<")
value_list = []
for i1 in range(1, len(tree_matrix)):
    for i2 in range(i1, len(tree_matrix)):
        if tree_matrix[i1][i2] != 0:
            value_list.append([tree_matrix[i1][i2], i1, i2])
value_list.sort()

c = 1
coords = [tree_matrix[0][x] for x in range(1, len(tree_matrix[0]))]

for j in range(len(value_list)):
    cluster = []
    i1 = value_list[j][1]
    i2 = value_list[j][2]
    if tree_matrix[i1][0] in coords:
        coord1 = tree_matrix[i1][0]
        cluster.append(coord1)
        coords.remove(coord1)

    if tree_matrix[0][i2] in coords:
        coord2 = tree_matrix[0][i2]
        cluster.append(coord2)
        coords.remove(coord2)

    if cluster != []:
        print(f"Состав {c}-го кластера: ", cluster)
        c += 1


# Определение количества смен, необходимых на потребление пищи всеми обучающимися
number_of_students = (4 * 9 + 2 * 2) * 25 # количество учеников в школе
NOS_per_row = 25 # количество учеников на одном ряду столов
NOS_in_dining_room = NOS_per_row * 8 # максимальное количество учеников в столовой
meal_time = 20 # время на обеденный перерыв для класса
break_time = 40 # время перерыва
number_of_shifts = ceil((number_of_students//NOS_in_dining_room)
                        /(break_time//meal_time)) # количество смен на потребление пищи всеми обучающимися
print("Количество смен:", number_of_shifts)
