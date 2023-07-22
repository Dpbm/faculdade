#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define EXIT_SUCESS 0

struct Node{
	int value;
	struct Node *left;
	struct Node *right;
};
typedef struct Node Node;
typedef struct Node Tree;

void start_tree(Tree **tree);
void add_to_tree(Tree **tree, int value);
void add_first_node(Tree **tree, int value);
Node* generate_node(int value);
Node* walk(Node *node);
void insert_in_node(Node *insertion_node, Node* new_node);
void show(Tree *tree);

int main(){
	Tree *tree;
	start_tree(&tree);

	add_to_tree(&tree, 1);
	add_to_tree(&tree, 2);
	add_to_tree(&tree, 3);
	add_to_tree(&tree, 4);
	add_to_tree(&tree, 5);
	add_to_tree(&tree, 6);
	add_to_tree(&tree, 7);
	add_to_tree(&tree, 8);
	show(tree);
	return EXIT_SUCESS;
}

void start_tree(Tree **tree){
	*tree = NULL;
}

void add_to_tree(Tree **tree, int value){
	if(*tree == NULL){
		add_first_node(tree, value);
		return;
	}

	Node *insertion_node = walk(*tree);
	Node *node = generate_node(value);
	insert_in_node(insertion_node, node);
}

void add_first_node(Tree **tree, int value){
	Node *node = generate_node(value);
	*tree = node;
}

Node* generate_node(int value){
	Node *node = (Node*)calloc(1, sizeof(Node));
	node->value = value;
	node->left = NULL;
	node->right = NULL;
	return node;
}

Node* walk(Node *node){
	if(node == NULL)
		return NULL;

	if(node->left == NULL || node->right == NULL)
		return node;

	
	Node* left_node = walk(node->left);
	Node* right_node = walk(node->right);


	if(left_node->left != NULL && left_node->right == NULL &&
	   right_node->left == NULL && right_node->right == NULL)
		return right_node;

	if(left_node->left == NULL && left_node->right == NULL && 
	   right_node->left != NULL && right_node->right == NULL)
		return right_node;

	return left_node;

	
}

void insert_in_node(Node *insertion_node, Node* new_node){
	if(insertion_node->left == NULL){
		insertion_node->left = new_node;
		return;
	}

	insertion_node->right = new_node;
}

void show(Tree *tree){
	if(tree == NULL)
		return;
	
	show(tree->left);
	printf(" %d ", tree->value);
	show(tree->right);
}
