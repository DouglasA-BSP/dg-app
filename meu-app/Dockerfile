# Fase 1: Definir a imagem base
# Usa uma imagem Python 3.9 slim (versão reduzida) como base
FROM python:3.9-slim

# Fase 2: Configurar diretório de trabalho
# Define /app como diretório padrão dentro do container
WORKDIR /app

# Fase 3: Instalar dependências
# Copia o arquivo de dependências primeiro (para aproveitar cache do Docker)
COPY requirements.txt .
# Instala as dependências Python listadas no requirements.txt
RUN pip install -r requirements.txt

# Fase 4: Copiar código da aplicação
# Copia o arquivo principal da aplicação para o container
COPY app.py .

# Fase 5: Configurar porta de exposição
# Informa que a aplicação usará a porta 80 (não abre a porta, apenas documenta)
EXPOSE 80

# Fase 6: Definir comando de execução
# Comando que será executado quando o container iniciar
CMD ["python", "app.py"]