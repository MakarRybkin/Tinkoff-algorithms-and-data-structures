import sys

# Увеличиваем лимит рекурсии для глубоких деревьев (хотя здесь не используется прямой DFS для LCA)
sys.setrecursionlimit(2 * 10**5)

class LCA:
    def __init__(self, n, parents_input):
        self.n = n
        # LOGN - это ceil(log2(n)). Для n=10^5, log2(10^5) примерно 16.6, так что 17 или 18 достаточно.
        self.LOGN = (n - 1).bit_length() # Эквивалент math.ceil(math.log2(n)) для n>1, иначе 1.
        if self.n == 1: # Edge case для дерева из одной вершины
             self.LOGN = 1

        # parent[u][k] будет хранить 2^k-го предка вершины u
        # Инициализируем нулями (или -1, если не хотим считать корень предком самого себя)
        self.parent = [[0] * self.LOGN for _ in range(n)]
        # depth[u] будет хранить глубину вершины u
        self.depth = [0] * n

        self._build_lca_structure(parents_input)

    def _build_lca_structure(self, parents_input):
        # Инициализируем parent[u][0] и depth для всех вершин
        # Корень (вершина 0) имеет глубину 0 и его 2^0-й предок - он сам (для удобства подъемов)
        self.depth[0] = 0
        self.parent[0][0] = 0

        # parents_input содержит предков p_i для вершин i от 1 до n-1.
        # parents_input[i-1] - это предок вершины i.
        for i in range(1, self.n):
            p_i = parents_input[i - 1]
            self.parent[i][0] = p_i
            self.depth[i] = self.depth[p_i] + 1

        # Заполняем остальные столбцы parent[u][k]
        for k in range(1, self.LOGN):
            for u in range(self.n):
                self.parent[u][k] = self.parent[self.parent[u][k-1]][k-1]

    def find_lca(self, u, v):
        # 1. Выравнивание глубин: Поднимаем более глубокую вершину
        if self.depth[u] < self.depth[v]:
            u, v = v, u # Меняем местами, чтобы u всегда была глубже или на той же глубине

        # Поднимаем u на ту же глубину, что и v
        for k in range(self.LOGN - 1, -1, -1):
            if self.depth[u] - (1 << k) >= self.depth[v]:
                u = self.parent[u][k]

        # Теперь u и v на одной глубине.
        # 2. Если u и v стали одинаковыми, это и есть LCA
        if u == v:
            return u

        # 3. Одновременный подъем, пока их родители не станут одинаковыми
        # Идем от самых больших степеней двойки вниз
        for k in range(self.LOGN - 1, -1, -1):
            # Если 2^k-е предки различны, значит LCA находится выше них
            # Поднимаем обе вершины
            if self.parent[u][k] != self.parent[v][k]:
                u = self.parent[u][k]
                v = self.parent[v][k]

        # Теперь u и v - непосредственные потомки LCA.
        # Их 2^0-й предок (то есть непосредственный родитель) - это и есть LCA.
        return self.parent[u][0]

# --- Основная часть программы ---
if __name__ == "__main__":
    n = int(sys.stdin.readline())

    # Входной формат: n-1 целых чисел pi — предок вершины i (0 <= pi < i)
    # Это значит, что p_input[i-1] будет предком вершины i.
    if n > 1:
        parents_input = list(map(int, sys.stdin.readline().split()))
    else: # Для случая n=1, предок отсутствует.
        parents_input = []

    lca_solver = LCA(n, parents_input)

    m = int(sys.stdin.readline())

    results = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        results.append(str(lca_solver.find_lca(u, v)))

    sys.stdout.write("\n".join(results) + "\n")