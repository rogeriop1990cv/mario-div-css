from io import FileIO


with open("goomba.html", "a") as f:
    dicionario= {
        1 :  "roxo",
        2 : "marromm",
        3 : "pele",
        4 : "preto"
    }
    for linha in range(14):
        for llinha in range(14):
            cor = input("digite a cor: ")
            f.write(f'<div class="{dicionario[cor]}"></div>')
        f.write("\n")