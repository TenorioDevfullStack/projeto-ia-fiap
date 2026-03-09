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
# Latitude e Longitude (São Paulo)
lat <- -23.5505
lon <- -46.6333
url <- sprintf("https://api.open-meteo.com/v1/forecast?latitude=%.4f&longitude=%.4f&current_weather=true", lat, lon)

resposta <- GET(url)

if(status_code(resposta) == 200) {
  clima_json <- fromJSON(content(resposta, "text", encoding = "UTF-8"))
  atual <- clima_json$current_weather
  
  # Interpretando o Código de Clima (WMO Weather interpretation codes)
  get_weather_desc <- function(code) {
    if (code == 0) return("Céu Limpo")
    if (code %in% c(1, 2, 3)) return("Parcialmente Nublado")
    if (code %in% c(45, 48)) return("Nevoeiro")
    if (code %in% c(51, 53, 55)) return("Drizzle (Garoa)")
    if (code %in% c(61, 63, 65)) return("Chuva")
    if (code %in% c(71, 73, 75)) return("Neve")
    if (code %in% c(80, 81, 82)) return("Pancadas de Chuva")
    if (code %in% c(95, 96, 99)) return("Trovoada")
    return("Desconhecido")
  }
  
  condicao <- get_weather_desc(atual$weathercode)
  
  cat("Status: Conexão bem-sucedida! Dados em tempo real.\n")
  cat(sprintf("-> Localização: Lat %.2f, Lon %.2f\n", lat, lon))
  cat(sprintf("-> Condição: %s\n", condicao))
  cat(sprintf("-> Temperatura: %.1f °C\n", atual$temperature))
  cat(sprintf("-> Velocidade do vento: %.1f km/h\n", atual$windspeed))
  
  # Lógica de decisão para auxílio no manejo
  cat("\nANÁLISE PARA MANEJO:\n")
  if (atual$windspeed > 12) {
    cat("- [AVISO] Vento acima de 12km/h detectado. Risco de deriva na pulverização.\n")
  } else {
    cat("- [OK] Ventos baixos. Janela favorável para aplicação de insumos.\n")
  }
  
  if (atual$weathercode >= 60) {
    cat("- [ALERTA] Chuva detectada ou iminente. Evitar aplicação de fertilizantes foliares.\n")
  } else {
    cat("- [INFORMAÇÃO] Sem previsão imediata de chuva forte.\n")
  }
  
} else {
  cat("Erro: Não foi possível conectar à API de meteorologia.\n")
}
cat("\n============================================\n")
