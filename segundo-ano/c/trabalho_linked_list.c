#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node{
  int value;
  struct Node* next;
};

typedef struct Node Node;
typedef struct Node LinkedList;

void menu();
int getUserOption();
void execSelectedFuntion(LinkedList **list, int function);
void addUserInputToList();
void initializeList(LinkedList **list);
void append(LinkedList **list, int value);
Node* getNewNode(int value);
bool isAnEmptyList(LinkedList *list);
void insertFirstValueIntoList(LinkedList **list, Node *newNode);
Node* getLastNode(LinkedList **list);
void setNextNode(Node *node, Node *newNode);
void showList(LinkedList *list);
void removeDuplicateNodes(LinkedList **list);
bool hasJustANode(LinkedList *list);
void removeValuesEqualTo(Node *startPoint, int value);
void removeNode(Node **node);

int main(){
    LinkedList *list;
    initializeList(&list);

	int userOption = NULL;

	do{
		menu();
		userOption = getUserOption();
		execSelectedFuntion(&list, userOption);

		printf("\n"); 
	}while(userOption != 0);

	

    return 0;
}


void menu(){
	printf("-----OPCOES-----\n");
	printf("1 - inserir na lista\n");
	printf("2 - remover valores repetidos\n");
	printf("3 - imprimir lista\n");
	printf("0 - sair\n");
}

int getUserOption(){
	int option;
	scanf("%d", &option);
	return option;
}

void execSelectedFuntion(LinkedList **list, int function){
	switch (function)
	{
	case 1:
		addUserInputToList(list);
		break;
	
	case 2:
		removeDuplicateNodes(list);
		break;
	
	case 3:
		showList(*list);
		break;

	default:
		break;
	}
}


void addUserInputToList(LinkedList **list){
	int value = getUserInputNodeValue();
	append(list, value);
}

int getUserInputNodeValue(){
	int value;
	printf("Valor para o no: ");
	scanf("%d", &value);
	return value;
}

void initializeList(LinkedList **list){
    *list = NULL;
}

void append(LinkedList **list, int value){
  Node *newNode = getNewNode(value);

  if(isAnEmptyList(*list)){
    insertFirstValueIntoList(list, newNode);
    return;
  }

  Node* lastNode = getLastNode(list);
  setNextNode(lastNode, newNode);
}

Node* getNewNode(int value){
  Node* newNode = (Node*)calloc(1, sizeof(Node));
  newNode->value = value;
  newNode->next = NULL;
  return newNode;
}

bool isAnEmptyList(LinkedList *list){
  return list == NULL;
}

void insertFirstValueIntoList(LinkedList **list, Node *newNode){
    *list = newNode;
}

Node* getLastNode(LinkedList **list){
    Node* actualNode = *list;
    while(actualNode->next != NULL)
        actualNode = actualNode->next;
    return actualNode;
}

void setNextNode(Node *node, Node *newNode){
    node->next = newNode;
}

void showList(LinkedList *list){
  Node* actualNode = list;
 
  while(actualNode != NULL){
    printf("%d ", actualNode->value);
    actualNode = actualNode->next;
  }
}

void removeDuplicateNodes(LinkedList **list){

	Node *actualNode = *list;

	if(isAnEmptyList(actualNode) || hasJustANode(actualNode))
		return;
	
	while(actualNode != NULL){
		removeValuesEqualTo(actualNode, actualNode->value);
		actualNode = actualNode->next;
	}
}

bool hasJustANode(LinkedList *list){
    return list->next == NULL;
}

void removeValuesEqualTo(Node *startPoint, int value){
	Node *actualNode = startPoint;

	while(actualNode != NULL && actualNode->next != NULL){
		if(actualNode->next->value == value){
			Node *newNextNode = actualNode->next->next;
			removeNode(&actualNode->next);
			actualNode = newNextNode;
			continue;
		}

		actualNode = actualNode->next;
	}
}

void removeNode(Node **node){
	Node* targetNode = *node;
	*node = targetNode->next;
	free(targetNode);
}