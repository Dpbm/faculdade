#include <stdio.h>
#include "../stack.h"

void test_push(Stack **stack);
void test_read(Stack *stack);
void test_empty_stack(Stack **stack);
void test_pop_just_one_on_stack(Stack **stack);
void test_pop_with_multiple_values_on_stack(Stack **stack);
void test_create_item();
void test_is_empty_true();
void test_is_empty_false();

int main(){
    Stack *stack;
    initialize_stack(&stack);

    test_create_item();

    test_empty_stack(&stack);
    
    test_push(&stack);
    test_read(stack);

    test_pop_just_one_on_stack(&stack);
    test_pop_with_multiple_values_on_stack(&stack);
    
    test_is_empty_true();
    test_is_empty_false();


    return 0;
}

void test_create_item(){
    Stack *stack;
    initialize_stack(&stack);
    Stack *item = create_item(stack, 10);
    if(item->value == 10 && item->next == NULL)
        printf("[0] test_create_item works!\n");
}


void test_empty_stack(Stack **stack){
    pop(stack);
    if((*stack) == NULL)
        printf("[1] test_empty_stack works!\n");
}

void test_push(Stack **stack){
    push(stack, 1);
    if((*stack)->value == 1)
        printf("[2] test_push works!\n");
}

void test_read(Stack *stack){
    int value = read(stack);
    if(value == 1)
        printf("[3] test_read works!\n");
}

void test_pop_just_one_on_stack(Stack **stack){
    pop(stack);
    if((*stack) == NULL)
        printf("[4] test_just_one_on_stack works!\n");
}

void test_pop_with_multiple_values_on_stack(Stack **stack){
    push(stack, 1);
    push(stack, 2);
    push(stack, 3);
    push(stack, 4);
    pop(stack);

    if((*stack)->value == 3)
        printf("[5] test_pop_with_multiple_values_on_stack works!\n");
}

void test_is_empty_true(){
    Stack *stack;
    initialize_stack(&stack);
    if(is_empty(stack))
        printf("[6] test_is_empty_true works!\n");
}

void test_is_empty_false(){
    Stack *stack;
    initialize_stack(&stack);
    push(&stack, 1);
    if(is_empty(stack))
        printf("[7] test_is_empty_false works!\n");
}