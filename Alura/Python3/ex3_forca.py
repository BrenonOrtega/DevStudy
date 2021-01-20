
def jogar():
    msg = "Bem vindo ao jogo de forca"
    msg_espacamento = "**************************************"

    print(msg_espacamento)
    print(msg)
    print(msg_espacamento,"\n")

    #inicio do jogo
    palavra_secreta = "banana"
    acertou = False
    enforcado = False

    num_letras_palavra_secreta = len(palavra_secreta)
    tentativas = len(palavra_secreta)
    segredo = []
    for i in range (num_letras_palavra_secreta):
        segredo.append("_")

    while (not acertou and not enforcado):
        print('Palavra Secreta:'," ".join(map(str, segredo)))
        letra_digitada = input("digite uma letra:")
        letra_digitada = letra_digitada.strip()
        
        if len(letra_digitada) == 1:    
            index_letra = 0 
            acerto = False
            for letra in palavra_secreta:
                if letra_digitada.upper == letra.upper:
                    print (f"Encontrei a letra {letra_digitada} na posição {index_letra} da palavra")
                    segredo[index_letra] = letra_digitada
                    acerto = True
                index_letra += 1

            print("jogando...")
        else:
            print("digite apenas uma única letra.")

        if acerto == False:
            print("Menos uma tentativa")
            

print("Fim do jogo")

if __name__ == "__main__":
    jogar()
