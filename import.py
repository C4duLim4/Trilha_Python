from pathlib import Path
arquivo = Path("arquivo1.txt")
if arquivo.exists():
    print("O arquivo existe")
else:
    print("O arquivo não existe")


