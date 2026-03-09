import math
import os

# a. e d. Vetores para armazenar os dados das culturas (Café e Soja)
# Organizados em vetores paralelos para atender ao requisito 'd'
culturas = []
areas = []
insumos = []
detalhes_manejo = []

def calcular_cafe():
    """
    b. Cálculo de área para Café: Trapézio
    c. Cálculo do manejo: Fosfato (500 mL/metro por rua)
    """
    print("\n[Café] - Cálculo de Área (Trapézio) e Manejo (Fosfato)")
    try:
        base_maior = float(input("Digite a base maior do talhão (m): "))
        base_menor = float(input("Digite a base menor do talhão (m): "))
        altura = float(input("Digite a altura/comprimento do talhão (m): "))
        area_total = ((base_maior + base_menor) * altura) / 2
        
        print("\n--- Manejo de Fosfato ---")
        num_ruas = int(input("Quantas ruas a lavoura de café tem? "))
        comprimento_rua = float(input("Qual o comprimento médio da rua (m)? "))
        
        # Cálculo: 500 mL (0.5 L) por metro linear de rua
        total_litros = num_ruas * comprimento_rua * 0.5
        
        print(f"-> Área calculada (Trapézio): {area_total:.2f} m²")
        print(f"-> Manejo: Serão necessários {total_litros:.2f} litros de Fosfato para as {num_ruas} ruas.")
        
        manejo_str = f"Fosfato: {total_litros:.2f}L ({num_ruas} ruas)"
        return area_total, total_litros, manejo_str
    except ValueError:
        print("Erro: Entrada inválida. Use números para dimensões.")
        return None, None, None

def calcular_soja():
    """
    b. Cálculo de área para Soja: Retângulo
    c. Cálculo do manejo: NPK (Pulverização baseada em área)
    """
    print("\n[Soja] - Cálculo de Área (Retângulo) e Manejo (NPK)")
    try:
        largura = float(input("Digite a largura da área plantada (m): "))
        comprimento = float(input("Digite o comprimento da área plantada (m): "))
        area_total = largura * comprimento
        
        # Exemplo: 0.2 kg de NPK por metro quadrado
        total_npk = area_total * 0.2
        
        print(f"-> Área calculada (Retângulo): {area_total:.2f} m²")
        print(f"-> Manejo: Necessário aplicar {total_npk:.2f} kg de NPK com o trator.")
        
        manejo_str = f"NPK: {total_npk:.2f}kg"
        return area_total, total_npk, manejo_str
    except ValueError:
        print("Erro: Entrada inválida. Use números para dimensões.")
        return None, None, None

def exibir_menu():
    print("\n" + "="*45)
    print("      FARMTECH SOLUTIONS - MENU PRINCIPAL      ")
    print("="*45)
    print("1 - Entrada de dados (Nova Cultura)")
    print("2 - Saída de dados (Listar Registros)")
    print("3 - Atualização de dados (Por Posição)")
    print("4 - Deleção de dados (Por Posição)")
    print("5 - Sair e Salvar")
    print("="*45)

# f. Rotinas de Loop e Decisão
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("\nEscolha a cultura:")
        print("1. Café")
        print("2. Soja")
        tipo = input("Opção: ")
        
        if tipo == '1':
            area, insumo, manejo = calcular_cafe()
            if area is not None:
                culturas.append("Café")
                areas.append(area)
                insumos.append(insumo)
                detalhes_manejo.append(manejo)
                print("Sucesso! Registro adicionado aos vetores.")
        elif tipo == '2':
            area, insumo, manejo = calcular_soja()
            if area is not None:
                culturas.append("Soja")
                areas.append(area)
                insumos.append(insumo)
                detalhes_manejo.append(manejo)
                print("Sucesso! Registro adicionado aos vetores.")
        else:
            print("Erro: Opção de cultura inválida.")

    elif opcao == '2':
        print("\n" + "-"*60)
        print(f"{'ID':<4} | {'CULTURA':<10} | {'ÁREA (m²)':<12} | {'MANEJO'}")
        print("-"*60)
        if not culturas:
            print("Nenhum dado registrado.")
        else:
            for i in range(len(culturas)):
                print(f"{i:<4} | {culturas[i]:<10} | {areas[i]:<12.2f} | {detalhes_manejo[i]}")
        print("-"*60)

    elif opcao == '3':
        if not culturas:
            print("\nErro: Não há dados para atualizar.")
            continue
        try:
            indice = int(input("\nDigite o índice (ID) para atualizar: "))
            if 0 <= indice < len(culturas):
                print(f"Atualizando {culturas[indice]} (ID: {indice})")
                nova_area = float(input("Nova área (m²): "))
                novo_insumo = float(input("Nova quant. insumo (valor numérico): "))
                novo_detalhe = input("Novo detalhe de manejo (texto): ")
                
                areas[indice] = nova_area
                insumos[indice] = novo_insumo
                detalhes_manejo[indice] = novo_detalhe
                print("Dados atualizados com sucesso!")
            else:
                print("Erro: Índice fora do intervalo.")
        except ValueError:
            print("Erro: Digite valores numéricos válidos.")

    elif opcao == '4':
        if not culturas:
            print("\nErro: Não há dados para excluir.")
            continue
        try:
            indice = int(input("\nDigite o índice (ID) para excluir: "))
            if 0 <= indice < len(culturas):
                removido = culturas.pop(indice)
                areas.pop(indice)
                insumos.pop(indice)
                detalhes_manejo.pop(indice)
                print(f"Registro de '{removido}' (ID: {indice}) removido!")
            else:
                print("Erro: Índice fora do intervalo.")
        except ValueError:
            print("Erro: Índice deve ser um número.")

    elif opcao == '5':
        # Salva o arquivo CSV para integração com R
        try:
            with open("dados_farmtech.csv", "w", encoding="utf-8") as file:
                file.write("cultura,area,insumo,manejo\n")
                for i in range(len(culturas)):
                    file.write(f"{culturas[i]},{areas[i]},{insumos[i]},{detalhes_manejo[i]}\n")
            print("\nDados exportados para 'dados_farmtech.csv'.")
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")
            
        print("Encerrando FarmTech App. Até a próxima!")
        break
    else:
        print("Opção inválida. Tente novamente.")
