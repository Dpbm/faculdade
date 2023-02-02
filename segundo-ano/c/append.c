#include <stdio.h>
#include <stdlib.h>

void append(
  int *list,
  int *total_used_spaces_ptr, 
  int len,
  int value
){
  int total_used_spaces_value = *total_used_spaces_ptr;

  list[total_used_spaces_value] = value;
  *total_used_spaces_ptr = total_used_spaces_value + 1;
}

void show(int *list, int *total_used){
  int i;
  for(i = 0; i < *total_used; i++)
    printf("endereco %x valor %d\n", (list+i), *(list+i));
}

int main(){
  int total_used_list_cells = 0;
  int *total_used_list_cells_ptr  = &total_used_list_cells;

  int list_length = 10;
  int *list = malloc(list_length * sizeof(int));


  append(list, total_used_list_cells_ptr, list_length, 3);
  append(list, total_used_list_cells_ptr, list_length, 21);
  append(list, total_used_list_cells_ptr, list_length, 11);
  append(list, total_used_list_cells_ptr, list_length, 1);
  append(list, total_used_list_cells_ptr, list_length, 2);
  show(list, total_used_list_cells_ptr);

  return 0;
}
