# Импортируем необходимые библиотеки
import sys
import bisect  # Модуль для работы с отсортированными списками


# Функция для решения задачи
def solve():
    # Читаем количество монстров
    n = int(sys.stdin.readline())

    # Читаем значения атаки и защиты монстров
    # Используем списки с 0-й индексацией, но монстры пронумерованы с 1
    # Поэтому для доступа к атаке/защите монстра i будем использовать индексы i-1
    a = list(map(int, sys.stdin.readline().split()))
    d = list(map(int, sys.stdin.readline().split()))

    # Храним живых монстров в отсортированном списке.
    # Это позволяет эффективно находить соседей с помощью бинарного поиска (bisect).
    # Монстры нумеруются от 1 до n, поэтому список содержит эти индексы.
    living_monsters_list = list(range(1, n + 1))

    # Дополнительно используем множество для быстрой проверки, жив ли монстр (O(1) в среднем)
    living_monsters_set = set(living_monsters_list)

    # Множество монстров, урон которых нужно проверить в текущем раунде.
    # Изначально проверяем урон всех монстров.
    to_check = set(living_monsters_list)

    # Список для хранения результатов (количества умерших монстров в каждом раунде)
    results = []

    # Симулируем до n раундов.
    # Если все монстры умрут раньше, цикл завершится досрочно.
    for _ in range(n):
        # Если множество монстров для проверки пусто, значит, больше никто не будет получать урон и умирать.
        # Бой закончен.
        if not to_check:
            # Заполняем оставшиеся раунды нулями
            results.extend([0] * (n - len(results)))
            break

        # Кандидаты для проверки урона в текущем раунде.
        # Преобразуем множество в список и сортируем. Сортировка не строго необходима для корректности,
        # но может помочь сделать порядок обработки предсказуемым.
        current_check_candidates = sorted(list(to_check))
        to_check = set()  # Очищаем множество для кандидатов следующего раунда

        # Множество монстров, которые определены как умирающие в текущем раунде
        dying_this_round = set()

        # Создаем копию списка живых монстров в начале фазы проверки урона.
        # Это необходимо, чтобы правильно определить текущих соседей для расчета урона,
        # до того как монстры начнут умирать в конце раунда.
        current_living_list_at_start_of_check = list(living_monsters_list)

        # Проходим по всем кандидатам и определяем, кто умрет
        for monster_idx in current_check_candidates:
            # Проверяем урон только для монстров, которые еще живы (их могли добавить в to_check,
            # но они могли умереть раньше в этом же раунде из-за другого соседа).
            if monster_idx in living_monsters_set:
                damage = 0

                # Находим индекс текущего монстра в списке живых на начало раунда с помощью бинарного поиска
                idx_in_list = bisect.bisect_left(current_living_list_at_start_of_check, monster_idx)

                # Находим левого соседа: элемент перед текущим в отсортированном списке
                left_neighbor = 0  # 0 означает отсутствие соседа (если монстр первый или его левый сосед умер)
                if idx_in_list > 0:
                    left_neighbor = current_living_list_at_start_of_check[idx_in_list - 1]
                    damage += a[
                        left_neighbor - 1]  # Используем 0-ю индексацию для списка атак (a[0] для монстра 1 и т.д.)

                # Находим правого соседа: элемент после текущего в отсортированном списке
                right_neighbor = 0  # 0 означает отсутствие соседа (если монстр последний или его правый сосед умер)
                if idx_in_list < len(current_living_list_at_start_of_check) - 1:
                    right_neighbor = current_living_list_at_start_of_check[idx_in_list + 1]
                    damage += a[right_neighbor - 1]  # Используем 0-ю индексацию для списка атак

                # Если суммарный урон, полученный монстром в этом раунде, строго больше его защиты, он умирает.
                if damage > d[monster_idx - 1]:  # Используем 0-ю индексацию для списка защиты
                    dying_this_round.add(monster_idx)

        # Добавляем количество умерших монстров в текущем раунде к результатам
        results.append(len(dying_this_round))

        # Если в этом раунде никто не умер, значит, оставшиеся монстры не могут убить друг друга.
        # Бой закончен досрочно.
        if not dying_this_round:
            # Заполняем оставшиеся раунды нулями
            results.extend([0] * (n - len(results)))
            break

        # Определяем соседей умерших монстров, которых, возможно, нужно проверить в следующем раунде.
        # Их соседи могли стать ближе друг к другу из-за смерти.
        neighbors_to_recheck = set()

        # Итерируемся по монстрам, которые определены как умирающие в этом раунде
        for dying_monster_idx in dying_this_round:
            # Находим его соседей в списке живых *до* его удаления из списка.
            # Используем список `current_living_list_at_start_of_check` для этого.
            idx_in_list = bisect.bisect_left(current_living_list_at_start_of_check, dying_monster_idx)

            # Определяем левого соседа умершего монстра до его смерти
            left_neighbor = 0
            if idx_in_list > 0:
                left_neighbor = current_living_list_at_start_of_check[idx_in_list - 1]

            # Определяем правого соседа умершего монстра до его смерти
            right_neighbor = 0
            if idx_in_list < len(current_living_list_at_start_of_check) - 1:
                right_neighbor = current_living_list_at_start_of_check[idx_in_list + 1]

            # Если левый сосед существовал (не 0) и он еще жив (не умер в этом же раунде),
            # добавляем его в множество для проверки в следующем раунде.
            if left_neighbor != 0 and left_neighbor in living_monsters_set:
                neighbors_to_recheck.add(left_neighbor)
            # Если правый сосед существовал (не 0) и он еще жив,
            # добавляем его в множество для проверки в следующем раунде.
            if right_neighbor != 0 and right_neighbor in living_monsters_set:
                neighbors_to_recheck.add(right_neighbor)

        # Удаляем умерших монстров из списка живых монстров и множества живых монстров.
        # Создание нового списка с помощью list comprehension - удобный способ удалить
        # несколько элементов, хотя в худшем случае это может быть медленно (O(N) за операцию).
        new_living_monsters_list = []
        for monster_idx in living_monsters_list:
            if monster_idx not in dying_this_round:
                new_living_monsters_list.append(monster_idx)
            else:
                # Удаляем умершего монстра из множества живых
                living_monsters_set.remove(monster_idx)

        # Обновляем список живых монстров
        living_monsters_list = new_living_monsters_list

        # Монстры для проверки в следующем раунде - это их соседи, чья "соседская" ситуация изменилась
        to_check = neighbors_to_recheck

    # Выводим результаты для всех n раундов, разделенные пробелами
    # Если бой закончился раньше, оставшиеся результаты будут 0
    print(*results)


# Запускаем функцию решения задачи
solve()