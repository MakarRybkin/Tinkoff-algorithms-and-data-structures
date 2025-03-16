from sys import stdin
import sys

n,k=[int(x) for x  in stdin.readline().split()]
numbers=[int(x) for x in stdin.readline().split()]
start,end=1,numbers[-1]-numbers[0]

def binary_search(start,end,k):
    max_diff = 0
    while start <=end:
        mid=(start+end)//2
        if count_max_possible_diffs(numbers,mid,k):
            max_diff = mid
            start = mid+1
        else:
            end = mid-1
    return max_diff

def count_max_possible_diffs(numbers,min_dist,k):
    count=1
    last_position = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] - last_position >= min_dist:
            count += 1
            last_position = numbers[i]
            if count == k:
                return True
    return False
print(binary_search(start,end,k))