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
| Árvore binária de busca (ABB) |Os valores menores ficam à esquerda e os maiores à direita de cada nó. A forma da árvore depende da ordem em que os valores são inseridos.| Para procurar ou inserir um valor, comparamos com o nó atual. Se for menor, vamos para a esquerda; se for maior, para a direita. A árvore pode ficar equilibrada ou ficar parecida com uma lista.|Na inserção, o valor é comparado com os nós até encontrar um espaço vazio. Na busca, seguimos o mesmo caminho até encontrar o valor ou chegar a uma posição vazia. |Expressões aritméticas e compiladores ou sistemas simples de cadastro onde a ordem dos elementos é inserida de forma semi-balanceada por padrão. | DROZDEK (2018), cap. 6, p. 186-193 |
| AVL |Funciona como uma árvore binária de busca, mantendo os valores menores à esquerda e os maiores à direita. Além disso, controla a altura dos dois lados da árvore. |A diferença de altura entre a esquerda e a direita de cada nó não pode ser maior que 1. Isso mantém a árvore equilibrada e deixa a busca mais rápida. |Quando a árvore fica desequilibrada, são feitas rotações simples ou duplas para corrigir sua estrutura. |Mecanismos de busca em memória e dicionários em tempo de execução onde operações de busca, inserção e exclusão precisam ser garantidamente rápidas, como tabelas de símbolos em compiladores. |DROZDEK (2018), cap. 6, p. 223-227 |
| Rubro-negra |Mantem a chave de dados e os ponteiros para os filhos como em uma ABB tradicional, Mas cada nó tem sua cor (Vermelho ou Preto) e os nós nulos são como folhas pretas. |Existem regras para as cores dos nós. A raiz é preta e não podem existir dois nós vermelhos seguidos. Essas regras ajudam a manter a árvore equilibrada. |Depois de uma inserção ou remoção, podem ser feitas recolorações e rotações para corrigir a árvore. |Gerenciamento de memória em sistemas operacionais, como a biblioteca padrão do C++ |DROZDEK (2018), cap. 6, p. 233-239 |
| B |Cada nó pode guardar várias chaves e vários filhos. As chaves ficam organizadas em ordem e ajudam a indicar para qual parte da árvore devemos ir. |Existe um limite de chaves e filhos em cada nó. Todas as folhas ficam no mesmo nível, mantendo a árvore balanceada. |Quando um nó fica cheio durante uma inserção, ele pode ser dividido em dois e uma chave é passada para o nó pai. Na remoção, pode ocorrer empréstimo ou junção de nós.|Amplamente aplicada na organização física de blocos em sistemas de arquivos de sistemas operacionais (ex.: NTFS). |DROZDEK (2018), cap. 7, p. 271-278 |
| B+ |SOs nós internos funcionam como índices, enquanto os dados ficam nas folhas. As folhas também são ligadas umas às outras para facilitar a leitura em sequência. |Os dados são acessados pelas folhas e todas elas ficam no mesmo nível. As folhas também ficam conectadas entre si. |Quando uma folha fica cheia, ela é dividida. Na remoção, pode acontecer redistribuição ou junção de folhas. | É a estrutura mais utilizada na implementação prática de índices em SGBDs modernos, onde consultas do tipo Range Query são extremamente frequentes, támbem utilizada para organizar diretórios e mapeamentos de arquivos grandes em disco de forma contínua e sequencial. |DROZDEK (2018), cap. 7, p. 280-285 |
| Heap |É uma árvore binária que normalmente é armazenada em um vetor, sem precisar de ponteiros para cada nó.|Tem o max-heap e o min-heap.No Max-Heap, o maior valor fica na raiz e cada pai é maior ou igual aos seus filhos. No Min-Heap, acontece o contrário. |Ao inserir, o novo elemento pode subir até sua posição correta. Ao remover a raiz, o último elemento ocupa seu lugar e pode descer para reorganizar a árvore. |Em softwares médicos de pronto-socorro, os pacientes são organizados com base na gravidade do seu estado de saúde, e não na ordem de chegada. O paciente com maior gravidade fica no topo do heap. |DROZDEK (2018), cap. 6, p. 234-236 |
| Trie |Os dados são separados por caracteres. Palavras que começam com as mesmas letras compartilham o mesmo caminho na árvore. |Cada nível representa uma letra. A busca depende principalmente do tamanho da palavra, e não da quantidade de palavras armazenadas. |Cada nível representa uma letra. A busca depende principalmente do tamanho da palavra, e não da quantidade de palavras armazenadas. |Quando você começa a digitar uma palavra, o sistema sugere o restante. A Trie percorre o "caminho" das letras digitadas e encontra instantaneamente todas as palavras armazenadas que compartilham aquele mesmo prefixo. |DROZDEK (2018), cap. 7, p. 317-323|

