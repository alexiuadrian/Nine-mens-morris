import time

import pygame
import sys

from pygame.time import Clock

ADANCIME_MAX = 6

# Functia verifica toate posibilitatile de formare de moara
def forms_mill(position, matr, jucator):
    if position[0] == 0 and position[1] == 0:
        if matr[0][3] == jucator and matr[0][6] == jucator:
            return True
        if matr[3][0] == jucator and matr[6][0] == jucator:
            return True
            
    if position[0] == 0 and position[1] == 3:
        if matr[0][0] == jucator and matr[0][6] == jucator:
            return True
        if matr[1][3] == jucator and matr[2][3] == jucator:
            return True 

    if position[0] == 0 and position[1] == 6:
        if matr[0][0] == jucator and matr[0][3] == jucator:
            return True
        if matr[3][6] == jucator and matr[6][6] == jucator:
            return True


    if position[0] == 1 and position[1] == 1:
        if matr[1][3] == jucator and matr[1][5] == jucator:
            return True
        if matr[3][1] == jucator and matr[5][1] == jucator:
            return True

    if position[0] == 1 and position[1] == 3:
        if matr[1][1] == jucator and matr[1][5] == jucator:
            return True
        if matr[0][3] == jucator and matr[2][3] == jucator:
            return True

    if position[0] == 1 and position[1] == 5:
        if matr[1][0] == jucator and matr[1][3] == jucator:
            return True
        if matr[3][5] == jucator and matr[5][5] == jucator:
            return True


    if position[0] == 2 and position[1] == 2:
        if matr[2][3] == jucator and matr[2][4] == jucator:
            return True
        if matr[3][2] == jucator and matr[4][2] == jucator:
            return True
    
    if position[0] == 2 and position[1] == 3:
        if matr[2][2] == jucator and matr[2][4] == jucator:
            return True
        if matr[1][3] == jucator and matr[0][3] == jucator:
            return True

    if position[0] == 2 and position[1] == 4:
        if matr[2][2] == jucator and matr[2][3] == jucator:
            return True
        if matr[3][4] == jucator and matr[4][4] == jucator:
            return True


    if position[0] == 3 and position[1] == 0:
        if matr[3][1] == jucator and matr[3][2] == jucator:
            return True
        if matr[0][0] == jucator and matr[6][0] == jucator:
            return True

    if position[0] == 3 and position[1] == 1:
        if matr[3][0] == jucator and matr[3][2] == jucator:
            return True
        if matr[1][1] == jucator and matr[5][1] == jucator:
            return True

    if position[0] == 3 and position[1] == 2:
        if matr[3][0] == jucator and matr[3][1] == jucator:
            return True
        if matr[2][2] == jucator and matr[4][2] == jucator:
            return True
    
    if position[0] == 3 and position[1] == 4:
        if matr[3][5] == jucator and matr[3][6] == jucator:
            return True
        if matr[2][4] == jucator and matr[4][4] == jucator:
            return True
    
    if position[0] == 3 and position[1] == 5:
        if matr[3][4] == jucator and matr[3][6] == jucator:
            return True
        if matr[1][5] == jucator and matr[5][5] == jucator:
            return True
    
    if position[0] == 3 and position[1] == 6:
        if matr[3][4] == jucator and matr[3][5] == jucator:
            return True
        if matr[0][6] == jucator and matr[6][6] == jucator:
            return True

    
    if position[0] == 4 and position[1] == 2:
        if matr[4][3] == jucator and matr[4][4] == jucator:
            return True
        if matr[3][3] == jucator and matr[2][3] == jucator:
            return True
    
    if position[0] == 4 and position[1] == 3:
        if matr[4][2] == jucator and matr[4][4] == jucator:
            return True
        if matr[5][3] == jucator and matr[6][3] == jucator:
            return True
    
    if position[0] == 4 and position[1] == 4:
        if matr[4][2] == jucator and matr[4][3] == jucator:
            return True
        if matr[3][4] == jucator and matr[2][4] == jucator:
            return True


    if position[0] == 5 and position[1] == 1:
        if matr[5][3] == jucator and matr[5][5] == jucator:
            return True
        if matr[3][1] == jucator and matr[1][1] == jucator:
            return True

    if position[0] == 5 and position[1] == 3:
        if matr[5][1] == jucator and matr[5][5] == jucator:
            return True
        if matr[5][3] == jucator and matr[5][6] == jucator:
            return True

    if position[0] == 5 and position[1] == 5:
        if matr[5][1] == jucator and matr[5][3] == jucator:
            return True
        if matr[5][4] == jucator and matr[5][6] == jucator:
            return True
    

    if position[0] == 6 and position[1] == 0:
        if matr[6][3] == jucator and matr[6][6] == jucator:
            return True
        if matr[3][0] == jucator and matr[0][0] == jucator:
            return True

