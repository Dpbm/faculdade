#include <stdio.h>

int main(){
  int *memory_start_index;
  int starting_value = 1;

  memory_start_index = &starting_value;

  printf("Starting Point: %x\nStarting content: %d\n", memory_start_index, *memory_start_index)
  printf("--------------------------------\n");
  
  while ((long long)memory_start_index <= 0xffffff){
    printf("%c", *memory_start_index);
    memory_start_index++
  }

  return 0;
}