## Etapa 3 — Identificação por analogias (35 minutos)

Para **cada situação**, identifique a estrutura, justifique sua resposta com uma propriedade técnica e explique **um limite da analogia** (algo que a comparação não representa fielmente). Evite responder apenas com o nome da árvore.

1. Uma estante de números é reorganizada por rotações quando um lado fica alto demais em relação ao outro.
- **Estrutura:** Árvore AVL
- **Propriedade técnica que justifica:** É uma árvore de busca balanceada por altura. Após inserções ou remoções, rotações são usadas para manter a diferença de altura entre as subárvores dentro do limite permitido.
- **Limite da analogia:** A estante sugere apenas uma organização física. Na árvore real, o balanceamento é calculado matematicamente pelas alturas das subárvores; não é simplesmente “arrumar” visualmente um lado.
2. Um catálogo guarda várias chaves por página; quando uma página fica cheia, ela é dividida.
- **Estrutura:** Árvore B
- **Propriedade técnica que justifica:** Cada nó pode armazenar várias chaves e vários filhos. Quando um nó atinge sua capacidade, ocorre uma divisão (split) para manter a estrutura balanceada.
- **Limite da analogia:** A “página” não é literalmente uma folha de papel: em sistemas de armazenamento, ela normalmente representa um bloco de memória/disco que pode conter vários registros ou chaves.
3. Uma fila mantém a tarefa de maior prioridade no topo para retirá-la primeiro.
- **Estrutura:** Heap
- **Propriedade técnica que justifica:** O elemento de maior prioridade fica na raiz de um max-heap (ou o de menor prioridade, em um min-heap), permitindo sua remoção eficiente.
- **Limite da analogia:** Uma fila comum sugere que o primeiro elemento inserido sai primeiro, seria "FIFO", mas um heap não segue FIFO; a prioridade determina a ordem de remoção.
4. Um índice percorre letras sucessivas e compartilha o início das palavras de mesmo prefixo.
- **Estrutura:** Trie
- **Propriedade técnica que justifica:** Cada nível representa normalmente um caractere, e palavras que possuem o mesmo prefixo compartilham os mesmos nós iniciais.
- **Limite da analogia:** A analogia com um índice de palavras não representa que todas as palavras necessariamente ocupem um caminho completo separado; os prefixos comuns são justamente compartilhados, economizando comparações em determinadas operações.
5. Uma estrutura usa cores, recolorações e rotações para manter controlada a altura dos caminhos de busca.
- **Estrutura:** Árvore Rubro-Negra
- **Propriedade técnica que justifica:** Os nós possuem uma cor (vermelho ou preto) e regras de coloração garantem que os caminhos não fiquem excessivamente desbalanceados. Rotações e recolorações corrigem violações após alterações.
- **Limite da analogia:** “Controlar a altura” não significa manter todos os caminhos com a mesma altura. A árvore é apenas aproximadamente balanceada, com uma altura limitada em relação ao número de nós.
6. Um índice conduz às folhas que contêm os registros, ligadas entre si para facilitar consultas por intervalo.
- **Estrutura:** Árvore B+
- **Propriedade técnica que justifica:** Os registros/dados ficam nas folhas, e as folhas são geralmente conectadas por ponteiros, permitindo percorrê-las sequencialmente e realizar consultas por intervalo com eficiência.
- **Limite da analogia:** A analogia de “conduzir às folhas” pode sugerir que os dados estão espalhados por todos os níveis; na B+, os nós internos funcionam principalmente como índices, enquanto os registros ficam nas folhas.
7. Numa coleção de números, cada nó direciona valores menores para a esquerda e maiores para a direita.
- **Estrutura:** Árvore Binária de Busca
- **Propriedade técnica que justifica:** Para cada nó, os valores da subárvore esquerda são menores e os da subárvore direita são maiores, permitindo buscar valores seguindo comparações.
- **Limite da analogia:** Essa regra, sozinha, não garante balanceamento. Se os valores forem inseridos em uma ordem desfavorável, a árvore pode ficar parecida com uma lista e perder eficiência.

## Entrega

Organize as respostas em **um único PDF** ou utilize o modelo no formato **Markdown**, editando-o com seu nome e sua turma e seguindo a ordem das etapas 1 a 3. Inclua ao final as referências realmente consultadas.

Registre a atividade no seu GitHub. A atividade é individual; textos, justificativas e exemplos devem ser produzidos por você. A avaliação é participativa, e a atividade será discutida na aula subsequente.

**Critérios de participação:** consulta às referências da disciplina, precisão conceitual, justificativas próprias e clareza da apresentação e da discussão na aula subsequente.
