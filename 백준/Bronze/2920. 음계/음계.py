num_list = list(map(int, input().split()))
ans = [i for i in range(1,9)]
if num_list == ans:
    print('ascending')
elif num_list == sorted(num_list, reverse=True):
    print('descending')
else:
    print('mixed')