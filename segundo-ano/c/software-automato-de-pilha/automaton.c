#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "stack.h"
#include "automaton.h"

void invalid_word(){
    printf("Palavra invalida!");
    exit(EXIT_FAILURE);
}

char q1(char letter, Stack **stack){
    if(letter == 'a'){
        push(stack, 1);
        return '1';
    }
    else if(letter == 'b') {
        if(is_empty(*stack))
            invalid_word();
        pop(stack);
        return '2';
    }
}


void q2(char letter, Stack **stack){
    if(letter == 'b'){
        if(is_empty(*stack))
            invalid_word();
        pop(stack);
    }
    else invalid_word();
}
