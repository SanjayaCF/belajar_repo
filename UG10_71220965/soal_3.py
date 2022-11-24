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

lst = map(str,lst)

if opsi == 1:
    urut = ' '.join(sorted(lst))
    print(f'Urutan bilangan dari yang terkecil adalah {urut}')
else:
    urut = ' '.join(sorted(lst)[::-1])
    print(f'Urutan bilangan dari yang terbesar adalah {urut}')
