#include <stdlib.h>
#include <stdbool.h>
#include "stack.h"

void initialize_stack(Stack **stack){
	(*stack) = NULL;
}

void push(Stack **stack, int value){
	Stack *item = create_item(*stack, value);
	*stack = item;
}

int read(Stack *stack){
	return stack->value;
}

void pop(Stack **stack){
	if((*stack) == NULL)
		return;

	if((*stack)->next == NULL){
		free((*stack)->next);
		initialize_stack(stack);
		return;
	}

	Stack *old_first = *stack;
	Stack *next = (*stack)->next;
	free(old_first);
	(*stack) = next;
}

Item *create_item(Item *top, int value){
	Item *item = (Item*)calloc(1, sizeof(Item));
	item->value = value;
	item->next = top;
	return item;
}

bool is_empty(Stack *stack){
	return stack == NULL;
}