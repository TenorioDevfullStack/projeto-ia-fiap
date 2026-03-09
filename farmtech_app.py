import math
import os

# a. e d. Vetores para armazenar as culturas do estado (Cana-de-açúcar e Laranja)
culturas = []
areas = []
insumos = []

def calcular_cana():
    # b. Cálculo de área: Retângulo
    print("\n[Cana-de-açúcar] - Cálculo de Área (Retângulo)")
    base = float(input("Digite a largura da área plantada (m): "))
    altura = float(input("Digite o comprimento (m): "))
    area_total = base * altura
    
    # c. Manejo de Insumos (ex: 0.1 kg de adubo NPK por metro quadrado)
    adubo = area_total * 0.1
    print(f"-> Área calculada: {area_total:.2f} m²")
    print(f"-> Manejo: Necessário aplicar {adubo:.2f} kg de adubo NPK com o trator.")
    return area_total, adubo

def calcular_laranja():
    # b. Cálculo de área: Círculo (Pivô central)
    print("\n[Laranja] - Cálculo de Área (Círculo)")
    raio = float(input("Digite o raio de alcance do pivô de irrigação (m): "))
    area_total = math.pi * (raio ** 2)
    
    # c. Manejo de Insumos (ex: 0.5 Litros de defensivo por metro quadrado)
    defensivo = area_total * 0.5
    print(f"-> Área calculada: {area_total:.2f} m²")
    print(f"-> Manejo: Pulverizar {defensivo:.2f} Litros de defensivo agrícola.")
    return area_total, defensivo

# f. Rotinas de Loop e Decisão
while True:
    print("\n" + "="*40)
    print("  MENU FARMTECH - AGRICULTURA DIGITAL  ")
    print("="*40)
    print("1 - Entrada de dados (Inserir cultura)")
    print("2 - Saída de dados (Listar lavouras)")
    print("3 - Atualização de dados no vetor")
    print("4 - Deleção de dados do vetor")
    print("5 - Sair do programa")
    
    # e. Menu de opções
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("\nEscolha a cultura a registrar:")
        print("1. Cana-de-açúcar")
        print("2. Laranja")
        tipo = input("Opção: ")
        
        if tipo == '1':
            area, insumo = calcular_cana()
            culturas.append("Cana-de-açúcar")
            areas.append(area)
            insumos.append(insumo)
            print("Sucesso! Registro inserido no vetor.")
        elif tipo == '2':
            area, insumo = calcular_laranja()
            culturas.append("Laranja")
            areas.append(area)
            insumos.append(insumo)
            print("Sucesso! Registro inserido no vetor.")
        else:
            print("Erro: Cultura não reconhecida.")

    elif opcao == '2':
        print("\n--- DADOS REGISTRADOS (SAÍDA) ---")
        if not culturas:
            print("Vetor vazio. Nenhum dado cadastrado.")
        else:
            for i in range(len(culturas)):
                print(f"Índice [{i}] | Cultura: {culturas[i]} | Área: {areas[i]:.2f} m² | Insumo: {insumos[i]:.2f}")

    elif opcao == '3':
        indice = int(input("\nDigite o índice do dado que deseja atualizar: "))
        if 0 <= indice < len(culturas):
            nova_area = float(input("Digite a nova área corrigida (m²): "))
            novo_insumo = float(input("Digite a nova quantidade de insumo: "))
            areas[indice] = nova_area
            insumos[indice] = novo_insumo
            print("Dado atualizado com sucesso!")
        else:
            print("Erro: Índice inválido.")

    elif opcao == '4':
        indice = int(input("\nDigite o índice que deseja excluir: "))
        if 0 <= indice < len(culturas):
            cultura_removida = culturas.pop(indice)
            areas.pop(indice)
            insumos.pop(indice)
            print(f"Registro de '{cultura_removida}' apagado do vetor!")
        else:
            print("Erro: Índice inválido.")

    elif opcao == '5':
        # Salva o arquivo CSV para o R ler em seguida
        with open("dados_farmtech.csv", "w", encoding="utf-8") as file:
            file.write("cultura,area,insumo\n")
            for i in range(len(culturas)):
                file.write(f"{culturas[i]},{areas[i]},{insumos[i]}\n")
        print("\nDados exportados para 'dados_farmtech.csv'.")
        print("Encerrando o sistema FarmTech. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")