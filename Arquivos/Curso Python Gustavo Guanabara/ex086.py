matris = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matris[l][c] = int(input(f'Digite um valor: [{l}, {c}]'))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matris[l][c]:^5}]', end='')
    print()