#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node{
  struct Node* next;
  int value;
};
typedef struct Node Node;
typedef struct Node Stack;

void init_stack(Stack **stack);
void push(Stack **stack, int value);
Node *generate_node(int value);
void show_stack(Stack *stack);
Node *top(Stack *stack);
int get_size(Stack *stack);
bool is_empty(Stack *stack);

int main(){
  Stack *stack;

  init_stack(&stack);

  push(&stack, 10);
  push(&stack, 20);
  push(&stack, 30);

  pop(&stack);

  show_stack(stack);

  return 0;
}

void init_stack(Stack **stack){
  *stack = NULL;
}

void push(Stack **stack, int value){
  Node *firstNode = *stack;
  Node *newNode = generate_node(value);
  newNode->net = firstNode;
  *stack = newNode;
}

Node *generate_node(int value){
  Node *newNode = malloc(1 * sizeof(Node));
  newNode->next = NULL;
  newNode->value = value;
  return newNode;
}

void show_stack(Stack *stack){
  Node *actualNode = stack;
  while(actualNode != NULL){
    printf("%d ", actualNode->value);
    actualNode = actualNode->next;
  }
}

void pop(Stack **stack){
  Node *firstNode = *stack;
  *stack = firstNode->next;
  free(firstNode);
}

Node *top(Stack *stack){
  return stack;
}

int get_size(Stack *stack){
  int total = 0;
  Node *actualNode = stack;
  while(actualNode != NULL){
    total++;
    actualNode = actualNode->next;
  }
  return total;
}

bool is_empty(Stack *stack){
  return stack == NULL;
}
