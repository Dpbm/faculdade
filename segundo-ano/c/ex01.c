#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node{
    int value;
    struct Node* next;
};
typedef struct Node Node;
typedef struct Node List;

void initialize_list(List **list);
void append(List **list, int value);
bool list_already_has_nodes(List *list);
void append_value(List **list, int value);
Node* get_new_node(int value);
void insert_first_node(List **list, int value);

void run_tests();
void test_initialize_as_null();
void test_list_already_has_nodes_as_false();
void test_list_already_has_nodes_as_true();
void test_get_new_node();
void test_insert_first_node();
void test_append_value();
void test_append_with_an_empty_list();
void test_append_with_a_list_with_elements();

int main(){
    run_tests();
    return 0;
}

void initialize_list(List **list){
    *list = NULL;
}

void append(List **list, int value){
    if(list_already_has_nodes(*list)){
        append_value(list, value);
        return;
    }

    insert_first_node(list, value);
}

bool list_already_has_nodes(List *list){
    return list != NULL;
}

void append_value(List **list, int value){
    Node* new_node = get_new_node(value);
    
    Node* actualNode = *list;
    while(actualNode->next != NULL)
        actualNode = actualNode->next;

    actualNode->next = new_node;
}

Node* get_new_node(int value){
    Node* new_node = malloc(1 * sizeof(Node));
    new_node->value = value;
    new_node->next = NULL;
    return new_node;
}

void insert_first_node(List **list, int value){
    Node* new_node = get_new_node(value);
    *list = new_node;
}






void run_tests(){
    test_initialize_as_null();
    test_list_already_has_nodes_as_false();
    test_list_already_has_nodes_as_true();
    test_get_new_node();
    test_insert_first_node();
    test_append_value();
    test_append_with_an_empty_list();
    test_append_with_a_list_with_elements();
}

void test_initialize_as_null(){
    List* list;
    initialize_list(&list);

    if(list == NULL){
        printf("test_initialize: check\n");
        return;
    }

    printf("test_intialize: failed!\n");
}

void test_list_already_has_nodes_as_false(){
    List* list;
    initialize_list(&list);

    if(!list_already_has_nodes(list)){
        printf("test_list_already_has_nodes_as_false: check\n");
        return;
    }

    printf("test_list_already_has_nodes_as_false: failed!\n");
}

void test_list_already_has_nodes_as_true(){
    List* list;
    initialize_list(&list);
    insert_first_node(&list, 1);

    if(list_already_has_nodes(list)){
        printf("test_list_already_has_nodes_as_true: check\n");
        return;
    }

    printf("test_list_already_has_nodes_as_true: failed!\n");
}

void test_get_new_node(){
    Node* new_node = get_new_node(10);

    if(new_node->value == 10 && new_node->next == NULL){
        printf("test_get_new_node: check\n");
        return;
    }

    printf("test_get_new_node: failed!\n");
}

void test_insert_first_node(){
    List* list;
    initialize_list(&list);
    insert_first_node(&list, 1);

    if(list->value == 1 && list->next == NULL){
        printf("test_insert_first_node: check\n");
        return;
    }
    
    printf("test_insert_first_node: failed!\n");
}

void test_append_value(){
    List* list;
    initialize_list(&list);
    insert_first_node(&list, 1);
    append_value(&list, 4);

    if(list->next != NULL && list->next->value == 4){
        printf("test_append_value: check\n");
        return;
    }
    
    printf("test_append_value: failed!\n");
}

void test_append_with_an_empty_list(){
    List* list;
    initialize_list(&list);
    append(&list, 10);

    if(list->next == NULL && list->value == 10){
        printf("test_append_with_an_empty_list: check\n");
        return;
    }
    
    printf("test_append_with_an_empty_list: failed!\n");
}

void test_append_with_a_list_with_elements(){
    List* list;
    initialize_list(&list);
    insert_first_node(&list, 4);
    append(&list, 10);

    if(
        list->next != NULL && list->next->value == 10
    ){
        printf("test_append_with_a_list_with_elements: check\n");
        return;
    }
    
    printf("test_append_with_a_list_with_elements: failed!\n");
}
