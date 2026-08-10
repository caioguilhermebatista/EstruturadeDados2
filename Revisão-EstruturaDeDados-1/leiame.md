Abaixo temos uma das minhas atividades práticas que da qual gostei de fazer no semestre passado, é um programa que ajuda uma bibliotacária escolar na organização de certos livros disponíveis na biblioteca, separa os livros em categorias e estado de conservação, e ao final do código mostra a quantidade de livros por categoria os livros novos na categoria de matemática.

O código utiliza de estruturas de repetição e estruturas de decisão.

#include <stdio.h>
int main() {
  int i;
  int categoria, conservacao;
  int matematica = 0, ciencias = 0, geografia = 0;
  int matNovos = 0;
  for (i = 1; i <= 15; i++) {
    printf("Livro %d\n", i);
    printf("Categoria (1-Matematica, 2-Ciencias, 3-Geografia): ");
    scanf("%d", &categoria);
    printf("Conservacao (1-Novo, 2-Bom, 3-Ruim): ");
    scanf("%d", &conservacao);
    if (categoria == 1) {
      matematica++;
      if (conservacao == 1) {
        matNovos++;
      }
    }
    else if (categoria == 2) {
      ciencias++;
    }
    else if (categoria == 3) {
      geografia++;
    }
    printf("\n");
  }
  printf("Quantidade de livros por categoria:\n");
  printf("Matematica: %d\n", matematica);
  printf("Ciencias: %d\n", ciencias);
  printf("Geografia: %d\n", geografia);
  printf("\nLivros novos na categoria Matematica: %d\n", matNovos);
  return 0;
}

