import sys

# Увеличиваем лимит рекурсии, хотя для этой итеративной версии не строго необходимо
# Но это хорошая практика для задач на деревьях
sys.setrecursionlimit(2 * 10 ** 5)


class TreePathMinEdge:
    def __init__(self, n, edge_data_input):
        self.n = n
        # LOGN - это ceil(log2(n)). Для n=10^5, log2(10^5) примерно 16.6, так что 18 достаточно.
        # .bit_length() возвращает количество бит, необходимое для представления числа.
        # Для n=1, (1-1).bit_length() == 0, но нам нужно хотя бы 1, чтобы избежать ошибок с пустыми массивами
        self.LOGN = (n - 1).bit_length() if n > 1 else 1

        # parent[u][k] - 2^k-й предок вершины u
        self.parent = [[0] * self.LOGN for _ in range(n)]
        # min_edge[u][k] - мин. вес ребра на пути от u до parent[u][k]
        # Используем sys.maxsize для инициализации "бесконечностью"
        self.min_edge_val = [[sys.maxsize] * self.LOGN for _ in range(n)]
        # depth[u] - глубина вершины u
        self.depth = [0] * n

        self._build_lca_structure(edge_data_input)

    def _build_lca_structure(self, edge_data_input):
        # Инициализируем для корня (вершины 0)
        self.depth[0] = 0
        self.parent[0][0] = 0  # Корень сам себе предок на 0-м уровне
        # min_edge_val[0][0] остается sys.maxsize, так как у корня нет входящего ребра от родителя

        # Заполняем parent[u][0], min_edge_val[u][0] и depth для всех узлов
        # edge_data_input[i] содержит информацию для вершины i+1 (т.к. i - это индекс строки, а вершина - i+1)
        for i in range(self.n - 1):
            child_node = i + 1  # Вершина, для которой мы считываем данные
            p = edge_data_input[i][0]  # Предок
            w = edge_data_input[i][1]  # Вес ребра

            self.parent[child_node][0] = p
            self.min_edge_val[child_node][0] = w
            self.depth[child_node] = self.depth[p] + 1

        # Заполняем остальные столбцы parent[u][k] и min_edge_val[u][k]
        for k in range(1, self.LOGN):
            for u in range(self.n):
                # 2^k-й предок - это 2^(k-1)-й предок 2^(k-1)-го предка
                self.parent[u][k] = self.parent[self.parent[u][k - 1]][k - 1]
                # Минимальный вес - это минимум из двух половин пути
                self.min_edge_val[u][k] = min(
                    self.min_edge_val[u][k - 1],
                    self.min_edge_val[self.parent[u][k - 1]][k - 1]
                )

    def find_min_edge_on_path(self, u, v):
        current_min = sys.maxsize  # Инициализируем очень большим значением

        # 1. Выравнивание глубин: Поднимаем более глубокую вершину
        if self.depth[u] < self.depth[v]:
            u, v = v, u  # Меняем местами, чтобы u всегда была глубже или на той же глубине

        # Поднимаем u на ту же глубину, что и v, и обновляем current_min
        for k in range(self.LOGN - 1, -1, -1):
            # Если u выше на 2^k или более, чем v
            if self.depth[u] - (1 << k) >= self.depth[v]:
                current_min = min(current_min, self.min_edge_val[u][k])
                u = self.parent[u][k]

        # Теперь u и v на одной глубине.
        # 2. Если u и v стали одинаковыми, это и есть LCA.
        # В этом случае, u (или v) - это предок другой вершины, и мы уже собрали все минимумы.
        if u == v:
            return current_min

        # 3. Одновременный подъем, пока их родители не станут одинаковыми
        for k in range(self.LOGN - 1, -1, -1):
            # Если 2^k-е предки различны, значит LCA находится выше них
            # Поднимаем обе вершины и обновляем минимум
            if self.parent[u][k] != self.parent[v][k]:
                current_min = min(current_min, self.min_edge_val[u][k])
                current_min = min(current_min, self.min_edge_val[v][k])
                u = self.parent[u][k]
                v = self.parent[v][k]

        # Теперь u и v - непосредственные потомки LCA.
        # Нужно учесть ребра от u и v до их общего родителя (LCA).
        current_min = min(current_min, self.min_edge_val[u][0])
        current_min = min(current_min, self.min_edge_val[v][0])

        return current_min



n = int(sys.stdin.readline())

edge_data_input = []
# Для n-1 строк, считываем предок и вес ребра
for _ in range(n - 1):
    x, y = map(int, sys.stdin.readline().split())
    edge_data_input.append((x, y))

# Создаем экземпляр класса для решения
solver = TreePathMinEdge(n, edge_data_input)

m = int(sys.stdin.readline())

results = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    results.append(str(solver.find_min_edge_on_path(u, v)))

print(*results,sep = '\n')