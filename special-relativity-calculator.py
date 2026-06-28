import math
import sys

def calcular_relatividade(): # Relatividade Restrita
    print("\n" + "" * 50)
    print(" CALCULADORA DE RELATIVIDADE RESTRITA")
    print("" * 50)
   
    while True:
        # 1. Entrada da velocidade como fração de c
        try:
            entrada_v = input("\nDigite a velocidade como fração de c: ").strip().lower()
            if entrada_v == 'sair':
                print("\nEncerrando o simulador do espaço-tempo.")
                sys.exit()
               
            v_frac = float(entrada_v)
        except ValueError:
            print("[Erro]: Por favor, digite um número válido.")
            continue

        if v_frac <= 0 or v_frac >= 1:
            print("[Erro Físico]: A velocidade deve ser maior que 0 e menor que 1c.")
            continue

        # 2. Cálculo do Fator Lorentz (Gama)
        gamma = 1 / math.sqrt(1 - v_frac**2)
        print(f"-> Fator Lorentz (Gama): {gamma:.4f}\n")

        # 3. Menu de opções para o usuário escolher o cálculo físico
        print("Escolha o cálculo que deseja realizar:")
        print("[1] Dilatação do Tempo")
        print("[2] Contração do Comprimento")
        print("[3] Energia Relativística Total (E = m*c²)")
        print("[4] Executar todos os cálculos")
        print("[5] Mudar a velocidade de simulação")
       
        opcao = input("Digite a opção (1-5): ").strip()
       
        if opcao == '5':
            continue
           
        c = 299792458

        try:
            if opcao in ['1', '4']:
                print("\nDILATAÇÃO DO TEMPO")
                t0 = float(input("Digite o tempo próprio (t₀) em anos: "))
                t = gamma * t0
                print(f"Resultado (t): {t:.4f} anos decorridos para o observador.")

            if opcao in ['2', '4']:
                print("\nCONTRAÇÃO DO COMPRIMENTO")
                l0 = float(input("Digite o comprimento próprio (L₀) em metros: "))
                l = l0 / gamma
                print(f"Resultado (L): {l:.4f} metros contraídos na direção do movimento.")

            if opcao in ['3', '4']:
                print("\nENERGIA RELATIVÍSTICA TOTAL")
                m0 = float(input("Digite a massa de repouso (m₀) em kg: "))
                energia = gamma * m0 * (c**2)
                print(f"Resultado (E): {energia:.4e} Joules")
               
            if opcao not in ['1', '2', '3', '4', '5']:
                print("[Erro]: Opção inválida no menu.")
               
        except ValueError:
            print("[Erro]: Digite apenas números para os valores físicos.")

if __name__ == "__main__":
    calcular_relatividade()
