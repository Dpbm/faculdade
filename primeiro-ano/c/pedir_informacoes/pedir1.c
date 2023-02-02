#include <stdio.h>

int main() {
  char nome[30];
  int idade;

  printf("Seu nome: ");
  scanf("%s", &nome);

  printf("Sua idade: ");
  scanf("%d", &idade);

  printf("\n%s tem %d anos de idade!\n", nome, idade);

  return 0;
}
