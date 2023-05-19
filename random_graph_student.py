import pprint, random
import networkx as nx
import matplotlib.pyplot as plt
# import draw


class RandomGraph:
    """Неориентированный случайный граф
    - вершинно и (или) реберно-взвешенный
    - гарантированно связный"""

    @classmethod
    def __check(cls, n, mean_degree, min_edge_weight, max_edge_weight,
                 min_node_weight, max_node_weight):
        """
        Проверка корректности входных параметров.
        Метод класса (определен на уровне класса).
        Приватный метод (нельзя получить к нему доступ извне класса).
        :param n: количество вершин графа
        :param mean_degree: средняя степень вершины
        :param min_edge_weight: минимальный вес ребра
        :param max_edge_weight: максимальный вес ребра
        :param min_node_weight: минимальный вес вершины
        :param max_node_weight: максимальный вес вершины
        :return: Bool
        """
        pass
        return True

    def __init__(self, n, mean_degree,
                 min_edge_weight=1, max_edge_weight=1,
                 min_node_weight=1, max_node_weight=1):
        """
        :param n: количество вершин графа
        :param mean_degree: средняя степень вершины
        :param min_edge_weight: минимальный вес ребра (по умолчанию 1)
        :param max_edge_weight: максимальный вес ребра (по умолчанию 1)
        :param min_node_weight: минимальный вес вершины (по умолчанию 1)
        :param max_node_weight: максимальный вес вершины (по умолчанию 1)
        """
        # проверка корректности заданных значений
        self.__check(n, mean_degree, min_edge_weight, max_edge_weight,
                 min_node_weight, max_node_weight)

        if mean_degree > n - 1:
            self.mean_degree_initial = n - 1        # проверка на полный граф
            self.mean_degree = n - 1
        else:
            self.mean_degree_initial = mean_degree  # заданное пользователем значение

        if mean_degree < 2 * (n - 1) / n:       # если средняя степень меньше минимально возможной для дерева
            self.mean_degree = 2 * (n - 1) / n  # будет сгенерировано дерево
        else:
            self.mean_degree = mean_degree

        self.n = n                                # число вершин
        self.min_edge_weight = min_edge_weight    # минимальный вес ребра
        self.max_edge_weight = max_edge_weight    # максимальный вес ребра
        self.min_node_weight = min_node_weight    # минимальный вес вершины
        self.max_node_weight = max_node_weight    # максимальный вес вершины
        self.num_of_edges = int(self.mean_degree * self.n / 2)   # число ребер графа
        self.W = list()         # матрица весов
        self.A = list()         # матрица смежности
        self.Al = list()        # список смежности (список соседей)
        self.B = list()         # матрица инциденций
        self.R = list()         # матрица достижимостей
        self.D = list()         # матрица кратчайших расстояний
        self.V = list()         # матрицв весов вершин
        self.E = list()         # список ребер (вес, начало, конец)
        self.degrees = list()   # список степеней вершин графа
        self.dead_ends = list() # список висячих вершин
        self.density = 0        # плотность графа
        self.diameter = 0       # диаметр графа
        self.is_connected = True    # граф связный
        self.isolated_nodes = list() # список изолированных вершин

        self.w_generation()     # генерация случайной матрицы W
        self.v_generation()     # генерация случайной матрицы V

    def w_generation(self):
        """Генерация матрицы весов W"""
        self.W = list()
        # заполняем матрицу W '-' и 0
        for i in range(self.n):
            self.W.append(['-'] * self.n)
            self.W[i][i] = 0  # главная диагональ 0
        # генерируем остовное дерево
        stack = []  # стек вершин
        for i in range(self.n):
            stack.append(i)
        random.shuffle(stack)  # перемешиваем вершины в стеке
        while stack:           # пока есть стек
            first = stack.pop()  # выдергиваем вершину из стека
            if stack:
                second = random.choice(stack)  # вторая вершина случайная из стека
                self.W[first][second] = self.W[second][first] = \
                    random.randint(self.min_edge_weight,
                                   self.max_edge_weight)  # заносим в матрицу весов

        # генерируем ребра не из остовного дерева
        edges_not_tree = self.num_of_edges - (self.n - 1)  # ребер не в остовном дереве
        for _ in range(edges_not_tree):  # генерируем ребра поверх дерева
            first = random.randint(0, self.n - 1)  # первая вершина (начало ребра)
            second = random.randint(0, self.n - 1)  # вторая вершина (конец ребра)
            while second == first or self.W[first][second] != '-':  # чтобы избежать петли и повтора ребра
                first = random.randint(0, self.n - 1)
                second = random.randint(0, self.n - 1)
            self.W[first][second] = self.W[second][first] = \
                random.randint(self.min_edge_weight,
                               self.max_edge_weight)  # прописываем ребро

    def v_generation(self):
        """Генерация матрицы весов вершин V"""
        self.V = list()
        for i in range(self.n):
            self.V.append(round(self.min_node_weight +
                                (self.max_node_weight - self.min_node_weight) *
                                random.random(), 4))

    def replace_from_files(self, filename1='Weight_0.txt', filename2='Vertex_0.txt'):
        """Считывает матрицы W и V из файлов
        :param filename1: имя файла с матрицей W
        :param filename2: имя файла с матрицей V"""
        # опустошаем матрицы W и V
        self.W = list()
        self.V = list()

        # перезаписываем матрицу W
        list_string = list()
        with open(filename1, "r") as f:
            for line in f.readlines():
                list_string.append(line[: len(line) - 2])  # отрезаем \n в конце каждой строки
        for value in list_string:  # формируем из списка строк список списков, убираем пробелы
            temp = value.rsplit()
            self.W.append(temp)
        for i, list_i in enumerate(self.W):
            for j, list_j in enumerate(list_i):
                if self.W[i][j] != '-':
                    self.W[i][j] = int(self.W[i][j])

        # перезаписываем матрицу V
        v_str = list()
        with open(filename2, "r") as f:
            line = f.readline()
            v_str = line.rsplit()
            for i in v_str:
                self.V.append(float(i))

        self.metrics()         # пересчет метрик графа
        self.node_degreeses()  # пересчет степеней вершин

    def graph_draw(self, path=list(), tree=list(), red_nodes=list()):
        """Рисует граф
        :param path: путь в графе (выделяется красным)
        :param tree: дерево в графе (выделяется фиолетовым)
        :param red_nodes: вершины (выделяются красным)
        """
        # список ребер графа
        edges = list()
        path_edges = list()
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.W[i][j] != '-':
                    edges.append((i, j))

        # список ребер пути path
        if path:
            for i, node in enumerate(path[:-1]):
                path_edges.append((path[i], path[i + 1]))
                path_edges.append((path[i + 1], path[i]))

        # отрисовка графа
        if len(self.W) <= 250:  # если n <= 250
            g = nx.Graph()
            g.add_nodes_from(range(self.n))
            g.add_edges_from(edges)

            node_colors = []
            edge_colors = []
            for node in g.nodes():
                if node in path:
                    node_colors.append('green')
                elif node in red_nodes:
                    node_colors.append('red')
                else:
                    node_colors.append('gray')

            for edge in g.edges():
                if edge in path_edges:
                    edge_colors.append('green')
                elif edge in tree:
                    edge_colors.append('magenta')
                else:
                    edge_colors.append('black')
            
            nx.draw(g, with_labels=True, node_color=node_colors, edge_color=edge_colors)  # хаотичное расположение
            plt.draw()
            plt.show()

    
    def path_length(self, path):
        """Вычисление длины маршрута
        Если нет такого маршрута, то False
        """
        pass

    def tree_weight(self, edges_list):
        """Вычисление веса дерева, заданного списком ребер"""
        pass

 
