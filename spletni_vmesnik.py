import bottle
import model
import zgeneriraj_novo_polje


@bottle.get('/')
def zacetna_stran():
    return bottle.template('zacetna_stran.html')

@bottle.post('/nova_igra/')
def nova_igra():
    global igra1 
    igra1= model.nova_igra()
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def igra():
    global igra1 
    igra1= model.nova_igra()
    return bottle.template('igra.html')

@bottle.post('/zacetna_stran/')
def vrni_na_zacetno_stran():
    bottle.redirect('/')

@bottle.get('/odlocitev/<polje>/')
def odlocitev(polje):
    global polje1
    polje1 = polje
    return bottle.template('odlocitev.html')

@bottle.get('/ugibanje_nemine/')
def ugibanje_nemine():
    if polje1[0] not in range(10):
        vrstica = int(polje1[1])
        stolpec = int(polje1[4])
    else:
        vrstica = polje1[0]
        stolpec = polje1[1]
    polje = (vrstica, stolpec)
    trenuten_rezultat = igra1.ugibaj_nemino(polje)
    if trenuten_rezultat == 'p':
        slovar = igra1.slovar_ugibov_nemin
        stevilo_min = igra1.stevilo_preostalih_min()
        seznam = igra1.ugibi_min
        zgeneriraj_novo_polje.prepisi_v_datoteko(slovar, seznam, stevilo_min)
        return bottle.template('tabela.html')
    else:
        return bottle.template('poraz.html')


@bottle.get('/ugibanje_mine/')
def ugibanje_mine():
    if polje1[0] not in range(10):
        vrstica = int(polje1[1])
        stolpec = int(polje1[4])
    else:
        vrstica = polje1[0]
        stolpec = polje1[1]
    polje = (vrstica, stolpec)
    trenuten_rezultat = igra1.ugibaj_mino(polje)
    if trenuten_rezultat == 'w':
        print(trenuten_rezultat)
        return bottle.template('zmaga.html')
    else:
        seznam = igra1.ugibi_min
        slovar = igra1.slovar_ugibov_nemin
        stevilo_min = igra1.stevilo_preostalih_min()
        zgeneriraj_novo_polje.prepisi_v_datoteko(slovar, seznam,stevilo_min)
        return bottle.template('tabela.html')
       

bottle.run(debug=True, reloader=True)