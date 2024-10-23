import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
import numpy as np

data = [["Фамилия", "Возраст", "Заработок", "Кредитная история", "Семейное положение", "Образование"],
     ["Иванов", 23, 15000, "Нет", "Женат", "Высшее"],
     ["Петров", 50, 40000, "Есть", "Женат", "Высшее"],
     ["Сидоров", 34, 16000, "Есть", "Холост", "Среднее"],
     ["Федоров", 29, 20000, "Нет", "Холост", "Среднее"],
     ["Яковлев", 42, 18000, "Есть", "Холост", "Уч. степень"]]
print(">>>>>Матрица измерений<<<<<", *data, sep="\n")
while True:
    #   Матрица расстояний
    parameter = input("Введите параметр: ")
    if parameter in data[0]:
        j = data[0].index(parameter)
        dist_matrix = [["", "Иванов", "Петров", "Сидоров", "Федоров", "Яковлев"],
                                ["Иванов", 0, "", "", "", ""],
                                ["Петров", "", 0, "", "", ""],
                                ["Сидоров", "", "", 0, "", ""],
                                ["Федоров", "", "", "", 0, ""],
                                ["Яковлев", "", "", "", "", 0]]
        for i1 in range(1, len(data)):
            for i2 in range(1, len(data)):
                arg1 = data[i1][j]
                arg2 = data[i2][j]
                try:
                    arg1 = float(arg1)
                    arg2 = float(arg2)
                    dist = abs(arg1-arg2)
                    dist_matrix[i1][i2] = int(dist)
                except Exception:
                    if arg1 == arg2:
                        dist_matrix[i1][i2] = 0
                    else:
                        dist_matrix[i1][i2] = 1
        print("\n>>>>>Матрица расстояний<<<<<", *dist_matrix, sep="\n")

        # Преобразуем матрицу расстояний в numpy массив
        distances = np.array([[dist_matrix[i][j] for j in range(1, len(data))] for i in range(1, len(data))])

        #   Создаем дендрограмму
        plt.figure(figsize=(10, 7))
        dendrogram = sch.dendrogram(sch.linkage(distances, method='single'), labels=[row[0] for row in data[1:]])
        plt.title('Дендрограмма результатов иерархической кластеризации')
        plt.xlabel('Фамилии')
        plt.ylabel('Расстояние')
        plt.show()

        #   Матрица остовного дерева
        tree_matrix = [["", "Иванов", "Петров", "Сидоров", "Федоров", "Яковлев"],
                                ["Иванов", 0, 0, 0, 0, 0],
                                ["Петров", 0, 0, 0, 0, 0],
                                ["Сидоров", 0, 0, 0, 0, 0],
                                ["Федоров", 0, 0, 0, 0, 0],
                                ["Яковлев", 0, 0, 0, 0, 0]]
        for i1 in range(1, len(data)):
            i1_list = []
            for i2 in range(1, len(data)):
                arg = dist_matrix[i1][i2]
                if i1 != i2:
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
        for i1 in range(1, len(data)):
            for i2 in range(i1, len(data)):
                if tree_matrix[i1][i2] != 0:
                    value_list.append([tree_matrix[i1][i2], i1, i2])
        value_list.sort()

        c = 1
        surnames = [tree_matrix[0][x] for x in range(1, len(tree_matrix[0]))]

        for j in range(len(value_list)):
            cluster = []
            i1 = value_list[j][1]
            i2 = value_list[j][2]
            if tree_matrix[i1][0] in surnames:
                surname1 = tree_matrix[i1][0]
                cluster.append(surname1)
                surnames.remove(surname1)

            if tree_matrix[0][i2] in surnames:
                surname2 = tree_matrix[0][i2]
                cluster.append(surname2)
                surnames.remove(surname2)

            print(f"Состав {c}-го кластера: ", cluster)
            c += 1

# После завершения кластерного анализа добавьте следующий код:


