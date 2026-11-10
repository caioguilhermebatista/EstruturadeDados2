rede = {
    "Caio": ["Diniz", "Gabriel", "Kelly", "Otávio"],
    "Maycon": ["Beatriz", "Nando"],
    "Diniz": ["Caio", "Jean", "Kelly", "Leandro"],
    "Beatriz": ["Maycon", "Felipe", "Jeronimo", "Mônica"],
    "Hugo": ["Gabriel", "Otávio"],
    "Felipe": ["Beatriz", "Mônica", "Pedro"],
    "Gabriel": ["Caio", "Hugo"],
    "Hendrick": ["Leandro", "Nando"],
    "Jean": ["Diniz", "Nando", "Pedro"],
    "Jeronimo": ["Beatriz", "Leandro", "Pedro"],
    "Kelly": ["Caio", "Diniz"],
    "Leandro": ["Diniz", "Hendrick", "Jeronimo"],
    "Mônica": ["Beatriz", "Felipe", "Nando"],
    "Nando": ["Maycon", "Hendrick", "Jean", "Mônica"],
    "Otávio": ["Caio", "Hugo"],
    "Pedro": ["Felipe", "Jean", "Jeronimo"]
}

# Quantidade de usuarios
n = len(rede)

# Calcule o grau de cada usuario
for usuario, amigos in rede.items():
    print(usuario, "tem", len(amigos), "conexoes")

# A soma dos graus conta cada amizade duas vezes
soma_graus = sum(len(amigos) for amigos in rede.values())
arestas = soma_graus // 2

print("Total de usuarios:", n)
print("Total de amizades:", arestas)

# Densidade do grafo
densidade = (2 * arestas) / (n * (n - 1))
print(f"Densidade: {densidade:.2%}")
