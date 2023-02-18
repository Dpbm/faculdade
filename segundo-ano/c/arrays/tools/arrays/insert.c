#include <stdlib.h>

#include "utils/array.h"
#include "insert.h"

void insert_int(int *list, int value, int index, int *array_size, int *last_index){
  if (index > *array_size || index < 0)
    return;

  int total_values = *array_size + 1;

  update_size_pointer(array_size, total_values, sizeof(int));
  realloc_list_int(list, total_values);
  update_index(last_index);

  int i = total_values;
  while (i > index){
    list[i] = list[i-1];
    i--;
  }

  list[index] = value;
}


