palavras = ('Aprender', 'Programar', 'Ensinar', 'Python')

for p in palavras:
    print(f'\n Na palavra {p.lower()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')