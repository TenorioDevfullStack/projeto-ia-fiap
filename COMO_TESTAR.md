# Guia de Testes - Projeto FarmTech Solutions

Este guia explica como validar as funcionalidades da aplicação de Agricultura Digital, garantindo que todos os requisitos da FarmTech Solutions foram atendidos.

---

## 1. Testando a Aplicação Python (`farmtech_app.py`)

A aplicação Python é responsável pela entrada de dados, cálculos geométricos de área, manejo de insumos e armazenamento em vetores.

### Passo a Passo:
1. Abra o terminal e navegue até a pasta do projeto.
2. Execute o comando:
   ```powershell
   python farmtech_app.py
   ```
3. **Teste de Inserção (Opção 1):**
   - Escolha **Café**: Insira dimensões (ex: Base 100m, Base 80m, Altura 50m). O sistema calculará a área do Trapézio. Informe o número de ruas e o comprimento médio para calcular o Fosfato necessário.
   - Escolha **Soja**: Insira Largura e Comprimento. O sistema calculará a área do Retângulo e o NPK necessário (0.2kg por m²).
4. **Teste de Visualização (Opção 2):**
   - Verifique se os dados inseridos aparecem na tabela com ID e valores formatados.
5. **Teste de Edição/Exclusão (Opções 3 e 4):**
   - Tente atualizar uma área ou excluir um registro usando o ID mostrado na listagem.
6. **Teste de Saída (Opção 5):**
   - Saia do programa. Isso gerará automaticamente o arquivo `dados_farmtech.csv` necessário para o próximo passo.

---

## 2. Testando a Análise em R (`analise_farmtech.R`)

O script em R realiza o processamento estatístico dos dados salvos pelo Python e conecta-se a uma API meteorológica em tempo real.

### Passo a Passo:
1. No terminal, execute:
   ```powershell
   Rscript analise_farmtech.R
   ```
   *(Nota: Certifique-se de ter os pacotes `httr` e `jsonlite` instalados no R).*

2. **O que validar na saída:**
   - **Estatísticas:** O R deve mostrar a **Média** e o **Desvio Padrão** das áreas e insumos inseridos anteriormente.
   - **Integração com API (Ir Além):**
     - O script conectará à API Open-Meteo.
     - Mostrará a **Temperatura** e a **Condição do Céu** em texto simples.
     - **Análise para Manejo:** O sistema emitirá um alerta automático se o vento estiver acima de 12km/h ou se houver detecção de chuva, sugerindo a suspensão da pulverização.

---

## 3. Verificação de Arquivos e Documentação

- Verifique se o arquivo `resumo_artigo.md` contém o resumo acadêmico solicitado sobre VANTs.
- Verifique se o `link_video.txt` foi atualizado com o seu link do YouTube.
- Certifique-se de que todos os arquivos estão na raiz antes de gerar o ZIP final para entrega.

---
**FarmTech Solutions - Inovação no Campo**
