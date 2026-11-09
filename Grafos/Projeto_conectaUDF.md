# Projeto ConectaUDF

Realizei o Trabalho sozinho Professora, avisei meus amigos para fazerem mas nenhum fez. 

# Grafo UDF

<img width="570" height="364" alt="Grafo_UDF" src="https://github.com/user-attachments/assets/34f05a00-aadf-4fcd-a335-741413049b7e" />

## Legenda

| Letra | Perfil |
|-------|--------|
| U | techudfoficial |
| C | caioo_.__ |
| F | felipinho_rd |
| P | prof.brulex |
| T | t3d3g4_28 |
| L | lo_ricoXd |
| M | _.mayconf |

**V** = {U, C, F, P, T, L, M}

**E** = {(F,U), (P,U), (C,U), (M,U), (T,U), {F,P}, {F,L}, {L,P}, {P,T}, {P,M}, {C,M}}

* pares com parênteses são arestas dirigidas

* pares com chaves são arestas sem seta.

## 1. Número de vértices
7

## 2. Número de arestas
11 (5 com seta e 6 sem seta)

## 3. Ordem |V|
|V| = 7

## 4. Tamanho |E|
|E| = 11

## 5. Grau de cada vértice

| Vértice | Arestas incidentes | Grau |
|---------|--------------------|------|
| U | (F,U), (P,U), (C,U), (M,U), (T,U) | 5 |
| C | (C,U), {C,M} | 2 |
| F | (F,U), {F,P}, {F,L} | 3 |
| P | (P,U), {F,P}, {L,P}, {P,T}, {P,M} | 5 |
| T | (T,U), {P,T} | 2 |
| L | {F,L}, {L,P} | 2 |
| M | (M,U), {P,M}, {C,M} | 3 |

Conferência: 5 + 2 + 3 + 5 + 2 + 2 + 3 = 22 = 2 × 11 arestas.




