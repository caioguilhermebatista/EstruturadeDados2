# Caderno do Estudante
# Projeto ConectaUDF: redes sociais com grafos
**Disciplina:** Algoritmos / Matemática Discreta / Ciência de Dados

**Alunos:** Caio Guilherme / Maycon Fidelis / Ítalo Diniz / Beatriz Alves

## 1. O desafio
Você faz parte da equipe que analisa a rede social fictícia **ConectaUDF**. Sua missão é representar as amizades em um grafo, realizar cálculos e usar Python para interpretar a estrutura da rede.

## 2. Conceitos essenciais
- **Vértice (ou nó):** representa um usuário.
- **Aresta:** representa uma amizade entre dois usuários.
- **Grau:** quantidade de conexões diretas de um usuário.
- **Caminho:** sequência de usuários em que cada par consecutivo está conectado.
- **Densidade:** proporção entre as amizades existentes e todas as amizades possíveis.

Neste projeto, a amizade é recíproca. Portanto, usamos um **grafo não direcionado**.

## 3. Conheça os usuários
| Código | Usuário |
|---|---|
| A | Caio |
| B | Maycon |
| C | Diniz |
| D | Beatriz |
| E | Hugo |
| F | Felipe |
| G | Gabriel |
| H | Hendrick |
| I | Jean |
| J | Jeronimo |
| K | Kelly |
| L | Leandro |
| M | Mônica |
| N | Nando |
| O | Otávio |
| P | Pedro |



## Lista de ligações

1. Caio — Diniz
2. Caio — Gabriel
3. Caio — Kelly
4. Caio — Otávio
5. Maycon — Beatriz
6. Maycon — Nando
7. Diniz — Jean
8. Diniz — Kelly
9. Diniz — Leandro
10. Beatriz — Felipe
11. Beatriz — Jeronimo
12. Beatriz — Mônica
13. Hugo — Gabriel
14. Hugo — Otávio
15. Felipe — Mônica
16. Felipe — Pedro
17. Hendrick — Leandro
18. Hendrick — Nando
19. Jean — Nando
20. Jean — Pedro
21. Jeronimo — Leandro
22. Jeronimo — Pedro
23. Mônica — Nando

---
### Resposta

<img width="540" height="450" alt="Captura de tela 2026-11-09 222409" src="https://github.com/user-attachments/assets/16e2c8f0-2692-472d-9c6a-7a8822978d86" />



---

## 4. Passo a passo: desenhe o grafo
1. Desenhe seis círculos, um para cada usuário.
2. Escreva o nome de cada pessoa dentro do círculo.
3. Para cada amizade da lista, desenhe uma linha entre os dois usuários.
4. Não desenhe duas linhas para a mesma amizade.
5. Confira se todas as oito amizades aparecem.

**Espaço para o seu desenho:** faça o grafo no caderno ou em uma ferramenta de desenho.

## 5. Passo a passo: calcule o grau
Conte quantas linhas chegam a cada círculo. Registre o resultado.

| Usuário | Amigos diretos | Grau |
|---|---|---|
| Caio | Diniz, Gabriel, Kelly, Otávio | 4 |
| Maycon | Beatriz, Nando | 2 |
| Diniz | Caio, Jean, Kelly, Leandro | 4 |
| Beatriz | Maycon, Felipe, Jeronimo, Mônica | 4 |
| Hugo | Gabriel, Otávio | 2 |
| Felipe | Beatriz, Mônica, Pedro | 3 |
| Gabriel | Caio, Hugo | 2 |
| Hendrick | Leandro, Nando | 2 |
| Jean | Diniz, Nando, Pedro | 3 |
| Jeronimo | Beatriz, Leandro, Pedro | 3 |
| Kelly | Caio, Diniz | 2 |
| Leandro | Diniz, Hendrick, Jeronimo | 3 |
| Mônica | Beatriz, Felipe, Nando | 3 |
| Nando | Maycon, Hendrick, Jean, Mônica | 4 |
| Otávio | Caio, Hugo | 2 |
| Pedro | Felipe, Jean, Jeronimo | 3 |

**Pergunta 1: quem tem mais conexões diretas?**
Resposta: Caio, Diniz, Beatriz e Nando empatam, cada um com grau 4.

## 6. Passo a passo: calcule o número de amizades
Some todos os graus. Como cada amizade conecta dois usuários, cada aresta é contada duas vezes.

**Fórmula:**  
`Número de arestas = soma dos graus ÷ 2`

1. Soma dos graus: 4 + 2 + 4 + 4 + 2 + 3 + 2 + 2 + 3 + 3 + 2 + 3 + 3 + 4 + 2 + 3 = 46
2. Divida por 2: 46 ÷ 2 = 23
3. Quantas amizades existem no grafo? 23

## 7. Passo a passo: calcule a densidade
A densidade compara as amizades existentes com o total de amizades possíveis.

Para um grafo simples não direcionado:

`D = 2 × E / (V × (V − 1))`

Em que:
- `D` = densidade;
- `E` = número de arestas;
- `V` = número de vértices.

Substitua os valores:
`D = 2 × 23 / (16 × (16 − 1))`

Resultado decimal: 0,1917 
Resultado percentual: 19,17%

**Interprete:** a rede tem poucas ou muitas das conexões possíveis? Explique com suas palavras.
**Resposta:** Possui poucas conexões possíveis porque o calculo mostrou que são quase 19% apenas das conexões possíveis.

________________________________________________________________

## 8. Passo a passo: represente o grafo em Python
A lista de adjacência registra, para cada usuário, os nomes de seus amigos. Digite o código em Python (por exemplo, no Google Colab ou em outro ambiente disponível).

```python
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
```

### Entenda o código
1. `rede` guarda os usuários e suas listas de amigos.
2. `len(rede)` conta os usuários.
3. `len(amigos)` calcula o grau de cada usuário.
4. `sum(...)` soma os graus.
5. `// 2` divide a soma por dois para contar cada amizade uma única vez.
6. A fórmula final calcula a densidade.

## 9. Passo a passo: encontre um caminho
Encontre um caminho de Caio até Mônica. Cada passagem por uma linha corresponde a uma aresta.

Exemplo de registro:
`Caio → Diniz → Jean → Nando → Mônica`

- Quantas arestas há no caminho? 4
- Você encontrou outro caminho com a mesma quantidade de arestas? Qual? Não, o mais perto fica com 5 arestas.
`Caio → Diniz → Jean → Pedro → Felipe → Mônica`

________________________________________________________________

## 10. Desafio em grupo
Amplie a rede social:
1. Adicione pelo menos quatro usuários fictícios.
2. Crie no mínimo cinco novas amizades.
3. Atualize a lista de adjacência no Python.
4. Recalcule os graus, o total de arestas e a densidade.
5. Compare a densidade antes e depois da ampliação.
6. Identifique os usuários com mais conexões.
7. Explique como a rede poderia recomendar uma nova amizade.

## 11. Entrega
Entregue:
- desenho do grafo;
- tabela com os graus;
- cálculos de arestas e densidade;
- código Python executável;
- respostas às perguntas e breve conclusão.

## 12. Pergunta de reflexão
Duas pessoas ainda não são amigas, mas têm três amigos em comum. Como essa informação poderia ser usada para sugerir uma nova conexão? Quais cuidados de privacidade devem ser considerados ao analisar redes sociais?

**Resposta:** A plataforma conta quantos amigos duas pessoas têm em comum, e quanto maior esse número, maior a chance de elas se conhecerem. Com três amigos em comum, é muito provável que o sistema sugira uma à outra, o que pode criar uma nova amizade e deixar a rede mais conectada
