#include <stdlib.h>

void update_index(int *actual_index){
  (*actual_index)++;
}

void update_size_pointer(int *array_size, int total_values, int type_size){
  (*array_size) = total_values * type_size;
}

void realloc_list_int(int *list, int total_values){
  list = realloc(list, total_values * sizeof(int));
}

void realloc_list_char(char *list, int total_values){
  list = realloc(list, total_values * sizeof(char));
}

void realloc_list_float(float *list, int total_values){
  list = realloc(list, total_values * sizeof(float));
}

void realloc_list_long(long *list, int total_values){
  list = realloc(list, total_values * sizeof(long));
}

void realloc_list_long_long(long long *list, int total_values){
  list = realloc(list, total_values * sizeof(long long));
}
void realloc_list_double(double *list, int total_values){
  list = realloc(list, total_values * sizeof(double));
}
