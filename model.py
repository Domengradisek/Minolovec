ZMAGA = 'w'
PORAZ = 'x'
PRAVILEN_UGIB_MINE = '+'
NAPAČEN_UGIB_MINE = '-'
PRAVILEN_UGIB_PRAZNEGA_POLJA = 'p'

class Igra:

    def __init__(self, ugibi_min, ugibi_nemin, polja_z_minami):
        self.ugibi_min = ugibi_min
        self.ugibi_nemin = ugibi_nemin
        self.polja_z_minami = polja_z_minami

    def pravilni_ugibi_min(self):
        seznam = []
        for ugib in self.ugibi_min:
            if ugib in self.polja_z_minami:
                seznam.append(ugib)
        return seznam

    def pravilni_ugibi_nemin(self):
        seznam = []
        for ugib in self.ugibi_nemin:
            if ugib not in self.polja_z_minami:
                seznam.append(ugib)
        return seznam

    def napacni_ugibi_min(self):
        seznam = []
        for ugib in self.ugibi_min:
            if ugib not in self.polja_z_minami:
                seznam.append(ugib)
        return seznam

    def stevilo_preostalih_min(self):
        return len(self.polja_z_minami) - len(self.pravilni_ugibi_min()) - len(self.napacni_ugibi_min())

    def poraz(self):
        for ugib in self.ugibi_nemin:
            if ugib in self.polja_z_minami:
                return True
        else:
            return False

    def zmaga(self):
        return self.pravilni_ugibi_min() == self.polja_z_minami

    def ugibaj_mino(self, polje):
        self.ugibi_min.append(polje)
        if self.zmaga():
            return ZMAGA
        elif self.poraz():
            return PORAZ
        elif polje in self.polja_z_minami:
            return PRAVILEN_UGIB_MINE
        else:
            return NAPAČEN_UGIB_MINE

    def ugibaj_nemino(self, polje):
        self.ugibi_nemin.append(polje)
        if self.poraz():
            return PORAZ
        elif polje not in self.polja_z_minami:
            stevilo_okoliskih_min = self.prestej_okoliske_mine(polje)
            if stevilo_okoliskih_min > 0:
                return PRAVILEN_UGIB_PRAZNEGA_POLJA
            else:
                slovar_okoliskih_polj = self.pokazi_okoliska_polja(polje)
                for polje1 in slovar_okoliskih_polj:
                    if slovar_okoliskih_polj[polje1] > 0:
                        pass
                    else:
                        self.ugibaj_nemino(polje1)
                return PRAVILEN_UGIB_PRAZNEGA_POLJA



    def prestej_okoliske_mine(self, polje):
        vrstica = polje[0]
        stolpec = polje[1]
        stevilo_okoliskih_min = 0
        for i in [vrstica - 1, vrstica, vrstica + 1]:
            for j in [stolpec - 1, stolpec, stolpec + 1]:
                if (i,j) != polje and i in range(0,10) and j in range(0,10):
                    if (i,j) in self.polja_z_minami:
                        stevilo_okoliskih_min += 1
        return stevilo_okoliskih_min


    def pokazi_okoliska_polja(self, polje):
        vrstica = polje[0]
        stolpec = polje[1]
        slovar = {}
        for i in [vrstica - 1, vrstica, vrstica + 1]:
            for j in [stolpec - 1, stolpec, stolpec + 1]:
                if i in range(0,10) and j in range(0,10) and (i,j) != polje:
                    stevilo_min = self.prestej_okoliske_mine((i,j))
                    slovar[(i,j)] = stevilo_min
        return slovar

import random

def nakljucno_polje():
    i = random.randint(0,9)
    j = random.randint(0,9)
    return (i,j)

def nova_igra():
    ugibi_min = []
    ugibi_nemin = []
    polja_z_minami = []
    while len(polja_z_minami) < 10:
        if nakljucno_polje() not in polja_z_minami:
            polja_z_minami.append(nakljucno_polje())
    return Igra(ugibi_min, ugibi_nemin, polja_z_minami)