#ifndef STACK
#define STACK 

#include <stdbool.h>


struct Stack{
	int value;
	struct Stack *next;
};

typedef struct Stack Stack;
typedef struct Stack Item; 

void initialize_stack(Stack **stack);
void push(Stack **stack, int value);
int read(Stack *stack);
void pop(Stack **stack);
Item *create_item(Item *top, int value);
bool is_empty(Stack *stack);
#endif