# Aceasta functie va returna o lista cu toate mutarile valide a unui jucator
# inainte ca acesta sa termine de asezat toate piesele pe tabla
def mutari_valide_faza_1(jucator, matr):
    mutari = []

    for line in range(len(matr)):
        for column in range(len(matr[line])):
            if matr[line][column] == '#':
                mutari.append((line, column))
    
    return mutari
    
# Aceasta functie va returna o lista cu toate mutarile valide ale unei piese
# dupa ce au fost asezate toate pe tabla
def mutari_valide_faza_2(poz, matr, jucator):
    mutari_valide = []
    
    if poz[0] < -1 or poz[0] > len(matr[0] - 1) or poz[1] < -1 or poz[1] > len(matr[0] - 1):
        return False
    
    # In aceasta lista adaug toti vecinii piesei
    mutari = [(poz[0] - 1, poz[1] - 1), (poz[0] - 1, poz[1]), (poz[0] - 1, poz[1] + 1), (poz[0], poz[1] + 1),
              (poz[0] + 1, poz[1] + 1), (poz[0] + 1, poz[1]), (poz[0] + 1, poz[1] - 1), (poz[0], poz[1] - 1)]

    # Verific daca acesti vecini pot fi mutari valide
    for possible_move in mutari:
        if matr[possible_move[0]][possible_move[1]] == '#':
            mutari_valide.append(possible_move)

    return mutari

def elem_identice(lista):
    if (all(elem == lista[0] for elem in lista[1:])):
        return lista[0] if lista[0] != Joc.GOL else False
    return False

# Functia va fi folosita pentru a verifica daca user-ul a dat click
# intr-unul din cercuri
def is_in_circle(point, center):
        for line in range(center[1] - 10, center[1] + 10):
            for column in range(center[0] - 10, center[0] + 10):
                if column == point[0] and line == point[1]:
                    return True
        
        return False

