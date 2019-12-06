from random import shuffle

continue = 'S'
while continue.upper()
	words = input("insira a frase: ").split(" ")
	for word in words: shuffle(words)

	print(" ".join(words))

	continue = input('Digite S para continuar')