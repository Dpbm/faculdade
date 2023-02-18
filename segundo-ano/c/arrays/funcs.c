#include <stdio.h>
#include <stdlib.h>

#include "tools/arrays/append.h"
#include "tools/arrays/insert.h"

int main(){
  int start_position = 0;
  int alloc_size = (start_position + 1) * sizeof(int);

  int *array = malloc(alloc_size);

  int *index = &start_position;
  int *array_size = &alloc_size;

  
  append_int(array, 10, index, array_size);
  append_int(array, 10, index, array_size);
  append_int(array, 10, index, array_size);
  insert_int(array, 3, 1, array_size, index);

  int i;
  for(i = 0; i < *index; i++)
    printf("%d ", array[i]);

  return 0;
}
