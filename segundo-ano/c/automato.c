#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define ALPHABET_SIZE 1

typedef struct Transition {
  char symbol;
  struct State *next;
} Transition;

typedef struct State{
  char *name;
  struct Transition *transitions[ALPHABET_SIZE];
  int last_transition_index;
  bool final;
} State;

State *init_state(char *name);
void add_transition(char symbol, State *next, State **parent);
void append_transition(State **state, Transition *transition);
bool correct_word(State *first_state, char *input_word);

int main(int argc, char *argv[]){
  char *input_word = argv[1];

  State *q0 = init_state("q0");
  State *q1 = init_state("q1");
  q0->final = true;

  add_transition('a', q1, &q0);
  add_transition('a', q0, &q1);

  if(correct_word(q0, input_word))
    printf("correct!!!");
  else
    printf("Wrong!!!");

  return 0;
}

State *init_state(char *name){
  State *state = calloc(1, sizeof(State));
  state->name = name;
  state->final = false;
  state->last_transition_index = -1;
  return state;
}

void add_transition(char symbol, State *next, State **parent){
  Transition *transition = calloc(1, sizeof(Transition));
  transition->symbol = symbol;
  transition->next = next;

  append_transition(parent, transition);
}

void append_transition(State **state, Transition *transition){
  int new_last_index = (*state)->last_transition_index+1;
  (*state)->transitions[new_last_index] = transition;
  (*state)->last_transition_index = new_last_index;
}

bool correct_word(State *first_state, char *input_word){
  int actual_index = 0;
  char letter = input_word[actual_index];
  State *actual_state = first_state;

  while(letter != '\0'){
    printf("state: %s; letter: %c; ", actual_state->name, letter);

    for(int i = 0; i < ALPHABET_SIZE; i++){
      Transition *actual_transition = actual_state->transitions[i];
      if(actual_transition->symbol == letter){
        actual_state = actual_transition->next;
        printf("new state: %s", actual_state->name);
        break;
      }
    }

    printf("\n");
    actual_index++;
    letter = input_word[actual_index];
  }
  return actual_state->final;
}

