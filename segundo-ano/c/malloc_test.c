#include <stdio.h>
#include <stdlib.h>

int main(){
  int list_length = 10;
  int *list_length_ptr = &list_length;
  int *list = malloc(list_length * sizeof(int));

  int i;
  *list_length_ptr = 20;

  for(i = 0; i < list_length; i++)
    list[i] = 1;

  for(i = 0; i < list_length; i++)
    printf("%d\n", list[i]);

  *list_length_ptr = 30;

  for (i = 0; i < list_length; i++) 
    list[i] = 1;

  printf("Trinta agora\n");
  for (i = 0; i < list_length; i++) 
    printf("%d\n", list[i]);


  return 0;
}
