# Material do Estudante — Desafios 5 e 7 (Respondido)

**Estrutura de Dados II | Unidade III — Grafos | Profa. Kadidja Valéria**

**Nome:** ____________________  **Turma:** ________  **Data:** ___/___/______

---

## Desafio 5 — Isomorfismo

**Grafos dados:**

- G: V = {1, 2, 3, 4}; E = {(1,2), (2,3), (3,4), (4,1)}
- H: V = {a, b, c, d}; E = {(a,c), (c,b), (b,d), (d,a)}

### 1. Ordem e tamanho

- **Ordem** = número de vértices; **tamanho** = número de arestas.

| Grafo | Ordem \|V\| | Tamanho \|E\| |
|-------|:-----------:|:-------------:|
| G     | 4           | 4             |
| H     | 4           | 4             |

### 2. Grau de cada vértice e sequência de graus

**Grafo G**

| Vértice | Vizinhos | Grau |
|:-------:|----------|:----:|
| 1 | 2, 4 | 2 |
| 2 | 1, 3 | 2 |
| 3 | 2, 4 | 2 |
| 4 | 3, 1 | 2 |

**Grafo H**

| Vértice | Vizinhos | Grau |
|:-------:|----------|:----:|
| a | c, d | 2 |
| b | c, d | 2 |
| c | a, b | 2 |
| d | b, a | 2 |

**Sequência de graus:** G = (2, 2, 2, 2) e H = (2, 2, 2, 2). São iguais.

### 3. Correspondência entre os vértices

Ambos os grafos são ciclos de comprimento 4 (G: 1–2–3–4–1; H: a–c–b–d–a). Percorrendo os ciclos na mesma ordem, define-se a função f: V(G) → V(H):

| Vértice em G | Correspondente em H |
|:------------:|:-------------------:|
| 1 | a |
| 2 | c |
| 3 | b |
| 4 | d |

A função é **bijetora** (cada vértice de H é imagem de exatamente um vértice de G).

### 4. Verificação aresta por aresta

| Aresta em G | Imagem (f(u), f(v)) | Existe em H? |
|:-----------:|:-------------------:|:------------:|
| (1,2) | (a,c) | ✔ Sim |
| (2,3) | (c,b) | ✔ Sim |
| (3,4) | (b,d) | ✔ Sim |
| (4,1) | (d,a) | ✔ Sim |

As 4 arestas de G são levadas em 4 arestas distintas de H. Como H possui exatamente 4 arestas, não sobra nenhuma aresta em H sem correspondente. Logo, **u e v são adjacentes em G ⇔ f(u) e f(v) são adjacentes em H**.

### 5. Conclusão

**Os grafos G e H são isomorfos.**

**Justificativa:** existe uma bijeção f entre os vértices de G e H que preserva as adjacências (e as não adjacências). Além disso, os invariantes coincidem: mesma ordem (4), mesmo tamanho (4) e mesma sequência de graus (2, 2, 2, 2). Os desenhos e rótulos são diferentes, mas a estrutura é a mesma: um ciclo de 4 vértices (C₄).

### Reflexão: ter a mesma sequência de graus é suficiente para garantir isomorfismo?

**Não.** A sequência de graus é uma condição **necessária**, mas **não suficiente**. Contraexemplo:

- **G₁ = C₆** (ciclo de 6 vértices): 6 vértices, 6 arestas, todos com grau 2.
- **G₂ = dois triângulos disjuntos** (K₃ ∪ K₃): 6 vértices, 6 arestas, todos com grau 2.

Ambos têm a sequência (2, 2, 2, 2, 2, 2), porém **não são isomorfos**: G₁ é conexo e G₂ não é (possui duas componentes). Como a conexidade é preservada por isomorfismos, os grafos têm estruturas diferentes. Portanto, sequências de graus iguais só permitem *descartar* isomorfismo quando diferem; quando coincidem, é preciso exibir a bijeção que preserva as adjacências.

---

## Desafio 7 — Sequência de graus

**Objetivo:** construir um grafo simples com 8 vértices e sequência de graus (1, 1, 2, 3, 3, 4, 4, 6).

### Verificação prévia (o grafo existe?)

- Soma dos graus = 1+1+2+3+3+4+4+6 = **24**, que é par → número de arestas = 24 / 2 = **12**.
- Teste de Havel–Hakimi (ordem decrescente: 6, 4, 4, 3, 3, 2, 1, 1):
  1. Remove 6 e subtrai 1 dos 6 maiores seguintes → (3, 3, 2, 2, 1, 0, 1) → ordenado: (3, 3, 2, 2, 1, 1, 0)
  2. Remove 3 e subtrai 1 dos 3 seguintes → (2, 1, 1, 1, 1, 0)
  3. Remove 2 e subtrai 1 dos 2 seguintes → (0, 0, 1, 1, 0) → ordenado: (1, 1, 0, 0, 0)
  4. Remove 1 e subtrai 1 do seguinte → (0, 0, 0, 0) ✔

A sequência é **gráfica**, ou seja, existe um grafo simples com esses graus.

### 1. Vértices

V = {A, B, C, D, E, F, G, H}

### 2. Construção das arestas (do vértice de maior grau para o menor)

Graus-alvo: A = 6, B = 4, C = 4, D = 3, E = 3, F = 2, G = 1, H = 1.

1. **A (grau 6)** liga-se a B, C, D, E, F, G → arestas AB, AC, AD, AE, AF, AG.
   Faltam: B = 3, C = 3, D = 2, E = 2, F = 1, G = 0, H = 1.
2. **B (falta 3)** liga-se a C, D, E → arestas BC, BD, BE.
   Faltam: C = 2, D = 1, E = 1, F = 1, G = 0, H = 1.
3. **C (falta 2)** liga-se a D, E → arestas CD, CE.
   Faltam: F = 1, H = 1 (os demais = 0).
4. **F** liga-se a **H** → aresta FH.

Nenhum laço e nenhuma aresta paralela foi usado.

### 3. Conjunto de arestas

**E = {AB, AC, AD, AE, AF, AG, BC, BD, BE, CD, CE, FH}** (12 arestas)

### 4. Graus obtidos

| Vértice | Vizinhos | Grau obtido |
|:-------:|----------|:-----------:|
| A | B, C, D, E, F, G | **6** |
| B | A, C, D, E | **4** |
| C | A, B, D, E | **4** |
| D | A, B, C | **3** |
| E | A, B, C | **3** |
| F | A, H | **2** |
| G | A | **1** |
| H | F | **1** |

**Sequência obtida (ordem não decrescente):** (1, 1, 2, 3, 3, 4, 4, 6) ✔

### 5. Verificação

- **Soma dos graus:** 6 + 4 + 4 + 3 + 3 + 2 + 1 + 1 = **24**
- **Número de arestas:** **12**
- **Soma dos graus = 2 × número de arestas?** Sim: 24 = 2 × 12 ✔ (Lema do aperto de mãos: cada aresta contribui com 1 grau para cada uma de suas duas extremidades.)

### Desenho (representação textual)

```
        G
        |
        A ------ F ------ H
      / | \
     /  |  \
    B---+---C
     \  |  /
      \ | /
       D  E      (D e E ligados a A, B e C)
```

Estrutura resumida: A, B, C formam um triângulo; D e E estão ligados aos três (A, B, C); G é pendente em A; e F liga A a H, formando um caminho A–F–H.

---

**Referência:** GOMES, Paulo César Rodacki. *Grafos: conceitos fundamentais, algoritmos e aplicações*. Blumenau: IFC, 2022. Capítulo 1.
