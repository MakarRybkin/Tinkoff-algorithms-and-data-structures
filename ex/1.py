
N, M = map(int, input().split())
computers = []
for _ in range(M):
    computers.append(list(map(int, input().split())))

def can_process_N(time_limit):
    total_processed_tasks = 0
    for T_i, B_i, Y_i in computers:
        if time_limit < T_i:
            continue

        block_time = T_i * B_i + Y_i
        num_blocks = time_limit // block_time
        processed_in_blocks = num_blocks * B_i
        remaining_time = time_limit - num_blocks * block_time
        can_process_more = min(B_i, remaining_time // T_i)

        total_processed_tasks += (processed_in_blocks + can_process_more)
        if total_processed_tasks >= N:
            return True
    return total_processed_tasks >= N

low = 0
high = 2 * (10 ** 9) * (10 ** 9)
ans_time = high

while low <= high:
    mid = (low + high) // 2
    if can_process_N(mid):
        ans_time = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans_time)

final_distribution = [0] * M
tasks_to_assign = N

for i in range(M):
    T_i, B_i, Y_i = computers[i]

    if ans_time < T_i:
        final_distribution[i] = 0
        continue

    block_time = T_i * B_i + Y_i
    num_blocks = ans_time // block_time
    processed_in_blocks = num_blocks * B_i
    remaining_time = ans_time - num_blocks * block_time
    can_process_more = min(B_i, remaining_time // T_i)

    tasks_on_this_computer_at_ans_time = processed_in_blocks + can_process_more

    assign_count = min(tasks_on_this_computer_at_ans_time, tasks_to_assign)
    final_distribution[i] = assign_count
    tasks_to_assign -= assign_count

    if tasks_to_assign == 0:
        break

print(*final_distribution)
