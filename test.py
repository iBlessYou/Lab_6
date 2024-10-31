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
