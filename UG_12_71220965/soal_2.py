print('~~~ Selamat Datang di Kalkulator Sederhana ~~~')


def add(a,b):
    return f'{a} + {b} = {a+b}'

def subtract(a,b):
    return f'{a} - {b} = {a-b}'

def multiply(a,b):
    return f'{a} * {b} = {a*b}'

def divide(a,b):
    return f'{a} / {b} = {a/b}'

calculator = {
    '+':[add,'penjumlahan'],
    '-':[subtract,'pengurangan'],
    'x':[multiply,'perkalian'],
    ':':[divide,'pembagian']
}
#mengambil dan memodifikasi keys dari dictionary ug11 no 1



operator = input('Masukan operator matematika yang ingin anda hitung: ').lower()

if operator in calculator:
    hitung_lagi = True

    while hitung_lagi:
        jumlah_operasi = int(input(f'Mau {calculator[operator][1]} berapa: '))
        jumlah_print = int(input('Print berapa banyak: '))
        lst_operasi = {x:y for x,y in zip(range(1,jumlah_operasi+1),range(jumlah_operasi,0,-1))}
        for i in range(1,jumlah_print+1):
            print(calculator[operator][0](i,lst_operasi[i]))
        print('')

        tidak_valid = True

        while tidak_valid:
            coba_lagi = input('Apakah Anda Ingin Menghitung Lagi? (Y/T): ').upper()
            if coba_lagi == 'Y':
                tidak_valid = False
            elif coba_lagi == 'T':
                tidak_valid = False
                hitung_lagi = False
            else:
                print('Input Tidak Valid\n')
                continue
    print('Terima Kasih dan Sampai Jumpa Lagi!')
else:
    print('Maaf, Operator Matematika yang anda cari belum tersedia.')