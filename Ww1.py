from random import randint
from time import sleep
c = ""
while c != "N":

    um = str(input("    -Está a fim de jogar?[S/N] ")).strip().upper()[0]
    if um == "N":
        break

    print("""   -Em um mundo devastado pela guerra, dois antigos inimigos se preparam para uma última batalha. 
    No Leste a União dos Estados Separatistas vem lutando a 20 anos pela liberdade e pela queda do regime ditadorial de Albatrox.""")

    sleep(2)

    print("=" * 20)

    c = str((input("    -Deseja continuar? [S/N] "))).strip().upper()[0]

    print("=" * 20)

    print('                                          |---------------------------------|                                                                                ')
    print('                                          |                                 |                                            ')
    print("                                          |                                 |                                              ")
    print("                                          |           |-------|             |                                                ")
    print("               ;)                         |           |       |             |                                              ")
    print("               -|-                        |           |       |             |                                           ")
    print("               /\                         |           |       |             |                            ")

    sleep(2)

    print("""   -O Reino de Albatrox, conhecido também como reino do Oeste, passou os últimos 20 anos tentando combater
    a União dos Estados Separatistas. Hoje essa batalha chegará ao fim! A União reuniu todo seu exército, em uma manobra 
    arriscada, rumo a capital de Albatrox: Lucius. """)

    sleep(6)

    print("=" * 20)

    print("""   -Caso a União vença a liberdade do mundo será mantida. Caso contrário ninguém poderá impedir que o 
    Império de Albatrox reconquiste as terras livres e, assim, comande o mundo inteiro!""")

    sleep(4)

    print("=" * 20)

    c = str((input("    -Deseja continuar? [S/N] "))).strip().upper()[0]

    print("=" * 20)

    sleep(2)

    confirm = ''

    while confirm != "S":
        classe = int(input("""    -Qual das classes abaixo será seu personagem:
        [0] Orc
        [1] Humano
        [2] Elfo
        [3] Anão
        (Essa é uma escolha importante, logo é melhor pensar antes de escolher): """))

        print("=" * 20)

        if classe == 0:

            classe = "Orc"

        elif classe == 1:

            classe = "Humano"

        elif classe == 2:

            classe = "Elfo"

        elif classe == 3:

            classe = "Anão"

        name = str(input("  -Digite o nome do personagem: "))


        confirm = str(input(f"  -Deseja confirmar a raça: {classe} e o nome: {name}?[S/N] ")).strip().upper()[0]

    sleep(2)

    print("=" * 20)


    print(f"    -Bem vindo {classe} chamado {name} ")

    sleep(4)

    print("=" * 20)

    guer = int(input("""   -Você está ao lado de bravos guerreiros e o General humano defensor das terras médias chamado Onofre 
    aparece para você e pergunta: 
    Você é um:
    [0] Guerreiro
    [1] Mago
    (Essa é uma escolha importante, logo é melhor pensar antes de escolher): """))

    if guer == 0:
        guer = "Guerreiro"
    elif guer == 1:
        guer = 'Mago'

    print("=" * 20)

    c = str((input("    -Deseja continuar? [S/N] "))).strip().upper()[0]


    sleep(3)

    print("=" * 20)

    print("""   -Você olha para frente e vê todo o exército aliado reunido atrás de 3 grandes montanhas.
    O inimigo está a apenas 3 dias de caminhada, bem atrás da terceira montanha """)

    print("=" * 20)


    continua = int(input("""   -O General olha para vocẽ e pergunta:
    Seu fracote, levante homem está na hora de ir!
    [0] Cala a boca, eu não sou louco de ir para a morte certa!
    [1] Sim senhor!
    (Essa é uma escolha importante, logo é melhor pensar antes de escolher): """))

    if continua == 0:
        print("""   -Você é acusado de traição e é entregue ao inimigo, que o executa logo em seguida.""")
        break

    sleep(5)

    print("=" * 20)

    print("""   -Depois de 3 dias de uma longa viagem os dois exércitos se encontram em uma extensa planície.
        O General diz:
        Senhores obrigado por lutarem até aqui! Sei que não foi fácil, mas eu éço que hoje vocês entrem pelo vale e 
        vençam essa guerra! Hoje é a nossa última esperança e o mundo inteiro e o mundo de nossos filhos e dos filhos de
        nossos filhos depende de nós! Hoje o dia terminará vermelho de sangue, lutem para que esse sangue seja do inimigo.
        Hoje senhores é a luta que nosso pais lutaram e sofreram para travar. LIBERDADE!""")

    c = str((input("    -Deseja continuar? [S/N] "))).strip().upper()[0]


    sleep(5)

    print("""-----------------------------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------------------------------------""")

    defeat = 3

    print("Você tem três pontos")

    if guer == "Mago":


        for batlle in range(0,3):
            sleep(2)

            um = int(input("""  -Um inimigo se aproxima:
            [0] Lançar um feitiço congelante
            [1] Lançar um raio
            [2] Jogar ele para longe
            : """))

            sorte = randint(0, 10)

            sleep(3)

            print("="*20)

            if sorte < 5:
                defeat -= 1

                if um == 0:
                    print(f"Você congelou seu aliado. Perdeu um ponto. Restam {defeat}")
                if um == 1:
                    print(f"Seu raio caiu no lugar errado. Perdeu um ponto. Restam {defeat}")
                if um ==2:
                    print(f"Você acabou se jogando para longe. Perdeu um ponto. Restam {defeat} ")


            elif sorte >= 5:
                defeat += 1

                if um == 0:
                    print(f"Você o congelou com sucesso. Agora você tem {defeat} pontos")
                if um == 1:
                    print(f"Seu raio o atingiu em cheio. Agora você tem {defeat} pontos")
                if um ==2:
                    print(f"Você jogou ele para longe. Agora você tem {defeat} pontos ")

        if defeat > 2:

            print(f"Você terminou com {defeat} pontos")

            print("A União ganhou! A liberdade foi reconstituída e p grande Império do Oeste caíu!")

            sleep(3)

            print("VITÓRIA")

            break

        elif defeat <= 2:

            print(f"Você terminou com {defeat} pontos")

            print('DERROTA')

            print("Você foi morto, assim como a rebelião e a liberdade.")

            sleep(3)

            print(":(")

            break

    elif guer == 'Guerreiro':
        for batlle in range(0, 3):
            sleep(2)
            um = int(input("""  -Um inimigo se aproxima:
            [0] Atacar com a espada
            [1] Atacar com a lança
            [2] Se defender com o escudo
            : """))

            sorte = randint(0, 10)

            sleep(3)

            print("=" * 20)

            if sorte >= 5:

                defeat += 1

                if um == 0:
                    print(f"Sua espada o apunhalou em cheio. Agora você tem {defeat} pontos")
                elif um == 1:
                    print(f"Sua lança cravou o coração do inimigo. Agora você tem {defeat} pontos")

                elif um ==2:

                    print(f"Você conseguiu se defender do inimigo. Agora você tem {defeat} pontos")

            elif sorte < 5:

                defeat -= 1

                if um == 0:
                    print(f"Sua espada não conseguiu acertar o inimigo. Restam {defeat} pontos")
                elif um == 1:
                    print(f"Sua lança passou do lado do inimigo mas não o acertou. Restam {defeat} pontos")

                elif um == 2:

                    print(f"Seu escudo não conseguiu de proteger a tempo. Restam {defeat} pontos")


    sleep(3)

    print("FIM")

    sleep(3)

    if defeat > 2:

        print(f"Você terminou com {defeat} pontos")

        print("A União ganhou! A liberdade foi reconstituída e p grande Império do Oeste caíu!")

        sleep(3)

        print("VITÓRIA")

        break

    elif defeat <= 2:

        print(f"Você terminou com {defeat} pontos")

        print('DERROTA')

        print("Você foi morto, assim como a rebelião e a liberdade.")

        sleep(3)

        print(":(")

        break

print("Obrigado por jogar World War!")

print("Feito por: Daniel Matos Falcão")


