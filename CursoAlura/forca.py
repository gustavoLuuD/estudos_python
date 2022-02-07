def jogar():							
	print("*******************")
	print("JOGO DA FORCA")
	print("*******************")
	acertou = False
	enforcou = False
	palavra_secreta = "melancia"
	letras_acertadas = ["_","_","_","_","_","_","_","_"]
	
	while(not enforcou and not acertou):
		escolha = input("Escolha uma letra:").strip().casefold() 		#remoção de espaços e passa para lowercase
		if(escolha == "quit"):			# remover aqui depois
			break
		index = 0
		for letra in palavra_secreta:
			if(letra == escolha):
				letras_acertadas[index] = escolha
			index = index + 1
		if("_" not in letras_acertadas):
			acertou = True
		print(letras_acertadas)
	if(acertou):
		print("Parabéns vc acertou!")
if(__name__ == "__main__"):
	jogar()