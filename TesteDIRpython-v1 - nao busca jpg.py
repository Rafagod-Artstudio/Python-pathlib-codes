import os, stat
import shutil
import time
from pathlib import Path
from datetime import datetime
from datetime import timedelta
# Código para se obter a pasta do arquivo py pela qual será feito a varredura pelo algoritmo
diretorio = Path(os.getcwd())
print(diretorio)
#
# Loop infinito até que se digite uma variável com três caracteres para um tipo de extensao
#
while True:
    try:
        ext = str(input("Digite a extensão desejada:"))
        if len(ext) > 3:
            raise ValueError("Extensão inválida")
        break
    except ValueError as error:
        print(error)
#
# Comando que seleciona e cria lista de todos os arquivos com extensão escolhida e em todos os
# subdiretorios de onde está o arquivo *.py
#
extensao = str('**/*.' + ext)
print(extensao)
files = sorted(Path(diretorio).glob(extensao))
print(files)
# Loop que varre todos os arquivos indicados na variável matriz files e obtém
# o caminho e a localização do arquivo guardando em variáveis a partir da
# da data de modificacao o ano e o mês 
for x in files:
    diretoriox = Path(x)
    print(diretoriox)
    data_iniciox = os.path.getmtime(diretoriox)
    data_objx = datetime.fromtimestamp(data_iniciox)
    ano = str(data_objx.year)
    mes = str(data_objx.month)
    if len(mes) == 1:
        mesdigito = mes
        mes = "0" + mesdigito
    dir_ano = diretorio / ano   
    dir_mes = diretorio / ano / mes
    if os.path.exists(dir_ano) == False:
        Path(dir_ano).mkdir(parents=True, exist_ok=True)
        if os.path.exists(dir_mes) == False:
            Path(dir_mes).mkdir(parents=True, exist_ok=True)
    else:
        if os.path.exists(dir_mes) == False:
            Path(dir_mes).mkdir(parents=True, exist_ok=True)
    diretoriodestino = dir_mes
    shutil.copy2(diretoriox, diretoriodestino)
