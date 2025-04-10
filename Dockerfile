FROM python:alpine

# Define diretório de trabalho
WORKDIR /app

# Copia dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código
COPY . .

# Expõe a porta do Flask
EXPOSE 5000

# Executa a aplicação
CMD ["python", "main.py"]
