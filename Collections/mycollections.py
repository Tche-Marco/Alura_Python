from collections import defaultdict

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_leaning = {13, 23, 56, 42}

# todos os usuários de data science e lachine learning
# Uniao de dois conjuntos
print(usuarios_data_science | usuarios_machine_leaning)

# apenas usuários que fizeram data science e lachine learning
print(usuarios_data_science & usuarios_machine_leaning)  # Interseção

# apenas usuários que fizeram data science, mas não fizeram machine learning
print(usuarios_data_science - usuarios_machine_leaning)

aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}

print(aparicoes)
aparicoes["Carlos"] = 1
print(aparicoes)
del aparicoes["Carlos"]
print(aparicoes)
for valores in aparicoes.keys():  # percorre as chaves
    print(valores)
for valores in aparicoes.values():  # percorre os valores
    print(valores)
for chave, valor in aparicoes.items():  # percorre as linhas
    print(f'{chave} = {valor}')

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro".lower()

# defaultdict retorna um valor default sempre que for solicitada uma chave que não esteja no dicionario
aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    # se n tiver nada em aparicoes[palavra], por conta do defaultdict, retorna 0
    aparicoes[palavra] += 1

print(aparicoes)
