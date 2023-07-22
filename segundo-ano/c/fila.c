#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node{
	struct Node *next;
	int value;
};

typedef struct Node Node;
typedef struct Node Queue;

void init_queue(Queue **queue, Node **lastNode);
bool is_empty(Queue *queue);
void insert_first_node(Queue **queue, Node **lastNode, Node *newNode);
Node *generate_node(int value);
void push(Queue **queue, Node **lastNode, int value);
bool has_just_one_node(Node *firstNode, Node *lastNode);
void remove_first(Queue **queue, Node **lastNode);
void show(Queue *queue);

int main(){
	Queue *queue;
	Node *lastNode;
	init_queue(&queue, &lastNode);

	push(&queue, &lastNode, 10);
	push(&queue, &lastNode, 20);
	remove_first(&queue, &lastNode);
	remove_first(&queue, &lastNode);
	push(&queue, &lastNode, 30);
	show(queue);
	return 0;
}

void init_queue(Queue **queue, Node **lastNode){
	*queue = NULL;
	*lastNode = NULL;
}

void push(Queue **queue, Node **lastNode, int value){
	Node *newNode = generate_node(value);

	if(is_empty(*queue)){
		insert_first_node(queue, lastNode, newNode);
		return;
	}

	Node *oldLastNode = *lastNode;
	oldLastNode->next = newNode;
	*lastNode = newNode;

}

bool is_empty(Queue *queue){
	return queue == NULL;
}

void insert_first_node(Queue **queue, Node **lastNode, Node *newNode){
	*queue = newNode;
	*lastNode = newNode;
}

Node *generate_node(int value){
	Node *newNode = calloc(1, sizeof(Node));
	newNode->next = NULL;
	newNode->value = value;
	return newNode;
}

void remove_first(Queue **queue, Node **lastNode){
	if(has_just_one_node(*queue, *lastNode)){
		Node *node = *queue;
		free(node);
		init_queue(queue, lastNode);
		return;
	}

	Node *oldFirst = *queue;
	*queue = oldFirst->next;
	free(oldFirst);
}

bool has_just_one_node(Node *firstNode, Node *lastNode){
	return firstNode == lastNode;
}

void show(Queue *queue){
	Node *actualNode = queue;
	while(actualNode != NULL){
		printf("%d ", actualNode->value);
		actualNode = actualNode->next;
	}
}
