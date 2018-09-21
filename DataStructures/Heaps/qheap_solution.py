import heapq
data = int(input())
heap = []
dictionary = {}
for i in range(data):
    option = input().split()
    if option[0] == '1':
        option = int(option[1])
        dictionary[option] = 0
        heapq.heappush(heap, option)
    elif option[0] == '2':
        option = int(option[1])
        dictionary[option] = 1
    else:
        while dictionary[heap[0]] == 1:
            heapq.heappop(heap)
        print(heap[0])