class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    NR_COLOANE = 3
    JMIN = None
    JMAX = None
    GOL = '#'
    PIESE_JMIN = 9
    PIESE_JMAX = 9
    PIESE_PE_TABLA_JMIN = 0
    PIESE_PE_TABLA_JMAX = 0

    @classmethod
    def initializeaza(cls, display, NR_COLOANE=3, dim_celula=40):
        cls.display = display
        cls.dim_celula = dim_celula
        cls.x_img = pygame.image.load('white.png')
        cls.x_img = pygame.transform.scale(cls.x_img, (dim_celula, dim_celula))
        cls.zero_img = pygame.image.load('black.png')
        cls.zero_img = pygame.transform.scale(cls.zero_img, (dim_celula, dim_celula))
        cls.background_image = pygame.image.load("background.png").convert()

        cls.celuleGrid = [(30, 30), (300, 30), (570, 30), (123, 122), (300, 122), (477, 122), (214, 215), (300, 215), (386, 215), 
        (30, 300), (123, 300), (214, 300), (386, 300), (477, 300), (570, 300), (214, 385), (300, 385), (386, 385), (123, 478), (300, 478), (477, 478), (30, 570),
        (300, 570), (570, 570)]  # este lista cu cercurile din colturi

        for linie in range(NR_COLOANE):
            for coloana in range(NR_COLOANE):
                patr = pygame.Rect(coloana * (dim_celula + 1), linie * (dim_celula + 1), dim_celula, dim_celula)
                cls.celuleGrid.append(patr)

    def deseneaza_grid(self, marcaj=None):  # tabla de exemplu este ["#","x","#","0",......]

        for ind in range(len(self.matr)):
            linie = ind // 3  # // inseamna div
            coloana = ind % 3

            if marcaj == ind:
                # daca am o patratica selectata, o desenez cu rosu
                culoare = (255, 0, 0)
            else:
                # altfel o desenez cu alb
                culoare = (255, 255, 255)

            #pygame.draw.rect(self.__class__.display, culoare, self.__class__.celuleGrid[ind])  # alb = (255,255,255)

            self.__class__.display.blit(self.background_image, [0, 0])

            pygame.draw.circle(self.__class__.display, (0, 0, 0), (30, 30), 10)

            pygame.draw.circle(self.__class__.display, (0, 0, 0), (300, 30), 10)

            pygame.draw.circle(self.__class__.display, (0, 0, 0), (570, 30), 10)


            pygame.draw.circle(self.__class__.display, (0, 0, 0), (123, 122), 10)

            pygame.draw.circle(self.__class__.display, (0, 0, 0), (300, 122), 10)

            pygame.draw.circle(self.__class__.display, (0, 0, 0), (477, 122), 10)


            pygame.draw.circle(self.__class__.display, (0, 0, 0), (214, 215), 10)

            pygame.draw.circle(self.__class__.display, (0, 0, 0), (300, 215), 10)

            pygame.draw.circle(self.__class__.display, (0, 0, 0), (386, 215), 10)


            pygame.draw.circle(self.__class__.display, (0, 0, 0), (30, 300), 10)

            pygame.draw.circle(self.__class__.display, (0, 0, 0), (123, 300), 10)

            pygame.draw.circle(self.__class__.display, (0, 0, 0), (214, 300), 10)

            pygame.draw.circle(self.__class__.display, (0, 0, 0), (386, 300), 10)

            pygame.draw.circle(self.__class__.display, (0, 0, 0), (477, 300), 10)

            pygame.draw.circle(self.__class__.display, (0, 0, 0), (570, 300), 10)


            pygame.draw.circle(self.__class__.display, (0, 0, 0), (123, 478), 10)

            pygame.draw.circle(self.__class__.display, (0, 0, 0), (300, 478), 10)

            pygame.draw.circle(self.__class__.display, (0, 0, 0), (477, 478), 10)


            pygame.draw.circle(self.__class__.display, (0, 0, 0), (30, 570), 10)

            pygame.draw.circle(self.__class__.display, (0, 0, 0), (300, 570), 10)

            pygame.draw.circle(self.__class__.display, (0, 0, 0), (570, 570), 10)

            if self.matr[ind] == 'x':
                self.__class__.display.blit(self.__class__.x_img, (
                30, 30))
            elif self.matr[ind] == '0':
                self.__class__.display.blit(self.__class__.zero_img, (
                300, 30))
        pygame.display.flip()  # obligatoriu pentru a actualiza interfata (desenul)

    # pygame.display.update()

    def __init__(self, tabla=None):
        self.matr = tabla or [self.__class__.GOL] * 9
        if tabla != None:
            self.matr = tabla
        else:
            self.matr = [['#', '-', '-', '#', '-', '-', '#'],
                         ['-', '#', '-', '#', '-', '#', '-'],
                         ['-', '-', '#', '#', '#', '-', '-'],
                         ['#', '#', '#', '-', '#', '#', '#'],
                         ['-', '-', '#', '#', '#', '-', '-'],
                         ['-', '#', '-', '#', '-', '#', '-'],
                         ['#', '-', '-', '#', '-', '-', '#']]

    @classmethod
    def jucator_opus(cls, jucator):
        return cls.JMAX if jucator == cls.JMIN else cls.JMIN

    def final(self):

        # rez = (elem_identice([self.matr[0][0], self.matr[0][3], self.matr[0][6]])
        #        or elem_identice([self.matr[0][0], self.matr[3][0], self.matr[6][0]])
        #        or elem_identice([self.matr[6][0], self.matr[6][3], self.matr[6][6]])
        #        or elem_identice([self.matr[0][6], self.matr[3][6], self.matr[6][6]])
        #        or elem_identice([self.matr[1][1], self.matr[1][3], self.matr[1][5]])
        #        or elem_identice([self.matr[1][5], self.matr[3][5], self.matr[5][5]])
        #        or elem_identice([self.matr[5][1], self.matr[5][3], self.matr[5][5]])
        #        or elem_identice([self.matr[1][1], self.matr[3][1], self.matr[5][1]])
        #        or elem_identice([self.matr[2][2], self.matr[2][3], self.matr[2][4]])
        #        or elem_identice([self.matr[2][4], self.matr[3][4], self.matr[4][4]])
        #        or elem_identice([self.matr[4][4], self.matr[4][3], self.matr[4][2]])
        #        or elem_identice([self.matr[2][2], self.matr[3][2], self.matr[4][2]])
        #        or elem_identice([self.matr[0][3], self.matr[1][3], self.matr[2][3]])
        #        or elem_identice([self.matr[3][4], self.matr[3][5], self.matr[3][6]])
        #        or elem_identice([self.matr[4][3], self.matr[5][3], self.matr[6][3]])
        #        or elem_identice([self.matr[3][0], self.matr[3][1], self.matr[3][2]])) 



        if self.PIESE_JMIN <= 2:
            return self.JMAX
        elif self.PIESE_JMAX <= 2:
            return self.JMIN
        else:
            return False

    def mutari(self, jucator_opus):
        l_mutari = []

        if self.PIESE_PE_TABLA_JMAX < 8:
            for i in range(len(self.matr)):
                if self.matr[i] == '#':
                    matr_tabla_noua = list(self.matr)
                    matr_tabla_noua[i] = jucator_opus
                    self.PIESE_PE_TABLA_JMAX += 1
                    l_mutari.append(Joc(matr_tabla_noua))
        else:
            for line in range(len(self.matr[0])):
                for column in range(len(self.matr[line])):
                    if self.matr[line][column] == jucator_opus:
                        mutari_posibile = mutari_valide_faza_2((line, column), self.matr)

                        for position in mutari_posibile:
                            matr_tabla_noua = list(self.matr)
                            matr_tabla_noua[position[0] * 7 + position[1]] = jucator_opus
                            # Verifica daca se formeaza o moara apeland forms_mill(position, self.matr, jucator_opus)
                            # Daca se formeaza, genereaza toate mutarile posibile fara o piesa din cealalta culoare
                            if forms_mill(position, self.matr, jucator_opus):
                                for index in range(len(matr_tabla_noua)):
                                    if jucator_opus == 'A':
                                        if matr_tabla_noua[index] == 'N':
                                            matr_tabla_noua_1 = list(matr_tabla_noua)
                                            matr_tabla_noua_1[index] = '#'
                                            self.PIESE_JMIN -= 1
                                            
                                            l_mutari.append(Joc(matr_tabla_noua_1))
                                    elif jucator_opus == 'N':
                                        if matr_tabla_noua[index] == 'A':
                                            matr_tabla_noua_1 = list(matr_tabla_noua)
                                            matr_tabla_noua_1[index] = '#'
                                            self.PIESE_JMIN -= 1

                                            l_mutari.append(Joc(matr_tabla_noua_1))

        return l_mutari

    # linie deschisa inseamna linie pe care jucatorul mai poate forma o configuratie castigatoare
    # practic e o linie fara simboluri ale jucatorului opus
    def linie_deschisa(self, lista, jucator):
        jo = self.jucator_opus(jucator)
        # verific daca pe linia data nu am simbolul jucatorului opus
        if not jo in lista:
            return 1
        return 0

    def linii_deschise(self, jucator):

        return (self.linie_deschisa([self.matr[0][0], self.matr[0][3], self.matr[0][6]], jucator)
                or self.linie_deschisa([self.matr[0][0], self.matr[3][0], self.matr[6][0]], jucator)
                or self.linie_deschisa([self.matr[6][0], self.matr[6][3], self.matr[6][6]], jucator)
                or self.linie_deschisa([self.matr[0][6], self.matr[3][6], self.matr[6][6]], jucator)
                or self.linie_deschisa([self.matr[1][1], self.matr[1][3], self.matr[1][5]], jucator)
                or self.linie_deschisa([self.matr[1][5], self.matr[3][5], self.matr[5][5]], jucator)
                or self.linie_deschisa([self.matr[5][1], self.matr[5][3], self.matr[5][5]], jucator)
                or self.linie_deschisa([self.matr[1][1], self.matr[3][1], self.matr[5][1]], jucator)
                or self.linie_deschisa([self.matr[2][2], self.matr[2][3], self.matr[2][4]], jucator)
                or self.linie_deschisa([self.matr[2][4], self.matr[3][4], self.matr[4][4]], jucator)
                or self.linie_deschisa([self.matr[4][4], self.matr[4][3], self.matr[4][2]], jucator)
                or self.linie_deschisa([self.matr[2][2], self.matr[3][2], self.matr[4][2]], jucator)
                or self.linie_deschisa([self.matr[0][3], self.matr[1][3], self.matr[2][3]], jucator)
                or self.linie_deschisa([self.matr[3][4], self.matr[3][5], self.matr[3][6]], jucator)
                or self.linie_deschisa([self.matr[4][3], self.matr[5][3], self.matr[6][3]], jucator)
                or self.linie_deschisa([self.matr[3][0], self.matr[3][1], self.matr[3][2]], jucator))

    def estimeaza_scor(self, adancime):
        t_final = self.final()
        if t_final == self.__class__.JMAX:
            return (99 + adancime)
        elif t_final == self.__class__.JMIN:
            return (-99 - adancime)
        elif t_final == 'remiza':
            return 0
        else:
            return (self.linii_deschise(self.__class__.JMAX) - self.linii_deschise(self.__class__.JMIN))

    def __str__(self):
        sir = ""

        for l in range(len(self.matr[0])):
            for c in range(len(self.matr[l])):
                sir = sir + str(self.matr[l][c]) + " "
        
            sir = sir + "\n"

        return sir


