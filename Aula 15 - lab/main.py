from item import Item
from carrinho import Carrinho

item1 = Item(199, 'Dark Souls')

item2 = Item(
    preco = 350,
    nome = 'Dark Souls 2 ',
    descricao =  'Vai sofrer muito!')
    
item3 = Item(
    preco = 350,
    nome = 'Dark Souls 2 ',
    descricao =  'Vai sofrer muito!')

carrinho = Carrinho()

print('Tamanho: ',carrinho.get_tamanho())
print('Valor: ',carrinho.get_valor_total())

# carrinho.adicionar(item1)
# carrinho.adicionar(item2)

# print('Tamanho: ',carrinho.get_tamanho())
# print('Valor: ',carrinho.get_valor_total())

print(item1 == item2)
print(item2 == item3)
print (item2 == 'Dark Souls 2') 