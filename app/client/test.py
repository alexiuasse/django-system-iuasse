class AnimalEstatico(object):

    # init estatico
    def __init__(self):
        self.windelimarcos = 'macaco'


class AnimalDinamico(object):

    # init dinamico
    def __init__(self, windelimarcos):
        self.windelimarcos = windelimarcos


class AnimalDinamicoNArgs(object):

    # init dinamico com n parametros
    def __init__(self, **kwargs):
        self.windelimarcos = kwargs['windelimarcos']
        self.sushi = kwargs['sushi']


# estatico
lista_estatico = []

for i in range(3):
    lista_estatico.append(AnimalEstatico().__dict__)

print(f"Lista com objeto estatico {lista_estatico}")

# dinamico
lista_dinamico = []

for i in range(3):
    lista_dinamico.append(AnimalDinamico('rinoceronte').__dict__)

print(f"Lista com objeto dinâmico {lista_dinamico}")


# dinamico n args
lista_dinamico_n_args = []

for i in range(3):
    lista_dinamico_n_args.append(AnimalDinamicoNArgs(
        windelimarcos='rinoceronte', sushi='leão').__dict__)

print(f"Lista com objeto dinâmico e n argumentos {lista_dinamico_n_args}")
