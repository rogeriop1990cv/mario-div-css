

lista = [
 
]




dicionario= {
    1 :  "roxo",
    2 : "marromm",
    3 : "pele",
    4 : "preto"
}

codigo = open("goomba.html", "a")
for cor in lista:
    codigo.write(f'<div class="{dicionario[cor]}"></div>\n')
codigo.close()
