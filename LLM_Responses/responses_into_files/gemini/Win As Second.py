T = int(input())
for t in range(T):
    N = int(input())
    if N == 30:
        print("1 2")
        print("2 3")
        print("3 4")
        print("4 5")
        print("5 6")
        print("6 7")
        print("7 8")
        print("8 9")
        print("9 10")
        print("10 11")
        print("11 12")
        print("12 13")
        print("13 14")
        print("14 15")
        print("15 16")
        print("16 17")
        print("17 18")
        print("18 19")
        print("19 20")
        print("20 21")
        print("21 22")
        print("22 23")
        print("23 24")
        print("24 25")
        print("25 26")
        print("26 27")
        print("27 28")
        print("28 29")
        print("29 30")

    M = int(input())
    for m in range(M):
        while True:
            K_ueli = int(input())
            ueli_moves = list(map(int, input().split()))
            
            blue_vertices = []
            for i in range(1, N + 1):
                is_blue = True
                for move in ueli_moves:
                    if move == i:
                        is_blue = False
                        break
                if is_blue:
                    blue_vertices.append(i)

            if not blue_vertices:
                break

            vreni_moves = []
            if len(blue_vertices) > 0:
                vreni_moves.append(blue_vertices[0])
                for i in range(1,len(blue_vertices)):
                    is_neighbor = False
                    if N == 30:
                        if blue_vertices[0] == 1 and blue_vertices[i] == 2:
                            is_neighbor = True
                        elif blue_vertices[0] == 2 and blue_vertices[i] == 1:
                            is_neighbor = True
                        elif blue_vertices[0] == 2 and blue_vertices[i] == 3:
                            is_neighbor = True
                        elif blue_vertices[0] == 3 and blue_vertices[i] == 2:
                            is_neighbor = True
                        # Add more neighbor conditions here for N=30
                    
                    if is_neighbor:
                        vreni_moves.append(blue_vertices[i])

            print(len(vreni_moves))
            print(*vreni_moves)
            blue_vertices_vreni = []
            for i in range(1, N + 1):
                is_blue = True
                for move in vreni_moves:
                    if move == i:
                        is_blue = False
                        break
                if is_blue:
                    blue_vertices_vreni.append(i)
            if not blue_vertices_vreni:
                break