class RandomDiGraph(RandomGraph):
    """Подкласс ориентированных графов.
    Создается на основе класса RandomGraph
    наследованием его атрибутов и методов.
    Некоторые методы переопределены по сравнению
    с родительским классом.
    """
    def w_generation(self):
        """Генерация матрицы весов W"""
        self.num_of_edges = int(self.mean_degree_initial * self.n)   # число ребер графа
        # заполняем матрицу W '-' и 0
        for i in range(self.n):
            self.W.append(['-'] * self.n)
            self.W[i][i] = 0  # главная диагональ 0
        # генерируем дуги
        for _ in range(self.num_of_edges):
            first = random.randint(0, self.n - 1)  # первая вершина (начало дуги)
            second = random.randint(0, self.n - 1)  # вторая вершина (конец дуги)
            while second == first or self.W[first][second] != '-':  # чтобы избежать петли и повтора дуги
                first = random.randint(0, self.n - 1)
                second = random.randint(0, self.n - 1)
            self.W[first][second] = random.randint(self.min_edge_weight,
                               self.max_edge_weight)  # прописываем дугу в граф

    def metrics(self):
        """Расчет метрик ориентированного графа"""
        pass

    def node_degreeses(self):
        """Вычияляет распределение степеней вершин графа
        Находит список висячих вершин (одна дуга входит или одна дуга выходит)
        Находит список изолированных вершин (нет инцидентных дуг)"""
        pass

    @staticmethod
    def edge_deleter(W1, edge):
        """Удаляет ребро графа"""
        pass

    @staticmethod
    def edge_inserter(W1, edge, weight):
        """Добавляет ребро edge в граф"""
        pass

    def graph_draw(self, path=list(), tree=list(), red_nodes=list()):
        """Рисует орграф
        :param path: путь в графе (выделяется красным)
        :param tree: дерево в графе (выделяется фиолетовым)
        :param red_nodes: вершины (выделяются красным)
        """
        # список ребер графа
        edges = list()
        path_edges = list()
        for i in range(self.n):
            for j in range(self.n):
                if self.W[i][j] != '-' and self.W[i][j] != 0:
                    edges.append((i, j))

        # список ребер пути path
        if path:
            for i, node in enumerate(path[:-1]):
                path_edges.append((path[i], path[i + 1]))
                path_edges.append((path[i + 1], path[i]))

        # отрисовка графа
        if len(self.W) <= 250:  # если n <= 250
            g = nx.DiGraph()
            g.add_nodes_from(range(self.n))
            g.add_edges_from(edges)

            node_colors = []
            edge_colors = []
            for node in g.nodes():
                if node in path:
                    node_colors.append('green')
                elif node in red_nodes:
                    node_colors.append('red')
                else:
                    node_colors.append('gray')

            for edge in g.edges():
                if edge in path_edges:
                    edge_colors.append('green')
                elif edge in tree:
                    edge_colors.append('magenta')
                else:
                    edge_colors.append('black')

            nx.draw_circular(g, with_labels=True, node_color=node_colors, edge_color=edge_colors)
            plt.draw()
            plt.show()

