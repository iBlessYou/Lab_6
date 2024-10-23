import matplotlib.pyplot as plt

# Исходные данные размещения столов
table_length = 7.2
table_width = 0.8
table_distance = 2
table_sum = 8
edge_x = 20.4
edge_y = 7.2
mid_x = 10.2
mid_y = 3.6

# Перечень координат предполагаемого расположения точки раздачи
distrib_coords = [(0, 0), (0, 3.6), (10.2, 0), (10.2, 3.6)]

# Перебор всех координат сидячих мест по оси X
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

# Перебор всех координат сидячих мест по оси Y
coords_y = [0.3]
y = 0.3
while y < (edge_y - 0.3):
    y += 0.6
    y = round(y, 1)
    coords_y.append(y)

# Создание декартовой системы координат
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
