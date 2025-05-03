import random

def flip_bits(binary):
    return ''.join(['0' if bit == '1' else '1' for bit in binary]

def reset_record(binary, rotation):
    rotated = binary[rotation:] + binary[:rotation]
    return ''.join([flip_bits(bit) for bit in rotated])

def main():
    try:
        T = int(input())
        for case in range(1, T+1):
            initial_value = bin(random.randint(1, 254))[2:].zfill(8)
            current_value = initial_value
            num_exchanges = 0
            while current_value != '0'*8 and num_exchanges <= 30:
                new_value = reset_record(current_value, random.randint(1, 7))
                print(new_value)
                N_i = int(input())
                if N_i == -1:
                    break
                current_value = ''.join(['0']*N_i + ['1']*(8-N_i))
                num_exchanges += 1
            else:
                print('Wrong Answer')
    except Exception as e:
        print(-1)

if __name__ == "__main__":
    main()