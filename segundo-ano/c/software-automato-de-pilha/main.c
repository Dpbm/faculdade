#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "automaton.h"

int main(){

	char *word = (char*)calloc(MAX_CHAR, sizeof(char));

	printf("Alfabeto: {a, b}\n");
	printf("Maximo de caracteres: 40\n");
	printf("Digite a Palavra: ");
	fgets(word, MAX_CHAR, stdin);

	if(strlen(word) == 1)
		invalid_word();
	else if(word[0] != 'a')
		invalid_word();
		
	Stack *stack;
	initialize_stack(&stack);
	char state = '1';

	int index;
	for(index = 0; index < strlen(word)-1; index++){
		char letter = word[index];

		if(state == '1')
			state = q1(letter, &stack);
		else
			q2(letter, &stack);
	}

	if(!is_empty(stack))
		invalid_word();
	printf("Palavra valida!");

	return 0;
}
