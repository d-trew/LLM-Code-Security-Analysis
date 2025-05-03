import sys
input = sys.stdin.readline
n_test = int(input())
for i in range(n_test):
    n, deque = map(int, input().split())
    deque = list(map(int, input().split()))
    
    # find the most delicious pancake and serve it to the customer
    max_deliciousness = max(deque)
    max_index = deque.index(max_deliciousness)
    customer_pay = 0
    if max_deliciousness >= deque[max_index - 1] and max_deliciousness >= deque[max_index + 1]:
        customer_pay = 1
    elif max_deliciousness < deque[max_index - 1] and max_deliciousness >= deque[max_index + 1]:
        customer_pay = 2
    else:
        customer_pay = 3
    
    # remove the most delicious pancake from the deque
    deque.pop(max_index)
    
    print('Case #%d: %d' % (i + 1, customer_pay))