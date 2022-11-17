import random
kelas = ['Warrior','Mage','Tank','Archer']
nama_player = input('Masukan Nama: ')
chance = ['Kalah','Menang','Kalah','Kalah','Kalah']

print(f'Halo {nama_player.capitalize()} Silahkan Pilih Kelas Mu: ')
for i,j in enumerate(kelas,start=1):
    print(f'{i}. {j}')
pilihan = kelas[int(input())-1]

opsi = int(input(f'Kamu adalah seorang {pilihan}, lalu ada Monster di depan mu, apa yang akan kamu lakukan? \n1. Serang\n2. Kabur\n'))

if opsi == 1:
    if random.choice(chance) == 'Menang':
        print('Kamu Berhasil Mengalahkan Monster Tersebut, Dan Akan Diingat Sebagai Legenda')
    else:
        print('Baru Juga Main Dah Mau Lawan Monster Aja :v, Ya Kalah Toh.')
    print('\n------------------------------THE END---------------------------')
else:
    print('Kamu Lari, Dan akan selalu diingat sebagai pengecut...Tamat')

