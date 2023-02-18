#include <stdio.h>
#include <string.h>

int search(char *str, char car){
  int i = 0;

  while(str[i] != '\0'){
    if(str[i] == car) return i;
    i++;
  }

  return -1;
}

int main(){
  char str[20], car;

  puts("Palavra: ");
  gets(str);

  fflush(stdin);
  puts("Caractere: ");
  scanf("%c",&car);

  int pos = search(str, car);

  if (pos == -1) puts("Caractere nao existe na palavra!");
  else printf("caractere encontrado na posicao: %d", pos);


  return 0;
}
