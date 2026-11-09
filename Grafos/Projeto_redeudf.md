# Caderno do Estudante
# Projeto ConectaUDF: redes sociais com grafos
# Integrantes: Caio Guilherme, Maycon Fidelis, Ítalo Diniz e Beatriz Alves
**Disciplina:** Algoritmos / Matemática Discreta / Ciência de Dados



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
