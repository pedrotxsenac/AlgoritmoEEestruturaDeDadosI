from Computador import Computador
from Notebook import Notebook
from Desktop import Desktop


desktop = Desktop("desktop gamer com muito RGB", "Preto com RGB", 5000, "100W")
print(desktop.getInformacoes())
desktop.cadastrar()

print('---------------------------------')

notebook = Notebook("Macbook da apple", "cinza", 10000, "15minutos")
print(notebook.getInformacoes())
notebook.cadastrar()
