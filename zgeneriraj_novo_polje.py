def po_ugibanju_nemine(slovar_ugibov_nemin, seznam_ugibov_min, stevilo_min):
    pravilni_ugibi_nemin =[]
    for polje in slovar_ugibov_nemin:
        pravilni_ugibi_nemin.append(polje)
    rezultat = f'''% rebase('osnova.html')\n<h1>Število preostalih min: {stevilo_min}</h1>\n<table>'''
    for i in range(10):
        rezultat += '\n    <tr>'
        for j in range(10):
            if (i,j) in pravilni_ugibi_nemin:
                stevilo = slovar_ugibov_nemin[(i,j)]
                slovar_linkov_stevil = {0:'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Minesweeper_0.svg/1024px-Minesweeper_0.svg.png',
                        1:'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Minesweeper_1.svg/1200px-Minesweeper_1.svg.png',
                        2:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Minesweeper_2.svg/1200px-Minesweeper_2.svg.png',
                        3:'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Minesweeper_3.svg/1200px-Minesweeper_3.svg.png',
                        4:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Minesweeper_4.svg/1200px-Minesweeper_4.svg.png',
                        5:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Minesweeper_5.svg/1200px-Minesweeper_5.svg.png',
                        6:'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Minesweeper_6.svg/1200px-Minesweeper_6.svg.png',
                        7:'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Minesweeper_7.svg/600px-Minesweeper_7.svg.png',
                        8:'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Minesweeper_8.svg/1200px-Minesweeper_8.svg.png'}
                rezultat += f'''\n        <th><img src='{slovar_linkov_stevil[stevilo]}'' alt='stevilka' id='stevilke'></th>'''
            elif (i,j) in seznam_ugibov_min:
                rezultat += f'''\n        <th><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Minesweeper_flag.svg/1200px-Minesweeper_flag.svg.png' alt='Zastavica' id='zas'></th>'''
            else:
                rezultat += f'''\n        <th><form action='/odlocitev/{(i,j)}/'><input type="submit" id='{(i,j)}' value=''></form></th>'''
        rezultat += '\n    </tr>'
    rezultat += '''\n</table>\n\n<form action='/zacetna_stran/', method="POST", id='igra'>\n    <input type='submit' value='Vrni na začetno stran' id='vrni' style="font-size : 20px">\n</form>'''
    return rezultat

def prepisi_v_datoteko(slovar_ugibov_nemin, seznam_ugibov_min, stevilo_min):
    datoteka = open('tabela.html', 'w', encoding='utf-8')
    n = datoteka.write(po_ugibanju_nemine(slovar_ugibov_nemin,seznam_ugibov_min, stevilo_min))
    datoteka.close()
