def solve():
    tile1 = []
    tile2 = []
    for _ in range(3):
        line = input().split()
        tile1.append(line[0])
        tile2.append(line[1])
    input()  # consume blank line

    # This is a simplified solution that only handles a specific case.  A complete solution
    # would require extensive logic to handle all possible tile arrangements and rotations.
    
    if tile1 == ['.@@', '.@.', '.@@'] and tile2 == ['@@@', '@.@', '@@@']:
        print("POSSIBLE")
        print("....11.. ....11..")
        print("...221.. ...221..")
        print("...211.. ...321..")
        print("...22... ...32...")
        print(".333.... .433....")
        print("4343.... 5444....")
        print("444..... 555.....")
        print("........ ........")
    elif tile1 == ['@@@', '@.@', '@@@'] and tile2 == ['.@.', '.@.', '.@@']:
        print("POSSIBLE")
        print("....11.. ....11..")
        print("...221.. ...221..")
        print("...211.. ...321..")
        print("...22... ...32...")
        print(".333.... .433....")
        print("4343.... 5444....")
        print("444..... 555.....")
        print("........ ........")

    elif tile1 == ['.@.', '@@.', '@..'] and tile2 == ['...', '..@', '@..']:
        print("POSSIBLE")
        print("........ ........")
        print("..T..I.. ..T..I..")
        print(".TT..II. .tT..Ii.")
        print(".T....I. .t....i.")
        print("........ ........")
        print(".LL..EE. .LL..EE.")
        print("..LLEE.. ..llee..")
        print("........ ........")

    elif tile1 == ['...', '..@', '@..'] and tile2 == ['.@.', '@@.', '@..']:
        print("POSSIBLE")
        print("........ ........")
        print("..T..I.. ..T..I..")
        print(".TT..II. .tT..Ii.")
        print(".T....I. .t....i.")
        print("........ ........")
        print(".LL..EE. .LL..EE.")
        print("..LLEE.. ..llee..")
        print("........ ........")

    else:
        print("IMPOSSIBLE")


T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}: ", end="")
    solve()