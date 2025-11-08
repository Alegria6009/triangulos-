import os
import time
import itertools

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def desenhar_triangulo(altura, char='*'):
    for i in range(1, altura + 1):
        espacos = altura - i
        estrelas = 2 * i - 1
        print(' ' * espacos + char * estrelas)

def animar(max_altura=12, fps=12):
    sequencia = list(range(1, max_altura + 1)) + list(range(max_altura - 1, 0, -1))
    try:
        for h in itertools.cycle(sequencia):
            limpar_tela()
            desenhar_triangulo(h, char='*')  # troque por '✦' ou '+' se quiser variar
            print("\nCtrl+C para parar")
            time.sleep(1 / fps)
    except KeyboardInterrupt:
        limpar_tela()
        print("Encerrado. 👍")

if __name__ == "__main__":
    animar(max_altura=12, fps=10)