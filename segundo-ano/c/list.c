#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node{
  int value;
  struct Node* next;
};

typedef struct Node Node;
typedef struct Node LinkedList;

void initializeList(LinkedList **list);
void append(LinkedList **list, int value, Node **lastNode);
void showList(LinkedList *list);
Node* generateNode(int value);
bool isAnEmptyList(LinkedList *list);
void insert_first_value(LinkedList **list, Node *node);
void updateLastNode(Node **lastNode, Node *newNode);
void insertAtLastNode(LinkedList **list, Node **lastNode, int value);
void removeFirstNode(LinkedList **list, Node **lastNode);
void clearLastNode(Node **lastNode);
bool hasJustANode(LinkedList *list);
void removeNode(Node *node);

int main(){
  LinkedList *list;
  Node *lastNode;
  initializeList(&list);

  append(&list, 1, &lastNode);
  append(&list, 2, &lastNode);
  append(&list, 3, &lastNode);
  append(&list, 3, &lastNode);
  append(&list, 5, &lastNode);
  
  removeFirstNode(&list, &lastNode);

  showList(list);
  printf("\nlast Node %d", lastNode->value);
  return 0;
}

void initializeList(LinkedList **list){
  *list = NULL;
}

void append(LinkedList **list, int value, Node **lastNode){
  Node *newNode = generateNode(value);

  updateLastNode(lastNode, newNode);


  if(isAnEmptyList(*list)){
    insert_first_value(list, newNode);
    return;
  }

  Node* actualNode = *list;
  while(actualNode->next != NULL)
    actualNode = actualNode->next;

  actualNode->next = newNode;
}

void insert_first_value(LinkedList **list, Node *node){
  *list = node;
}

bool isAnEmptyList(LinkedList *list){
  return list == NULL;
}

Node* generateNode(int value){
  Node* newNode = calloc(1, sizeof(Node));
  newNode->value = value;
  newNode->next = NULL;
  return newNode;
}

void showList(LinkedList *list){
  Node* actualNode = list;
  while(actualNode != NULL){
    printf("%d ", actualNode->value);
    actualNode = actualNode->next;
  }
}

void updateLastNode(Node **lastNode, Node *newNode){
    *lastNode = newNode;
}


void insertAtLastNode(LinkedList **list, Node **lastNode, int value){
    Node* newNode = generateNode(value);

    if(isAnEmptyList(*list)){
        insert_first_value(list, newNode);
        updateLastNode(lastNode, newNode);
        return;
    }

    (*lastNode)->next = newNode;
    updateLastNode(lastNode, newNode);
}

void removeFirstNode(LinkedList **list, Node **lastNode){
    Node *firstNode = *list;

    if(isAnEmptyList(firstNode))
        return;

    if(hasJustANode(firstNode)){
        removeNode(firstNode);
        initializeList(list);
        clearLastNode(lastNode);
        return;
    }

    *list = firstNode->next;
    removeNode(firstNode);
}

void removeNode(Node *node){
    free(node);
}

void clearLastNode(Node **lastNode){
    *lastNode = NULL;
}

bool hasJustANode(LinkedList *list){
    return list->next == NULL;
}