import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial import ConvexHull

# Шаг 1: Параметры
num_tables = 8  # Количество столов
table_length = 7.2  # Длина стола (м)
table_width = 0.8  # Ширина стола (м)
distance_between_tables = 2  # Расстояние между столами (м)
people_per_class = 25  # Количество человек в одном классе
num_classes = 4 + 2  # Количество классов (1-9 классы и 10-11 классы)

# Шаг 2: Расположение столов (гипотетическое расположение)
# Столы разместим в виде прямоугольной сетки
table_positions = []
rows = 3  # 3 ряда столов (8 столов)
cols = 3  # 3 столбца

# Учитываем размеры стола и расстояния между ними
for i in range(rows):
    for j in range(cols):
        if len(table_positions) < num_tables:
            x = j * (table_length + distance_between_tables)
            y = i * (table_width + distance_between_tables)
            table_positions.append([x, y])

table_positions = np.array(table_positions)

# Шаг 3: Распределение точек раздачи еды
# Мы разместим кастрюли, разнос и напитки в стратегически удобных местах
distribution_points = [
    [0, 0],  # Кастрюля с супом
    [10, 0],  # Разнос с вторым блюдом
    [20, 0]   # Разнос с напитками
]

# Кластеризация с использованием K-means
kmeans = KMeans(n_clusters=3, random_state=0).fit(table_positions)

# Получаем центры кластеров
cluster_centers = kmeans.cluster_centers_

# Шаг 4: Построение выпуклой оболочки (Convex Hull)
hull = ConvexHull(table_positions)

# Шаг 5: Визуализация
plt.figure(figsize=(10, 8))

# Столы
plt.scatter(table_positions[:, 0], table_positions[:, 1], c='blue', label='Столы')
for pos in table_positions:
    plt.text(pos[0], pos[1], f'({pos[0]:.1f}, {pos[1]:.1f})')

# Кластеры
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', marker='x', s=200, label='Центры кластеров')

# Раздача еды
for point in distribution_points:
    plt.scatter(point[0], point[1], c='green', marker='o', s=100, label='Точка раздачи')

# Выпуклая оболочка
for simplex in hull.simplices:
    plt.plot(table_positions[simplex, 0], table_positions[simplex, 1], 'k-')

# Настройки графика
plt.title('Оптимизация расстановки столов и точек раздачи пищи')
plt.xlabel('X (метры)')
plt.ylabel('Y (метры)')
plt.legend()
plt.grid(True)
plt.show()

