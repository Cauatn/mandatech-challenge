import os
import shutil

SRC_FILE = ".env.local"
DEST_FILE = ".env"

if os.path.exists(DEST_FILE):
    print(f"{DEST_FILE} já existe. Nenhuma alteração feita.")
else:
    if os.path.exists(SRC_FILE):
        shutil.copy(SRC_FILE, DEST_FILE)
        print(f"{SRC_FILE} copiado para {DEST_FILE}.")
    else:
        print(f"Arquivo {SRC_FILE} não encontrado. Crie-o antes de rodar este script.")
