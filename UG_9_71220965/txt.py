import random
welcoming_txt = '''dunia ini telah dipenuhi monster dan manusia sudah hampir putus harapan, 
apakah kedatangan mu disini adalah sebuah kebetulan atau harapan bagi umat manusia?
'''
kelas = {
    'Warrior':{'kelas':'','hp':100,'dmg':5,'turn':2},
    'Mage':{'kelas':'','hp':80,'dmg':8,'turn':3},
    'Tank':{'kelas':'','hp':200,'dmg':3,'turn':4},
    'Archer':{'kelas':'','hp':70,'dmg':4,'turn':1}
}

monster = {
    'Slime':{'hp':20,'dmg':2,'turn':1},
    'Goblin':{'hp':40,'dmg':5,'turn':2},
    'Werewolf':{'hp':30,'dmg':7,'turn':2},
    'Demon':{'hp':60,'dmg':6,'turn':4},
}

performa = {
    'Total Damage Yang Diberikan':0,
    'Total Damage Yang Diterima':0,
    'Jumlah Menyerang':0
}

txt_reputasi = [['Kamu Kalah Dan Telah Mengecewakan Mereka Yang Menaruh Harapan Padamu','Pernah Dengar Dengan Yang Namanya Kerja Keras?','Lah Kok Kalah :v'],['Kamu Kalah Namun Perjuangan Mu Dihargai', 'Terima Kasih Karena Sudah Mencoba Berjuang Menyelamatkan Dunia Ini.'],['Kamu Telah Berbuat Cukup, Kamu Akan Diingat Sebagai Legenda', 'Perjuangan Mu Akan Diteruskan Oleh Mereka Yang Tergerak Oleh Mu']]



def status(pilihan):
    global kelas
    if kelas[pilihan]['kelas'] == '':
        kalimat = f"Kamu Merupakan Seorang {pilihan}, Berikut Adalah Status Mu:\n"
        status = '\n'.join(f'{stat.upper()}: {kelas[pilihan][stat]}' for stat in kelas[pilihan] if kelas[pilihan][stat] != '')
        kelas[pilihan]['kelas'] = pilihan
    else:
        kalimat = f'STATUS:\n'
        status = '\n'.join(f'{stat.upper()}: {kelas[pilihan][stat]}' for stat in kelas[pilihan] if kelas[pilihan][stat] != '')
    return f'{kalimat}{status}\n'


