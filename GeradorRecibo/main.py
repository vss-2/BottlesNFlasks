import json, flask, os

def adcNome(nome):
        # Aqui vai o código que adiciona ao JSON o nome
        with open('lista.json') as jsonfile:
                
        return

if __name__ == "__main__":
        print('OBS: Digite -1 quando quiser parar de adicionar')
        novoNome = ''
        while novoNome != '-1':
                novoNome = input('Insira qual nome quer adicionar a lista dos formulários: ')
                adcNome(novoNome)
        exit()
