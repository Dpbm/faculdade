#include "append.h"
#include "utils/array.h"

void append_int(int *list, int value, int *actual_index, int *array_size){
  list[*actual_index] = value;
  
  update_index(actual_index);
  update_size_pointer(array_size, *actual_index, sizeof(int));
  realloc_list_int(list, *actual_index);

}
