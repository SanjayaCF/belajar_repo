print('SELAMAT DATANG DI PROGRAM PEMBUAT PIRAMIDA BERLUBANG')
n = int(input('Masukan Angka : '))

space = n-1
for i in range(n):
    print(' '*space,end='')
    print('*' if i == 0 else '**' if i != 0 and i != n-1 else '*'*(n*2-1))
    space -= 1