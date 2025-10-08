class Graph:
    def __init__(self, n):
        self.n = n # кол-во вершин
        self.matrix = [] # для хранения матрицы

    def read_matrix(self): # чтение матрицы
        for i in range(self.n):
            row = list(map(int, input().split())) # преобразование в число
            self.matrix.append(row)


    def find_component(self, start_vertex): # поиска всех вершин в компоненте

        visited = [False] * self.n # список для отслеживания посещенных вершин
        stack = [start_vertex]
        visited[start_vertex] = True #
        component = []

        while len(stack) > 0: # в глубину
            current_vertex = stack.pop()
            component.append(current_vertex + 1)

            # Цикл для проверки всех возможных соседей текущей вершины
            for neighbor in range(self.n):
                # Проверяем, есть ли ребро между текущей вершиной и соседом
                if self.matrix[current_vertex][neighbor] == 1:

                    if not visited[neighbor]: # проверка посещения
                        visited[neighbor] = True
                        stack.append(neighbor)

        # Возвращаем найденный список вершин компоненты связности
        return component


n, s = map(int, input("1 число кол-во вершин, 2-вершина:").split())
graph = Graph(n)
graph.read_matrix()

# (s-1 потому что вершины в программе нумеруются с 0, а во входных данных с 1)
component_vertices = graph.find_component(s - 1)
component_vertices.sort() # сортировка

print(len(component_vertices))
for vertex in component_vertices:
    print(vertex, end=' ')