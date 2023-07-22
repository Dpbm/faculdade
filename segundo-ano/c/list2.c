#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node{
  int value;
  struct Node* next;
  struct Node* previous;
};

typedef struct Node Node;
typedef struct Node LinkedList;

void initialize_list(LinkedList **list);
void append(LinkedList **list, int value, Node **lastNode);
void show_list(LinkedList *list);
Node* generate_node(int value);
bool is_an_empty_list(LinkedList *list);
void insert_first_value(LinkedList **list, Node *node);
void updateLastNode(Node **lastNode, Node *newNode);
void show_reverse(Node *lastNode);

int main(){
  LinkedList *list;
  Node *lastNode;
  initialize_list(&list);

  append(&list, 12, &lastNode);
  append(&list, 13, &lastNode);
  append(&list, 14, &lastNode);
  append(&list, 15, &lastNode);
  append(&list, 16, &lastNode);

  show_reverse(lastNode);
  return 0;
}

void initialize_list(LinkedList **list){
  *list = NULL;
}


void append(LinkedList **list, int value, Node **lastNode){
  Node *newNode = generate_node(value);

  updateLastNode(lastNode, newNode);

  if(is_an_empty_list(*list)){
    insert_first_value(list, newNode);
    return;
  }

  Node* actualNode = *list;
  while(actualNode->next != NULL)
    actualNode = actualNode->next;

  actualNode->next = newNode;
  newNode->previous = actualNode;
}

Node* generate_node(int value){
  Node* newNode = calloc(1, sizeof(Node));
  newNode->value = value;
  newNode->next = NULL;
  newNode->previous = NULL;
  return newNode;
}

void updateLastNode(Node **lastNode, Node *newNode){
    *lastNode = newNode;
}

bool is_an_empty_list(LinkedList *list){
  return list == NULL;
}

void insert_first_value(LinkedList **list, Node *node){
  *list = node;
}

void show_list(LinkedList *list){
  Node* actualNode = list;
  while(actualNode != NULL){
    printf("%d ", actualNode->value);
    actualNode = actualNode->next;
  }
}

void show_reverse(Node *lastNode){
    Node* actualNode = lastNode;
    while(actualNode != NULL){
        printf("%d ", actualNode->value);
        actualNode = actualNode->previous;
    }
}