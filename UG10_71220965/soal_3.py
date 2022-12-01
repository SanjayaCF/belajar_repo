pilihan = ['Ascending','Descending']

print('Tentukan Pilihan Anda!!! [1/2]\n')
for i in range(1,len(pilihan)+1):
    print(f'{i}. {pilihan[i-1]}')

print('')

opsi = int(input('Masukan Pilihan yang anda Inginkan: '))

lst = []
for bil in ['Pertama','Kedua','Ketiga','Keempat']:
    bilangan = int(input(f'Masukan bilangan {bil} : '))
    lst.append(bilangan)

lst = map(int,lst)

if opsi == 1:
    print('Urutan bilangan dari yang terkecil adalah ',end='')
    print(*sorted(lst),sep=' ')
else:
    print('Urutan bilangan dari yang terbesar adalah ',end=' ')
    print(*sorted(lst,reverse=True),sep=' ')
