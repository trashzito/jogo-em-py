import random

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
    
    def __str__(self):
        return f"{self.valor} de {self.naipe}"

class Baralho:
    def __init__(self):
        self.cartas = []
        self.inicializar_baralho()

    def inicializar_baralho(self):
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        naipes = ['Espadas', 'Paus', 'Copas', 'Ouros']
        for naipe in naipes:
            for valor in valores:
                self.cartas.append(Carta(valor, naipe))

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir_cartas(self, num_cartas):
        return [self.cartas.pop() for _ in range(num_cartas)]

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def receber_carta(self, carta):
        self.mao.append(carta)

    def mostrar_mao(self):
        print(f"{self.nome} tem as seguintes cartas na mão:")
        for carta in self.mao:
            print(carta)

if __name__ == "__main__":
    baralho = Baralho()
    baralho.embaralhar()

    jogador1 = Jogador("Jogador 1")
    jogador2 = Jogador("Jogador 2")

    num_cartas_para_cada_jogador = 5

    cartas_para_jogador1 = baralho.distribuir_cartas(num_cartas_para_cada_jogador)
    cartas_para_jogador2 = baralho.distribuir_cartas(num_cartas_para_cada_jogador)

    for carta in cartas_para_jogador1:
        jogador1.receber_carta(carta)

    for carta in cartas_para_jogador2:
        jogador2.receber_carta(carta)

    jogador1.mostrar_mao()
    print()
    jogador2.mostrar_mao()