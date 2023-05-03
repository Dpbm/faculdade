#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define size 10

typedef struct stack{
  int top;
  int elements[size];
} Stack;

void init_stack(Stack *stack);
bool is_full(Stack *stack);
bool is_empty(Stack *stack);
void push(Stack *stack, int value);
void show_stack(Stack *stack);
void pop(Stack *stack);
int get_size(Stack *stack);
int get_top(Stack *stack);

int main(){
  Stack *stack = malloc(1 * sizeof(Stack));
  
  init_stack(stack);
  push(stack, 10);
  push(stack, 30);
  push(stack, 20);

  pop(stack);

  show_stack(stack);

  return 0;

}

void init_stack(Stack *stack){
  stack->top = -1;
}

void is_full(Stack *stack){
  return stack->top == size-1;
}

void is_empty(Stack *stack){
  return stack->top == -1;
}

void push(Stack *stack, int value){
  if(is_full(stack))
    return;

  stack->top++;
  stack->elements[stack->top] = value;
}

void show_stack(Stack *stack){
  int i;
  for(i = stack->top; i>=0; i--)
    printf("%d ", stack->elements[i]);
}

void pop(Stack *stack){
  if(is_empty(stack))
    return;
  //write penultimate element over last element
  stack->elements[stack->top] = stack->elements[stack->top-1];
  stack->top--;
}

int get_size(Stack *stack){
  if(is_empty(stack))
    return 0;


  return stack->top+1;
}

int get_top(Stack *stack){
  if(is_empty(stack))
    return 0;

  return stack->elements[stack->top];
}
