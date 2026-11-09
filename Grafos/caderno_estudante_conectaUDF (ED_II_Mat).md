# Caderno do Estudante
# Projeto ConectaUDF: redes sociais com grafos
**Disciplina:** Algoritmos / Matemática Discreta / Ciência de Dados

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
| A | Ana |
| B | Bruno |
| C | Carla |
| D | Diego |
| E | Elisa |
| F | Felipe |
As amizades são:
1. Ana — Bruno
2. Ana — Carla
3. Bruno — Carla
4. Bruno — Diego
5. Carla — Elisa
6. Diego — Elisa
7. Diego — Felipe
8. Elisa — Felipe

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
|---|---|---:|
| Ana | __________________ | ____ |
| Bruno | __________________ | ____ |
| Carla | __________________ | ____ |
| Diego | __________________ | ____ |
| Elisa | __________________ | ____ |
| Felipe | __________________ | ____ |

**Pergunta 1:** quem tem mais conexões diretas?  
Resposta: __________________________________________________

## 6. Passo a passo: calcule o número de amizades
Some todos os graus. Como cada amizade conecta dois usuários, cada aresta é contada duas vezes.

**Fórmula:**  
`Número de arestas = soma dos graus ÷ 2`

1. Soma dos graus: ______
2. Divida por 2: ______ ÷ 2 = ______
3. Quantas amizades existem no grafo? ______

## 7. Passo a passo: calcule a densidade
A densidade compara as amizades existentes com o total de amizades possíveis.

Para um grafo simples não direcionado:

`D = 2 × E / (V × (V − 1))`

Em que:
- `D` = densidade;
- `E` = número de arestas;
- `V` = número de vértices.

Substitua os valores:
`D = 2 × ____ / (____ × (____ − 1))`

Resultado decimal: __________  
Resultado percentual: __________ %

**Interprete:** a rede tem poucas ou muitas das conexões possíveis? Explique com suas palavras.

________________________________________________________________

## 8. Passo a passo: represente o grafo em Python
A lista de adjacência registra, para cada usuário, os nomes de seus amigos. Digite o código em Python (por exemplo, no Google Colab ou em outro ambiente disponível).

