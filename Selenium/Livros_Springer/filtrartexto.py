if __name__ == "__main__":
        with open('texto_filter.txt') as linkfiles:
                tamanho = linkfiles.readlines()
                contador = 0
                print(tamanho[1])
                with open('output_texto_filter.txt','w+') as escritor:
                        for texto in tamanho:
                                if (contador%2 == 1):
                                        print(texto)
                                        escritor.write(texto)
                                contador += 1
