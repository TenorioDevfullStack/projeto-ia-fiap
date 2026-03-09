# Configura o caminho da biblioteca do usuário
.libPaths(c(file.path(Sys.getenv("USERPROFILE"), "R", "win-library", "4.5"), .libPaths()))

# Instale os pacotes necessários caso não tenha
# install.packages(c("httr", "jsonlite"), repos = "https://cloud.r-project.org")
library(httr)
library(jsonlite)

cat("\n============================================\n")
cat("    FARMTECH - ESTATÍSTICA E METEOROLOGIA    \n")
cat("============================================\n\n")

# g. Lendo os dados gerados pelo Python para estatística básica
arquivo <- "dados_farmtech.csv"

if(file.exists(arquivo)) {
  dados <- read.csv(arquivo, encoding = "UTF-8")
  
  if(nrow(dados) > 0) {
    cat("--- ANÁLISE ESTATÍSTICA DOS DADOS ---\n")
    
    # Cálculos para Área
    media_area <- mean(dados$area)
    desvio_area <- sd(dados$area)
    
    # Cálculos para Insumos
    media_insumo <- mean(dados$insumo)
    desvio_insumo <- sd(dados$insumo)
    
    cat(sprintf("Média da área plantada: %.2f m²\n", media_area))
    if(!is.na(desvio_area)) {
      cat(sprintf("Desvio Padrão da área: %.2f m²\n", desvio_area))
    }
    
    cat(sprintf("Média de insumos aplicados: %.2f (L ou kg)\n", media_insumo))
    if(!is.na(desvio_insumo)) {
      cat(sprintf("Desvio Padrão de insumos: %.2f\n", desvio_insumo))
    }
    
    cat("\nResumo por Cultura:\n")
    print(aggregate(area ~ cultura, data = dados, FUN = function(x) c(Media = mean(x), Total = sum(x))))
    
  } else {
    cat("O arquivo CSV está vazio. Adicione dados no Python primeiro!\n")
  }
} else {
  cat("Arquivo dados_farmtech.csv não encontrado. Rode o programa em Python primeiro!\n")
}

cat("\n--- CONECTANDO À API METEOROLÓGICA (SÃO PAULO) ---\n")
# Ir Além: Conectar a uma API meteorológica pública (Open-Meteo)
# Latitude/Longitude de São Paulo (pode ser ajustado)
url <- "https://api.open-meteo.com/v1/forecast?latitude=-23.5505&longitude=-46.6333&current_weather=true"

resposta <- GET(url)

if(status_code(resposta) == 200) {
  clima_json <- fromJSON(content(resposta, "text", encoding = "UTF-8"))
  temperatura <- clima_json$current_weather$temperature
  vento <- clima_json$current_weather$windspeed
  direcao_vento <- clima_json$current_weather$winddirection
  
  cat("Status: Conexão bem-sucedida!\n")
  cat(sprintf("-> Temperatura atual: %.1f °C\n", temperatura))
  cat(sprintf("-> Velocidade do vento: %.1f km/h\n", vento))
  cat(sprintf("-> Direção do vento: %d°\n", direcao_vento))
  
  # Dica Agrícola baseada no clima
  if(vento > 15) {
    cat("!!! ALERTA: Ventos fortes detectados. Evitar pulverização agora.\n")
  } else {
    cat("DICA: Condições de vento favoráveis para manejo de precisão.\n")
  }
} else {
  cat("Não foi possível coletar dados climáticos no momento.\n")
}
cat("\n============================================\n")
