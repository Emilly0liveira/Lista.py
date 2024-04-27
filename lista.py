frutas = ["maçã", "banana", "laranja", "uva", "morango"]

frutas.append("abacaxi")

frutas.remove("uva")

fruta_especifica = "morango"
esta_presente = fruta_especifica in frutas

frutas_ordenadas = sorted(frutas)

print("Lista de frutas:", frutas)
print("A fruta 'uva' foi removida.")
print("A fruta '{}' está presente na lista? {}".format(fruta_especifica, esta_presente))
print("Todos os itens da lista em ordem alfabética:", frutas_ordenadas)
