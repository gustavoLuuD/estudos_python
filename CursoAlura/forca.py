def jogar():							
	print("*******************")
	print("JOGO DA FORCA")
	print("*******************")
	acertou = False
	enforcou = False
	palavra_secreta = "melancia"
	while(not enforcou and not acertou):
		escolha = input("Escolha uma letra:").strip().casefold() 		#remoção de espaços e passa para lowercase
		if(escolha == "quit"):			# remover aqui depois
			break
		for letra in palavra_secreta:
			if(letra == escolha):
				print("Tem")
				break
if(__name__ == "__main__"):
	jogar()