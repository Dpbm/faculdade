#include <stdio.h>

int main() {
  char nome[30];
  int idade;

  printf("Seu nome: ");
  // fgets(nome, 30, stdin);
  scanf("%[^\n]s", &nome);

  printf("Sua idade: ");
  scanf("%d", &idade);

  printf("\n%s tem %d anos de idade!\n", nome, idade);

  return 0;
}
