# Instale os pacotes necessários caso não tenha (descomente a linha abaixo)
install.packages(c("httr", "jsonlite"))
library(httr)
library(jsonlite)

cat("\n==========================================\n")
cat("   FARMTECH - ESTATÍSTICA E METEOROLOGIA   \n")
cat("==========================================\n\n")

# g. Lendo os dados gerados pelo Python para estatística básica
arquivo <- "dados_farmtech.csv"

if(file.exists(arquivo)) {
  dados <- read.csv(arquivo, encoding = "UTF-8")
  
  # Cálculo de Média e Desvio
  media_area <- mean(dados$area)
  desvio_area <- sd(dados$area)
  
  cat("--- ANÁLISE DAS ÁREAS PLANTADAS ---\n")
  cat(sprintf("Média da área plantada: %.2f m²\n", media_area))
  
  # O Desvio padrão precisa de pelo menos 2 itens no vetor
  if(is.na(desvio_area)){
    cat("Desvio Padrão: Impossível calcular (apenas 1 cultura cadastrada).\n")
  } else {
    cat(sprintf("Desvio Padrão da área: %.2f m²\n", desvio_area))
  }
} else {
  cat("Arquivo dados_farmtech.csv não encontrado. Rode o programa em Python primeiro!\n")
}

cat("\n--- CONECTANDO À API METEOROLÓGICA (SÃO PAULO) ---\n")
# Ir Além: API Pública de clima para auxílio no manejo agrícola
url <- "https://api.open-meteo.com/v1/forecast?latitude=-23.5505&longitude=-46.6333&current_weather=true"

resposta <- GET(url)

if(status_code(resposta) == 200) {
  # Extração dos dados processados do JSON
  clima_json <- fromJSON(content(resposta, "text", encoding = "UTF-8"))
  temperatura <- clima_json$current_weather$temperature
  vento <- clima_json$current_weather$windspeed
  
  cat("Status: Conectado com sucesso à Open-Meteo.\n")
  cat(sprintf("-> Temperatura em SP agora: %.1f °C\n", temperatura))
  cat(sprintf("-> Velocidade do vento: %.1f km/h\n", vento))
  cat("-> Dica da FarmTech: Ventos acima de 10 km/h podem atrapalhar a pulverização da Laranja. Avalie a janela climática!\n")
} else {
  cat("Erro ao conectar na API de clima.\n")
}