class RandomEulersGraph(RandomGraph):
    """Эйлеров граф.
    Неориентированный граф с эйлеровым циклом.
    Переопределена функция генерации графа."""

    def w_generation(self):

        def m_calc(n, mean_degree):
            """
            Предварительно вычисляет число ребер графа
            :param mean_degree: средняя степень вершин
            :return: m
            """
            if mean_degree < 2:
                mean_degree = 2  # минимальный граф с эйлеровым циклом
            if mean_degree > n - 1 and n % 2 != 0:  # если средняя степень > n-1 и число вершин нечетное
                mean_degree = n - 1  # будет сгенеирован полный граф (эйлеров)
            if mean_degree > n - 1 and n % 2 == 0:  # если средняя степень > n-1 и число вершин четное
                mean_degree = n - 2  # то средняя степень n-2
            m = int(mean_degree * n / 2)  # общее число ребер графа
            return m

        def possible_edges(n):
            """
            Вычисляет список возможных чисел ребер эйлерова графа
            """
            p_edges = []
            if n == 3 or n == 4:  # если 3 или 4 вершины
                p_edges.append(n)
            elif n % 2 == 0:  # иначе если число вершин четное
                p_edges.append(n)
                for i in range(n + 3, int(n * (n - 1) / 2 - n / 2) + 1):
                    p_edges.append(i)
            else:  # иначе если число вершин нечетное
                p_edges.append(n)
                for i in range(n + 3, int(n * (n - 1) / 2) - 2):
                    p_edges.append(i)
                p_edges.append(int(n * (n - 1) / 2))

            return p_edges

        def num_of_edges_check(n, mean_degree):
            """
            Проверка допустимости числа ребер для эйлерова графа
            Если число некорректное, то выбирается ближайшее
            """
            m = m_calc(n, mean_degree)
            p_edges = possible_edges(n)  # список возможных чисел ребер
            p_edges1 = possible_edges(n)  # список возможных чисел ребер
            if m not in p_edges1:  # если найденное число ребер не допустимо для эйлерова графа
                for i in range(len(p_edges1)):
                    p_edges1[i] = abs(p_edges1[i] - m)
                min_delta = min(p_edges1)
                index = p_edges1.index(min_delta)
                m = p_edges[index]
            return m

        def is_all_even(d):
            """
            Проверяет, все ли числа из списка d четные
            """
            for degree in d:
                if degree % 2 != 0:
                    return False
            return True

        def shuffle_nodes(n):
            """
            Выдает n вершин в случайном порядке
            """
            nodes = []
            for i in range(n):
                nodes.append(i)
            random.shuffle(nodes)
            return nodes

        def w_gen(n, m):
            """
            Генерирует матрицу весов
            :param n: число вершин
            :param m: число ребер
            :return:
            """
            W1 = list()
            for _ in range(n):
                W1.append(['-'] * n)
            for i in range(n):
                W1[i][i] = 0

            d = [2] * n  # степени вершин (список)
            nodes = shuffle_nodes(n)  # герерируем список вершин со случайным порядком
            for i in range(n - 1):  # строим первоначальный обход графа
                W1[nodes[i]][nodes[i + 1]] = 1
                W1[nodes[i + 1]][nodes[i]] = 1
            W1[nodes[-1]][nodes[0]] = 1
            W1[nodes[0]][nodes[-1]] = 1

            for _ in range(m - n):  # строим недостающие ребра
                start = random.randint(0, n - 1)
                end = random.randint(0, n - 1)
                while end == start or W1[start][end] == 1 or W1[end][start] == 1:
                    start = random.randint(0, n - 1)
                    end = random.randint(0, n - 1)
                d[start] += 1
                d[end] += 1
                W1[start][end] = 1
                W1[end][start] = 1

            return W1, d

        m = num_of_edges_check(self.n, self.mean_degree_initial)  # находим число ребер эйлерова графа
        Gen = w_gen(self.n, m)  # генерируем граф впервые
        d = Gen[1]
        attempts = 1            # количество попыток
        while not is_all_even(d):  # если это не эйлеров граф, то генерируем повторно
            Gen = w_gen(self.n, m)
            d = Gen[1]
            attempts += 1

        self.W = Gen[0]         # сохраняем матрицу весов в атрибуты графа

if __name__ == '__main__':
    g1 = RandomGraph(9, 3, 1, 9)
    #g1.replace_from_files('Weight_0.txt', 'Vertex_0.txt')
    g1.graph_draw([], [], [0])