```python
rede = {
    "Ana": ["Bruno", "Carla"],
    "Bruno": ["Ana", "Carla", "Diego"],
    "Carla": ["Ana", "Bruno", "Elisa"],
    "Diego": ["Bruno", "Elisa", "Felipe"],
    "Elisa": ["Carla", "Diego", "Felipe"],
    "Felipe": ["Diego", "Elisa"]
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
Encontre um caminho de Ana até Felipe. Cada passagem por uma linha corresponde a uma aresta.

Exemplo de registro:
`Ana → __________ → __________ → Felipe`

- Quantas arestas há no caminho? ______
- Você encontrou outro caminho com a mesma quantidade de arestas? Qual?

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
## Desenho do grafo;
 <img width="459" height="354" alt="Captura de tela 2026-11-09 103504" src="https://github.com/user-attachments/assets/616aaeb7-bd56-4a33-ab8b-735243e5992e" />


## Tabela de graus

| Usuário | Grau | Conexões |
|---|---|---|
| Maycon | 9 | Diniz, Caio, Pedro, Arthur, Sousa, Cayo, Luiz, Gustavo, Gabriel |
| Diniz | 8 | João, Nery, Lucas, Portela, Guilherme, Caio, Beatriz, Maycon |
| Pedro | 8 | Caio, Beatriz, Maycon, Arthur, Patrick, Leo, Bruna, Leticia |
| Beatriz | 8 | Diniz, Caio, Pedro, Brian, Camila, Emily, Vitória, Laiane |
| Portela | 6 | João, Nery, Lucas, Guilherme, Diniz, Caio |
| Nery | 5 | João, Lucas, Portela, Guilherme, Diniz |
| Guilherme | 5 | João, Nery, Lucas, Portela, Diniz |
| Arthur | 5 | Maycon, Pedro, Patrick, Bruna, Leticia |
| Caio | 5 | Portela, Diniz, Beatriz, Maycon, Pedro |
| João | 4 | Nery, Portela, Guilherme, Diniz |
| Lucas | 4 | Nery, Portela, Guilherme, Diniz |
| Laiane | 4 | Beatriz, Brian, Emily, Vitória |
| Cayo | 4 | Sousa, Maycon, Luiz, Gustavo |
| Luiz | 4 | Sousa, Cayo, Maycon, Gustavo |
| Emily | 3 | Beatriz, Vitória, Laiane |
| Vitória | 3 | Beatriz, Emily, Laiane |
| Sousa | 3 | Maycon, Cayo, Luiz |
| Gustavo | 3 | Cayo, Maycon, Luiz |
| Patrick | 3 | Pedro, Arthur, Leo |
| Brian | 2 | Beatriz, Laiane |
| Bruna | 2 | Pedro, Arthur |
| Leticia | 2 | Pedro, Arthur |
| Leo | 2 | Pedro, Patrick |
| Camila | 1 | Beatriz |
| Gabriel | 1 | Maycon |

## Arestas e densidade

- Número de vértices: **n = 25**
- Soma dos graus: 104
- Arestas = 104 ÷ 2 = **52**
- Densidade = 2·52 / (25·24) = 104 / 600 ≈ **0,1733 (17,33%)**
- código Python executável;

```python
rede = {
    "Joao": ["Nery", "Portela", "Guilherme", "Diniz"],
    "Nery": ["Joao", "Lucas", "Portela", "Guilherme", "Diniz"],
    "Lucas": ["Nery", "Portela", "Guilherme", "Diniz"],
    "Portela": ["Joao", "Nery", "Lucas", "Guilherme", "Diniz", "Caio"],
    "Guilherme": ["Joao", "Nery", "Lucas", "Portela", "Diniz"],
    "Diniz": ["Joao", "Nery", "Lucas", "Portela", "Guilherme", "Caio", "Beatriz", "Maycon"],
    "Caio": ["Portela", "Diniz", "Beatriz", "Maycon", "Pedro"],
    "Maycon": ["Diniz", "Caio", "Pedro", "Arthur", "Sousa", "Cayo", "Luiz", "Gustavo", "Gabriel"],
    "Beatriz": ["Diniz", "Caio", "Pedro", "Brian", "Camila", "Emily", "Vitoria", "Laiane"],
    "Brian": ["Beatriz", "Laiane"],
    "Camila": ["Beatriz"],
    "Emily": ["Beatriz", "Vitoria", "Laiane"],
    "Vitoria": ["Beatriz", "Emily", "Laiane"],
    "Laiane": ["Beatriz", "Brian", "Emily", "Vitoria"],
    "Pedro": ["Caio", "Beatriz", "Maycon", "Arthur", "Patrick", "Leo", "Bruna", "Leticia"],
    "Patrick": ["Pedro", "Arthur", "Leo"],
    "Leo": ["Pedro", "Patrick"],
    "Bruna": ["Pedro", "Arthur"],
    "Leticia": ["Pedro", "Arthur"],
    "Arthur": ["Maycon", "Pedro", "Patrick", "Bruna", "Leticia"],
    "Sousa": ["Maycon", "Cayo", "Luiz"],
    "Cayo": ["Sousa", "Maycon", "Luiz", "Gustavo"],
    "Luiz": ["Sousa", "Cayo", "Maycon", "Gustavo"],
    "Gustavo": ["Cayo", "Maycon", "Luiz"],
    "Gabriel": ["Maycon"]
}

n = len(rede)

for usuario, amigos in rede.items():
    print(usuario, "tem", len(amigos), "conexoes")

soma_graus = sum(len(amigos) for amigos in rede.values())
arestas = soma_graus // 2

print("Total de usuarios:", n)
print("Total de amizades:", arestas)

densidade = (2 * arestas) / (n * (n - 1))
print(f"Densidade: {densidade:.2%}")
```
   
- respostas às perguntas e breve conclusão.

Como essa informação poderia ser usada para sugerir uma nova conexão? 
Como possue 3 amigos em comum, as chances de fazer uma amizade acontecer entre os dois que não se conhecem é grande

Quais cuidados de privacidade devem ser considerados ao analisar redes sociais?
Consentimento e transparência: o usuário deve saber que suas conexões são usadas para gerar sugestões e poder aceitar ou recusar isso.
Segurança: proteger as bases de dados contra vazamentos e acessos indevidos.

## 12. Pergunta de reflexão
Duas pessoas ainda não são amigas, mas têm três amigos em comum. Como essa informação poderia ser usada para sugerir uma nova conexão? Quais cuidados de privacidade devem ser considerados ao analisar redes sociais?
