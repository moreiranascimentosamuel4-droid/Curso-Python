import random
import time

def jogar():
    print("🎯=== JOGO DA ADIVINHAÇÃO ===🎯")
    print("Tente adivinhar o número secreto!")
    print("--------------------------------")

    while True:
        print("\nEscolha o nível de dificuldade:")
        print("1 - Fácil (1 a 50, 10 tentativas)")
        print("2 - Médio (1 a 100, 7 tentativas)")
        print("3 - Difícil (1 a 200, 5 tentativas)")

        nivel = input("Digite o número do nível: ")

        if nivel == "1":
            limite = 50
            tentativas = 10
        elif nivel == "2":
            limite = 100
            tentativas = 7
        elif nivel == "3":
            limite = 200
            tentativas = 5
        else:
            print("❌ Nível inválido, tente novamente.")
            continue

        numero_secreto = random.randint(1, limite)
        pontos = 1000
        print(f"\nEstou pensando em um número entre 1 e {limite}...")
        time.sleep(1)
        print("Você consegue adivinhar? 😏")

        for rodada in range(1, tentativas + 1):
            print(f"\nTentativa {rodada} de {tentativas}")
            chute = input("Seu palpite: ")

            if not chute.isdigit():
                print("⚠️ Digite apenas números!")
                continue

            chute = int(chute)

            if chute < 1 or chute > limite:
                print(f"⚠️ O número deve estar entre 1 e {limite}.")
                continue

            # compara o chute com o número secreto
            if chute == numero_secreto:
                print(f"🎉 ACERTOU! O número era {numero_secreto}.")
                print(f"💯 Você fez {pontos} pontos!")
                break
            else:
                diferenca = abs(numero_secreto - chute)
                if diferenca <= 5:
                    dica = "🔥 Está MUITO perto!"
                elif diferenca <= 15:
                    dica = "🌡️ Está perto!"
                else:
                    dica = "❄️ Está longe..."
                
                if chute < numero_secreto:
                    print(f"O número secreto é MAIOR. {dica}")
                else:
                    print(f"O número secreto é MENOR. {dica}")

                # perde pontos proporcionalmente à diferença
                pontos_perdidos = diferenca * 5
                pontos -= pontos_perdidos
                if pontos < 0:
                    pontos = 0

        else:
            print(f"\n💀 Fim das tentativas! O número era {numero_secreto}.")
            print(f"Você fez {pontos} pontos.")

        # perguntar se quer jogar novamente
        jogar_novamente = input("\nQuer jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != "s":
            print("\n👋 Obrigado por jogar! Até a próxima!")
            break

# executa o jogo
if __name__ == "__main__":
    jogar()