class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari() care ofera lista cu configuratiile posibile in urma mutarii unui jucator
    """

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, estimare=None):
        self.tabla_joc = tabla_joc
        self.j_curent = j_curent

        # adancimea in arborele de stari
        self.adancime = adancime

        # estimarea favorabilitatii starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
        self.estimare = estimare

        # lista de mutari posibile din starea curenta
        self.mutari_posibile = []

        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa = None

    def mutari(self):
        l_mutari = self.tabla_joc.mutari(self.j_curent)
        juc_opus = Joc.jucator_opus(self.j_curent)
        l_stari_mutari = [Stare(mutare, juc_opus, self.adancime - 1, parinte=self) for mutare in l_mutari]

        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Jucator curent:" + self.j_curent + ")\n"
        return sir


""" Algoritmul MinMax """


def min_max(stare):
    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.estimare = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    # calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari()
    print(len(stare.mutari_posibile))

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutariCuEstimare = [min_max(mutare) for mutare in stare.mutari_posibile]

    if stare.j_curent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu estimarea maxima
        stare.stare_aleasa = max(mutariCuEstimare, key=lambda x: x.estimare)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu estimarea minima
        stare.stare_aleasa = min(mutariCuEstimare, key=lambda x: x.estimare)
    stare.estimare = stare.stare_aleasa.estimare
    return stare


def alpha_beta(alpha, beta, stare):
    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.estimare = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    if alpha > beta:
        return stare  # este intr-un interval invalid deci nu o mai procesez

    stare.mutari_posibile = stare.mutari()

    if stare.j_curent == Joc.JMAX:
        estimare_curenta = float('-inf')

        for mutare in stare.mutari_posibile:
            # calculeaza estimarea pentru starea noua, realizand subarborele
            stare_noua = alpha_beta(alpha, beta, mutare)

            if (estimare_curenta < stare_noua.estimare):
                stare.stare_aleasa = stare_noua
                estimare_curenta = stare_noua.estimare
            if (alpha < stare_noua.estimare):
                alpha = stare_noua.estimare
                if alpha >= beta:
                    break

    elif stare.j_curent == Joc.JMIN:
        estimare_curenta = float('inf')

        for mutare in stare.mutari_posibile:

            stare_noua = alpha_beta(alpha, beta, mutare)

            if (estimare_curenta > stare_noua.estimare):
                stare.stare_aleasa = stare_noua
                estimare_curenta = stare_noua.estimare

            if (beta > stare_noua.estimare):
                beta = stare_noua.estimare
                if alpha >= beta:
                    break
    stare.estimare = stare.stare_aleasa.estimare

    return stare


def afis_daca_final(stare_curenta):
    final = stare_curenta.tabla_joc.final()
    if (final):
        if final == "A":
            print("Albul a castigat!")
        elif final == "N":
            print("Negrul a castigat!")

        return True

    return False


def main():
    # initializare algoritm
    raspuns_valid = False
    while not raspuns_valid:
        tip_algoritm = input("Algorimul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n ")
        if tip_algoritm in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")
    # initializare jucatori
    raspuns_valid = False
    while not raspuns_valid:
        Joc.JMIN = input("Doriti sa jucati cu Alb (scrieti A) sau cu Negru (scrieti N)? ").upper()
        if (Joc.JMIN in ['A', 'N']):
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie A sau N.")
    Joc.JMAX = 'N' if Joc.JMIN == 'A' else 'A'

    dificultate = 3
   # alegere dificultate
    raspuns_valid = False
    while not raspuns_valid:
        dificultate = input("Selectati dificultatea adversarului. \n 1. Usor\n 2. Mediu\n 3. Greu\n")
        if tip_algoritm in ['1', '2', '3']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")

    if dificultate == '1':
        ADANCIME_MAX = 2
    elif dificultate == '2':
        ADANCIME_MAX = 4
    else:
        ADANCIME_MAX = 6

    # initializare tabla
    tabla_curenta = Joc()
    print("Tabla initiala")
    print(str(tabla_curenta))

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, 'A', ADANCIME_MAX)

    print(stare_curenta.j_curent)
    print(Joc.JMIN)

    # setari interf grafica
    pygame.init()
    pygame.display.set_caption("Alexiu Adrian - Nine Men's Morris")
    # dimensiunea ferestrei in pixeli
    ecran = pygame.display.set_mode(size=(602, 602))  # N *100+ N-1
    Joc.initializeaza(ecran)

    de_mutat = False
    tabla_curenta.deseneaza_grid()
    while True:

        if (stare_curenta.j_curent == Joc.JMIN):
            # muta jucatorul
            # [MOUSEBUTTONDOWN, MOUSEMOTION,....]
            # l=pygame.event.get()

            

            if Joc.PIESE_PE_TABLA_JMIN < 8:
                raspuns_valid=False
                while not raspuns_valid:
                    try:
                        linie=int(input("linie="))
                        coloana=int(input("coloana="))
                    
                        if (linie in range(7) and coloana in range(7)):
                            if stare_curenta.tabla_joc.matr[linie][coloana] == '#':
                                raspuns_valid=True
                            else:
                                print("Exista deja un simbol in pozitia ceruta.")
                        else:
                            print("Linie sau coloana invalida (trebuie sa fie unul dintre numerele [0..7]).")
                
                    except ValueError:
                        print("Linia si coloana trebuie sa fie numere intregi")

                stare_curenta.tabla_joc.matr[linie][coloana] = Joc.JMIN
                Joc.PIESE_PE_TABLA_JMIN += 1
            # else:
            #     try:
            #         print("Muta o piesa: ")
            #         linie=int(input("linie="))
            #         coloana=int(input("coloana="))
                
            #         if (linie in range(Joc.NR_COLOANE) and coloana in range(Joc.NR_COLOANE)):
            #             if stare_curenta.tabla_joc.matr[linie * 7 + coloana] == Joc.GOL:					
            #                 raspuns_valid=True
            #             else:
            #                 print("Exista deja un simbol in pozitia ceruta.")
            #         else:
            #             print("Linie sau coloana invalida (trebuie sa fie unul dintre numerele [0..7]).")
                
            #     except ValueError:
            #         print("Linia si coloana trebuie sa fie numere intregi")

            # afisarea starii jocului in urma mutarii utilizatorului
            print("\nTabla dupa mutarea jucatorului")
            print(str(stare_curenta))

            stare_curenta.tabla_joc.deseneaza_grid()
            # testez daca jocul a ajuns intr-o stare finala
            # si afisez un mesaj corespunzator in caz ca da
            if (afis_daca_final(stare_curenta)):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = Joc.jucator_opus(stare_curenta.j_curent)

            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()  # inchide fereastra
            #         sys.exit()
            #     elif event.type == pygame.MOUSEBUTTONDOWN:

            #         pos = pygame.mouse.get_pos()  # coordonatele clickului


            #         '''
            #         Aici de verificat unde se apasa!
            #         '''

            #         for circle in Joc.celuleGrid:
            #             if is_in_circle(pos, circle):
            #                 pygame.draw.circle(ecran, (255, 255, 255), (circle[0], circle[1]), 15)

            #         for np in range(len(Joc.celuleGrid)):

            #             if Joc.celuleGrid[np].collidepoint(
            #                     pos):  # verifica daca punctul cu coord pos se afla in dreptunghi(celula)
            #                 linie = np // 3
            #                 coloana = np % 3
            #                 ###############################
            #                 if stare_curenta.tabla_joc.matr[np] == Joc.JMIN:
            #                     if (de_mutat and linie == de_mutat[0] and coloana == de_mutat[1]):
            #                         # daca am facut click chiar pe patratica selectata, o deselectez
            #                         de_mutat = False
            #                         stare_curenta.tabla_joc.deseneaza_grid()
            #                     else:
            #                         de_mutat = (linie, coloana)
            #                         # desenez gridul cu patratelul marcat
            #                         stare_curenta.tabla_joc.deseneaza_grid(np)
            #                 if stare_curenta.tabla_joc.matr[np] == Joc.GOL:
            #                     if de_mutat:
            #                         #### eventuale teste legate de mutarea simbolului
            #                         stare_curenta.tabla_joc.matr[de_mutat[0] * 7 + de_mutat[1]] = Joc.GOL
            #                         de_mutat = False
            #                     # plasez simbolul pe "tabla de joc"
            #                     stare_curenta.tabla_joc.matr[linie * 7 + coloana] = Joc.JMIN

            #                     # afisarea starii jocului in urma mutarii utilizatorului
            #                     print("\nTabla dupa mutarea jucatorului")
            #                     print(str(stare_curenta))

            #                     stare_curenta.tabla_joc.deseneaza_grid()
            #                     # testez daca jocul a ajuns intr-o stare finala
            #                     # si afisez un mesaj corespunzator in caz ca da
            #                     if (afis_daca_final(stare_curenta)):
            #                         break

            #                     # S-a realizat o mutare. Schimb jucatorul cu cel opus
            #                     stare_curenta.j_curent = Joc.jucator_opus(stare_curenta.j_curent)


        # --------------------------------
        else:  # jucatorul e JMAX (calculatorul)
            # Mutare calculator

            # preiau timpul in milisecunde de dinainte de mutare
            t_inainte = int(round(time.time() * 1000))
            if tip_algoritm == '1':
                stare_actualizata = min_max(stare_curenta)
            else:  # tip_algoritm==2
                stare_actualizata = alpha_beta(-500, 500, stare_curenta)
            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta))

            stare_curenta.tabla_joc.deseneaza_grid()
            # preiau timpul in milisecunde de dupa mutare
            t_dupa = int(round(time.time() * 1000))
            print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")

            if (afis_daca_final(stare_curenta)):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = Joc.jucator_opus(stare_curenta.j_curent)


if __name__ == "__main__":
    main()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
