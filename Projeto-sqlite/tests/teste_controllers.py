from src.controllers.item_controller import ItemController
from src.models.item import Item

controller = ItemController()
items = controller.pegar_todos_itens()
for item in items:
    print(item)

novo_item = Item("OLA1", "Cooler REDRAGON Vermelho", 19.90)
print(controller.inserir_item(novo_item))

print("**************************************************************************************")
items = controller.pegar_todos_itens()
for item in items:
    print(item)

print("**************************************************************************************")
item = controller.pegar_item("CAF")
print(item)


print("**************************************************************************************")
item = controller.pegar_item("OLA1")
item.nome = "RTX 4090"
item.preco = 14990.90
print(controller.atualizar_item(item))