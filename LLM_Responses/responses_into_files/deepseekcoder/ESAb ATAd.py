T = int(input())
B = 10
bits = [0]*B
queries = []
for _ in range(T):
    for _ in range(150):
        query = int(input())
        queries.append(query)
        if query % 10 == 1:
            bits[query//10] = (bits[query//10]+1)%2
    answer = ''
    for bit in bits:
        answer += str(bit)
    print(answer)