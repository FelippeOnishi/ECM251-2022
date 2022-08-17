from modelos.documentos import Book, Document, EMail
from plantas import Arvore, Alface

def run_system():
    doc1 = Document()
    doc2 = EMail(to = 'murilo.carvalho@maua.br', authors=["Murilo Zanini"])
    doc3 = Book(title = "Design Patterns", authors=["Erich Gamma","John Vlissides","Ralph Johnson","Richard Helm"])
    print(doc2)
    print(doc3)

if __name__ == "__main__":
    # planta1 = Arvore('Carvalho')
    # planta2 = Alface(nome='Hamburguer de Siri do Futuro')

    # print(planta1.Ola())
    # print(planta2.Ola())
    run_system()