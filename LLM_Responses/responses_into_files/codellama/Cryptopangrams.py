for t in range(int(input())):
    N, L = map(int, input().split())
    ciphertext = list(map(int, input().split()))
    plaintext = ""
    for i in range(L):
        c = chr((ciphertext[i] - 1) % 26 + ord('A'))
        plaintext += c
    print("Case #" + str(t+1) + ": " + plaintext)