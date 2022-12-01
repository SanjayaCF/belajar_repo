import random
from txt import *
import time
#mengubah kelas menjadi dict dengan tambahan status

nama_player = input('Masukan Nama: ').title()
chance = ['zonk','heal','crit','zonk','zonk']
reputasi = 100
monster_defeated = {mob:0 for mob in list(monster)}

print(f'Halo {nama_player}, {welcoming_txt.title()}\nPilih Kelas Mu:')#menambah text dari file lain
for i,j in enumerate(kelas,start=1):
    print(f'{i}. {j}')
pilihan = list(kelas)[int(input())-1]

print(status(pilihan))

def encounter(monster,user):
    global kelas
    global reputasi
    global performa
    plus = random.randint(10,30)
    min = random.randint(1,20)
    mob = random.choice(list(monster))
    opsi = int(input(f'Kamu Melihat Sebuah {mob}, Apa Yang Akan Kamu Lakukan?\n1. Serang [Reputasi +{plus}]\n2. Lari [Reputasi -{min}]\n'))
    mob_hp, mob_turn, mob_atk = monster[mob]['hp'], monster[mob]['turn'], monster[mob]['dmg']
    user_hp, user_turn, user_atk = user[pilihan]['hp'], user[pilihan]['turn'], user[pilihan]['dmg']
    if opsi == 1:
        while mob_hp > 0 and user_hp > 0:
            player_chance = random.randint(1,5)
            jackpot_chance = random.randint(1,5)
            if user_turn == 1:
                move = ''
                mult = 1
                if player_chance == jackpot_chance:
                    move = random.choice(chance)
                    if move == 'heal':
                        extra_hp = random.randint(5,15)
                        print(f'Kamu Mendapatkan Heal,\nHP: {user_hp} --> {user_hp+extra_hp}\n')
                        user_hp += extra_hp
                    elif move == 'crit':
                        mult = random.randint(2,3)
                        print(f'Menyerang Di Titik Lemah, Damage Menjadi Lebih Sakit {mult}x Lipat')
                    else:
                        print(f'Serangan {nama_player} ({kelas[pilihan]["kelas"]}) Terhadap {mob} Meleset\n')

                if move != 'zonk':
                    mob_hp -= user_atk*mult
                    performa['Total Damage Yang Diberikan'] += user_atk*mult
                    user_turn = user[pilihan]['turn']
                    performa['Jumlah Menyerang'] += 1
                    print(f'{nama_player} ({kelas[pilihan]["kelas"]}) Menyerang {mob}:')
                    print(f'HP: {mob_hp+user_atk*mult} --> {mob_hp if mob_hp > 0 else 0}\nTurn: {mob_turn} --> {mob_turn-1 if mob_turn != 1 else "After This"}\n')
                    time.sleep(1)
            else:
                user_turn -= 1
            if mob_hp > 0:
                if mob_turn == 1:
                    user_hp -= mob_atk
                    performa['Total Damage Yang Diterima'] += mob_atk
                    mob_turn = monster[mob]['turn']
                    print(f'{mob} Menyerang {nama_player} ({kelas[pilihan]["kelas"]}):')
                    print(f'HP: {user_hp+mob_atk} --> {user_hp if user_hp > 0 else 0}\nTurn: {user_turn} --> {user_turn-1 if user_turn != 1 else "After This"}\n')
                    time.sleep(1)
                else:
                    mob_turn -= 1
            else:
                reputasi += plus
                kelas[pilihan]['hp'] = user_hp
                monster_defeated[mob] += 1
                print(f'Kamu Berhasil Mengalahkan {mob}, Mendapatkan {plus} Poin Reputasi\n')
                print(status(pilihan))

            if user_hp <= 0:
                kelas[pilihan]['hp'] = 0
                print('------------------------------------YOU DIE------------------------------------\n')
                print('Jumlah Monster Yang Berhasil Dikalahkan:')
                for mons in monster_defeated:
                    print(f'{mons}: {monster_defeated[mons]}')
                print('')
                for log in performa:
                    print(f'{log}: {performa[log]}')
                print(f'Reputasi: {reputasi}')
                print('')
                print(random.choice(txt_reputasi[0 if reputasi < 150 else 1 if reputasi < 200 else 2]))
                print('')
                print('------------------------------------THE END------------------------------------')
    else:
        reputasi -= min
        print(f'Kamu Memutuskan Untuk Lari, Poin Reputasi Mu Berkurang Sebanyak {min}\n')
        if reputasi <= 0:
            print('---------------------------YOU SURVIVE, BUT AT WHAT COST?------------------------------------\n')
            print(f'Reputasi : {reputasi}\n')
            for log in performa:
                print(f'{log}: {performa[log]}')
            print('')
            print('Kamu Akan Diingat Sebagai Pengecut Dari Segala Pengecut Jika Seandainya Manusia Berhasil Bertahan Hidup.\n')
            print('------------------------------------THE END------------------------------------')

while kelas[pilihan]['hp'] > 0 and reputasi > 0:
    encounter(monster,kelas)


'''if opsi == 1:
    if random.choice(chance) == 'Menang':
        print('Kamu Berhasil Mengalahkan Monster Tersebut, Dan Akan Diingat Sebagai Legenda')
    else:
        print('Baru Juga Main Dah Mau Lawan Monster Aja :v, Ya Kalah Toh.')
    print('\n------------------------------THE END---------------------------')
else:
    print('Kamu Lari, Dan akan selalu diingat sebagai pengecut...Tamat')
'''
