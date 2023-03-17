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
void show_list(LinkedList *list);
void insert_after_value(LinkedList **list, int target, int newNodeValue);
void insert_before_value(LinkedList **list, int target, int newNodeValue);
Node* generate_node(int value);
void insert_sorted(LinkedList **list, int value);
bool is_an_empty_list(LinkedList *list);
void insert_first_value(LinkedList **list, Node *node);
void insert_sorted(LinkedList **list, int value);

int main(){
  LinkedList *list;
  initialize_list(&list);

  /*append(&list, 10);
  append(&list, 11);
  append(&list, 12);
  append(&list, 13);
  append(&list, 14);
  append(&list, 15);
  append(&list, 16);

  insert_after_value(&list, 10, 0);
  insert_after_value(&list, 20, 0);
  insert_after_value(&list, 16, 0);
  insert_after_value(&list, 12, 0);
  
  insert_before_value(&list, 10, 1);
  insert_before_value(&list, 20, 1);
  insert_before_value(&list, 16, 1);
  insert_before_value(&list, 12, 1);
  */
  insert_sorted(&list, 3);
  insert_sorted(&list, 5);
  insert_sorted(&list, 4);
  insert_sorted(&list, 3);
  insert_sorted(&list, 4);
  insert_sorted(&list, 0);
  insert_sorted(&list, -10);
  insert_sorted(&list, -1);
  insert_sorted(&list, 1);

  show_list(list);
  return 0;
}

void initialize_list(LinkedList **list){
  *list = NULL;
}

void append(LinkedList **list, int value){
  Node *newNode = generate_node(value);

  if(is_an_empty_list(*list)){
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

bool is_an_empty_list(LinkedList *list){
  return list == NULL;
}

Node* generate_node(int value){
  Node* newNode = calloc(1, sizeof(Node));
  newNode->value = value;
  newNode->next = NULL;
  return newNode;
}

void show_list(LinkedList *list){
  Node* actualNode = list;
  while(actualNode != NULL){
    printf("%d ", actualNode->value);
    actualNode = actualNode->next;
  }
}


void insert_after_value(LinkedList **list, int target, int newNodeValue){
  Node* actualNode = *list;
  while(actualNode != NULL && actualNode->value != target)
    actualNode = actualNode->next;
 
  if(actualNode == NULL || actualNode->value != target)
    return;

  Node* newNode = generate_node(newNodeValue);
  newNode->next = actualNode->next;
  actualNode->next = newNode;
}

void insert_before_value(LinkedList **list, int target, int newNodeValue){

  Node* actualNode = *list;
  Node* newNode = generate_node(newNodeValue);

  if(target == actualNode->value){
    newNode->next = actualNode;
    *list = newNode;
    return;
  } 

  while(actualNode->next != NULL && actualNode->next->value != target)
    actualNode = actualNode->next;

  if(actualNode->next == NULL)
    return;

  newNode->next = actualNode->next;
  actualNode->next = newNode;
}

void insert_sorted(LinkedList **list, int value){
  Node* newNode = generate_node(value);
 
  Node* actualNode = *list;

  if(is_an_empty_list(actualNode)){
    insert_first_value(list, newNode);
    return;
  }

  if(value <= actualNode->value){
    insert_before_value(list, actualNode->value, value);
    return;
  }
  
  while(actualNode->next != NULL && actualNode->next->value < value)
    actualNode = actualNode->next;

  newNode->next = actualNode->next;
  actualNode->next = newNode;  
}

