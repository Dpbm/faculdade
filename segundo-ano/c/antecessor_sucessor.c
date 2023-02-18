#include <stdio.h>

void get_antecessor(int num, int* antecessor);
void get_sucessor(int num, int* sucessor);

int main(){
  int num;

  printf("Digite um valor: ");
  scanf("%d", &num);

  int antecessor, sucessor;
  get_antecessor(num, &antecessor);
  get_sucessor(num, &sucessor);

  printf("Sucessor: %d\nAntecessor: %d", sucessor, antecessor);
  return 0;
}


void get_antecessor(int num, int* antecessor){ *antecessor = num-1; }
void get_sucessor(int num, int* sucessor){ *sucessor = num+1; }
