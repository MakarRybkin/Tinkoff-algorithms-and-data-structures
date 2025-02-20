def search_min_diff(a,b,low, high) -> int:
    if high - low == 1 :
        if abs(b-a[low])>abs(a[high]-b):
            return a[high]
        else:
            return a[low]
    mid = (low + high) // 2
    if a[mid] > b:
        return search_min_diff(a, b, low, mid)
    elif a[mid] < b:
        return search_min_diff(a, b, mid, high)
n,k = map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
for i in range(k):
    print(search_min_diff(a,b[i],0,len(a)-1))