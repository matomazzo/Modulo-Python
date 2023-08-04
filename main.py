from funcoes import find_index

list1 = ['maçã', 'banana', 'melancia', 'melão', 'abacate']

item = input("Digite o nome de uma fruta para ver se ela está na lista: ").lower()

var1 = find_index(list1, item)

print(var1)