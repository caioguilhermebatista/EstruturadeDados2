# Revisão de estrutura de árvores (Atividade individual remota para o dia 28/09)

**Nome:** Caio Guilherme Batista Rodrigues 
**Disciplina:** Estrutura de Dados II &nbsp; **Professora:** Profa. Kadidja Valéria  
**Modalidade:** individual, remota e assíncrona &nbsp; **Tempo estimado:** 1 hora e 45 minutos

> A atividade pode ser realizada integralmente de casa. Não é necessário comparecer à faculdade.

## Objetivos de aprendizagem

- Retomar os conceitos de nó, raiz, pai, filho, folha, altura e percurso.
- Diferenciar as regras e aplicações dos tipos de árvores estudados.
- Relacionar analogias cotidianas às propriedades técnicas de cada estrutura.
- Justificar a escolha de uma árvore para um problema apresentado.

## Etapa 1 — Revisão bibliográfica (35 minutos)

Consulte as **referências bibliográficas indicadas no plano de ensino e os materiais disponibilizados na disciplina**. Inicie pelos conceitos básicos de árvore; depois estude árvore geral, árvore binária, árvore binária de busca (ABB), AVL, rubro-negra, B e B+.

Para cada estrutura, procure identificar: como os dados são organizados; qual propriedade deve ser mantida; como funcionam busca e inserção; que ajustes podem ocorrer após alterações; e em que contexto ela é útil. Redija com suas próprias palavras.

## Etapa 2 — Quadro comparativo (35 minutos)

Preencha todas as linhas pertinentes ao conteúdo da disciplina. Acrescente árvore geral, árvore binária, heap e trie quando forem abordadas nas referências ou aulas. A coluna de referência deve apontar a fonte específica usada para cada linha.

| Estrutura | Organização dos dados | Regra ou propriedade principal | Operação ou ajuste importante | Exemplo de aplicação | Referência consultada |
|---|---|---|---|---|---|
| Árvore binária de busca (ABB) | | | | | |
| AVL |Como qualqueem uma árvore binária de busca, os nós mantêm sua ordenação baseada em chaves: valores menores ficam à esquerda de um nó e valores maiores ficam à direita.
Na Árvore AVL, cada nó armazena uma propriedade extra chamada Fator de Balanceamento |Condição de Balanceamento de Adel’son-Vel’skii e Landis: Para todo nó da árvore, a diferença entre as alturas da subárvore esquerda ($h_E$) e da subárvore direita ($h_D$) deve ser no máximo $1$. Garantia de Altura: Devido a esse controle rígido de altura, a altura total de uma Árvore AVL com $n$ nós é mantida em $O(\log n)$, garantindo que a busca no pior caso continue sendo executada em tempo logarítmico. |Rotações Simples:
Rotação à Direita (LL): Aplicada quando a subárvore esquerda do filho esquerdo fica mais alta (caso esquerda-esquerda).
Rotação à Esquerda (RR): Aplicada quando a subárvore direita do filho direito fica mais alta (caso direita-direita).
Rotações Duplas:
Rotação Dupla Esquerda-Direita (LR): Consiste em uma rotação simples à esquerda no filho esquerdo, seguida de uma rotação simples à direita no nó desbalanceado.
Rotação Dupla Direita-Esquerda (RL): Consiste em uma rotação simples à direita no filho direito, seguida de uma rotação simples à esquerda no nó desbalanceado. |Garantia de Busca Eficiente: É aplicada em cenários nos quais o desempenho de busca no pior caso precisa ser estritamente $O(\log n)$, evitando o problema das ABBs comuns degenerarem em listas encadeadas de custo $O(n)$.Sistemas com Frequência Alta de Consultas/Buscas: Ideal para aplicações onde as operações de busca são muito mais frequentes do que as inserções e remoções, pois a árvore se mantém perfeitamente equilibrada ao custo de pequenos ajustes pontuais (rotações) quando ocorrem alterações. | DROZDEK (2018), cap. 6, seç. 6.7.2, p. 228-233 |
| Rubro-negra |Múltipla representação nos nós: além de manter a chave de dados e os ponteiros para os filhos como em uma ABB tradicional, cada nó armazena um bit extra que representa sua cor (Vermelho ou Preto).
Os nós nulos, as "folhas sem filho"são tratados conceitualmente como folhas pretas (NULL) |Propriedade da Cor: Todo nó é vermelho ou preto.
Propriedade da Raiz: A raiz é sempre preta.
Propriedade das Folhas: Todas as folhas (nós NULL) são pretas.
Propriedade do Nó Vermelho: Se um nó é vermelho, então ambos os seus filhos devem ser pretos (ou seja, não pode haver dois nós vermelhos consecutivos em um caminho).
Propriedade da Altura Preta: Para cada nó, todos os caminhos simples dele até qualquer uma de suas folhas descendentes contêm o mesmo número de nós pretos. |Recoloração: Mudança da cor dos nós (de vermelho para preto ou vice-versa) para restabelecer a propriedade sem alterar a topologia da árvore.
Rotações: Rotações para a esquerda ou para a direita, utilizadas para reorganizar a estrutura dos nós quando a recoloração isolada não resolve a violação |Sistemas Dinâmicos de Alto Desempenho: Ideal para cenários onde há uma quantidade equilibrada ou frequente de inserções, remoções e buscas, pois exige menos rotações para reequilibrar se comparada à Árvore AVL. | DROZDEK (2018), cap. 6, seç. 6.7.3, p. 233-239|
| B | | | | | |
| B+ | | | | | |

## Etapa 3 — Identificação por analogias (35 minutos)

Para **cada situação**, identifique a estrutura, justifique sua resposta com uma propriedade técnica e explique **um limite da analogia** (algo que a comparação não representa fielmente). Evite responder apenas com o nome da árvore.

1. Uma estante de números é reorganizada por rotações quando um lado fica alto demais em relação ao outro.
2. Um catálogo guarda várias chaves por página; quando uma página fica cheia, ela é dividida.
3. Uma fila mantém a tarefa de maior prioridade no topo para retirá-la primeiro.
4. Um índice percorre letras sucessivas e compartilha o início das palavras de mesmo prefixo.
5. Uma estrutura usa cores, recolorações e rotações para manter controlada a altura dos caminhos de busca.
6. Um índice conduz às folhas que contêm os registros, ligadas entre si para facilitar consultas por intervalo.
7. Numa coleção de números, cada nó direciona valores menores para a esquerda e maiores para a direita.

## Entrega

Organize as respostas em **um único PDF** ou utilize o modelo no formato **Markdown**, editando-o com seu nome e sua turma e seguindo a ordem das etapas 1 a 3. Inclua ao final as referências realmente consultadas.

Registre a atividade no seu GitHub. A atividade é individual; textos, justificativas e exemplos devem ser produzidos por você. A avaliação é participativa, e a atividade será discutida na aula subsequente.

**Critérios de participação:** consulta às referências da disciplina, precisão conceitual, justificativas próprias e clareza da apresentação e da discussão na aula subsequente.
