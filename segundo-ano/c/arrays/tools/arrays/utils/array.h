#ifndef ARRAY_UTILS_H_
#define ARRAY_UTILS_H_

void update_index(int *actual_index);
void update_size_pointer(int *array_size, int total_values, int type_size);
void realloc_list_int(int *list, int total_values);
void realloc_list_char(char *list, int total_values);
void realloc_list_float(float *list, int total_values);
void realloc_list_long(long *list, int total_values);
void realloc_list_long_long(long long *list, int total_values);
void realloc_list_double(double *list, int total_values);

#endif
