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
| Árvore binária de busca (ABB) |Ordenação por Comparação: A posição de cada valor orienta a procura e a organização.   Valores Menores: Seguem/ficam para a esquerda de um determinado nó.   Valores Maiores: Seguem/ficam para a direita de um determinado nó.   Forma da Árvore: Pode variar entre mais equilibrada ou degenerada, dependendo da ordem em que os dados são inseridos. |Regra de Direcionamento:Se o valor procurado/inserido for menor que o nó atual $\rightarrow$ siga à esquerda.   Se o valor procurado/inserido for maior que o nó atual $\rightarrow$ siga à direita.   Sem Duplicados: A convenção adotada na aula estabelece que não há valores duplicados na árvore.   Condição de Parada da Busca: A busca encerra/para quando o valor é encontrado ou quando se atinge uma posição vazia (None).   Impacto no Custo: A ordem de inserção define o número de comparações e o custo da busca:Árvore mais equilibrada: A busca tende a ter complexidade $O(\log n)$.   Árvore degenerada: Pior caso de busca tem complexidade $O(n)$.    |Inserção Guiada:Compara-se o novo valor com o nó atual .   Decide-se ir para a esquerda (se menor) ou para a direita (se maior).   Repete-se a comparação até encontrar uma posição vazia onde o novo nó será inserido.   Busca Básica: 
Compare: Verifica se o valor procurado é igual ao nó atual.   Decida: Se menor, navegue para a esquerda; se maior, navegue para a direita.   Repita: Continue navegando pelo caminho até encontrar o elemento ou alcançar o fim  | | |
| AVL | | | | | |
| Rbro-negra | | | | | |
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
