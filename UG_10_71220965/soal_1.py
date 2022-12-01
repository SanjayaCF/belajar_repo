print('Pilihlah salah satu bangun ruang yang ingin dihitung volumenya:\n1. Limas\n2. Bola\n3. Prisma\n4. Kerucut\n')

pilihan = int(input('Masukkan Pilihan Anda: '))
if pilihan == 1:
    panjang = float(input('Masukkan panjang sisi alas limas: '))
    tinggi = float(input('Masukkan tinggi limas: '))
    volume = f'Volume limas tersebut adalah {2*panjang*tinggi}'

elif pilihan == 2:
    jari2 = float(input('Masukkan panjang jari-jari bola: '))
    volume = f'Volume bola tersebut adalah {(4/3)*3.14*(jari2**3)}'

elif pilihan == 3:
    print('Pilihlah salah satu dari pilihan di bawah:\n1. Prisma Segitiga\n2. Prisma Segiempat\n3. Prisma Segilima')
    pilihan_prisma = int(input('Tentukan pilihan anda: '))
    if str(pilihan_prisma) in '123':
        panjang_sisi = float(input('Masukkan panjang sisi alas prisma: '))
        alas = float(input('Masukkan tinggi alas prisma: '))

        if pilihan_prisma == 1:
            tinggi_prisma = float(input('Masukan tinggi prisma segitiga: '))
            prisma = 'segitiga'
            hasil = 0.5*(panjang_sisi*alas*tinggi_prisma)
        elif pilihan_prisma == 2:
            tinggi_prisma = float(input('Masukan tinggi prisma segiempat: '))
            prisma = 'segiempat'
            hasil = panjang_sisi*alas*tinggi_prisma
        elif pilihan_prisma == 3:
            tinggi_prisma = float(input('Masukan tinggi prisma segilima: '))
            prisma = 'segilima'
            hasil = ((5*alas*panjang_sisi)*tinggi_prisma)/2
        volume = f'Volume prisma {prisma} tersebut adalah {hasil}'
    else:
        volume = 'Prisma yang Anda cari belum tersedia di kalkulator ini'

elif pilihan == 4:
    jari2 = float(input('Masukan jari-jari kerucut: '))
    tinggi_kerucut = float(input('Masukan tinggi kerucut: '))
    volume = f'Volume kerucut tersebut adalah {(1/3)*3.14*jari2*jari2*tinggi_kerucut}'

print(volume)
    
