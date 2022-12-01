daftar1 = ['Sikat Gigi', 'Odol', 'Shampoo', 'Sabun', 'Ciduk']
daftar2 = ['Teh', 'Gula', 'Garam', 'Micin', 'Kecap']

try:
    pilihan = int(input('Jawab dengan angka [1/2]\n1. Rubah Belanjaan\n2. Keluar\nMasukan Pilihan: '))
    if pilihan == 1:
        insert1 = input('Masukan nama item ke daftar 1: ')
        ind1 = int(input('Masukan index yang ingin dirubah: '))
        daftar1[ind1] = insert1
        print('')
        insert2 = input('Masukan nama item ke daftar 2: ')
        ind2 = int(input('Masukan index yang ingin dirubah: '))
        daftar2[ind2] = insert2

    print('')
    print(f'Daftar Belanja 1: {daftar1}\n')
    print(f'Daftar Belanja 2: {daftar2}')
except:
    print('WRONG INPUT')