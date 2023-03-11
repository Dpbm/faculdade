#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node{
  int value;
  struct Node* next;
};

typedef struct Node Node;
typedef struct Node LinkedList;

void initialize_list(LinkedList **list);
void append(LinkedList **list, int value);
Node* generateNode(int value);
bool isEmptyList(LinkedList *list);
void insertNextNode(Node *previousNode, Node *newNode);
void show(LinkedList *list);

int main(){
  LinkedList *list;
  initialize_list(&list);

  append(&list, 10);
  append(&list, 20);
  append(&list, 30);
  append(&list, 40);
  append(&list, 50);
  show(list);
  return 0;
}

void initialize_list(LinkedList **list){
  *list = NULL;
}

void append(LinkedList **list, int value){
  Node *newNode = generateNode(value);

  if(isEmptyList(*list))
    *list = newNode;

  Node *actualNode = *list;
  while(actualNode->next != NULL)
    actualNode = actualNode->next;

  insertNextNode(actualNode, newNode); 
}

Node* generateNode(int value){
  Node *newNode = malloc(1 * sizeof(Node));
  newNode->value = value;
  newNode->next = NULL;
  return newNode;
}

bool isEmptyList(LinkedList *list){
  return list == NULL;
}

void insertNextNode(Node *previousNode, Node* newNode){
  previousNode->next = newNode;
}

void show(LinkedList *list){
  Node *actualNode = list;
  while(actualNode != NULL){
    printf("value  %d\n", actualNode->value);
    printf("actual %x\n", actualNode);
    printf("next   %x\n", actualNode->next);
    actualNode = actualNode->next;
  }
}

