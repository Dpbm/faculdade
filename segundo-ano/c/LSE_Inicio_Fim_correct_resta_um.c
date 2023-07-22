#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct dados
{
	int info;
	struct dados *prox;
};

typedef struct dados NO;


void Cria_LSE(NO **Inicio, NO **Fim )
{
	*Inicio = NULL;
	*Fim = NULL;
}

void Ins_Inicio(NO **Inicio, NO **Fim, int val)
{
	NO *p;
	
	p = (NO*)calloc(1,sizeof(NO));
	p->info = val;
	p->prox = *Inicio;
	if (*Inicio==NULL)  // lista vazia
	    *Fim = p;
	    
	*Inicio = p;
}

void Ins_Fim(NO **Inicio, NO **Fim, int val)
{
	NO *p;
	p = (NO*)calloc(1,sizeof(NO));
	p->info = val;
	p->prox = NULL;
	if (*Inicio==NULL)
	    *Inicio = p;
	else
	   (*Fim)->prox = p;
	   
	*Fim = p;	
}

void Imprime(NO *Inicio)
{
	NO *p = Inicio;
	
	printf("\nInicio -->");
	while (p!=NULL)
	{
		printf("%d-->", p->info);
		p = p->prox;
	}
	printf("NULL\n");
}

void Rem_Inicio(NO **Inicio, NO **Fim){
	NO *p = *Inicio;
	
	if(p == *Fim){
		*Inicio = NULL;
		*Fim = NULL;
	}
	else 
		*Inicio = p->prox;

	free(p);
}


void Rem_Fim(NO **Inicio, NO **Fim){
	if(*Inicio == *Fim){
		*Inicio = NULL;
		*Fim = NULL;
		return;
	}

	NO *q = *Inicio;
	while(q->prox != *Fim)
		q = q->prox;

	q->prox = NULL;
	*Fim = q;
}

void Trans_Fim(NO **Inicio, NO **Fim){
	NO* p = *Inicio;
	NO* q = *Fim;

	*Inicio = p->prox;

	p->prox = NULL;
	q->prox = p;

	*Fim = q;
}

void Trans_Inicio(NO **Inicio, NO **Fim){	
	NO* q = *Inicio;
	while(q->prox != *Fim)
		q = q->prox;

	NO* p = *Fim;

	q->prox = NULL;
	*Fim = q;
	
	p->prox = *Inicio;
	*Inicio = p;
}

void update_case_remove_last_node(NO **lastNode, NO *actualNode){
	NO* p = actualNode;
	p->prox = NULL;
	*lastNode = p;
}

void update_case_remove_middle_node(NO* actualNode){
	NO* p = actualNode->prox;	
	actualNode->prox = p->prox;
}

void change_to_first_node(NO *firstNode, NO **actualNode){
	*actualNode = firstNode;
}

void change_to_next_node(NO **actualNode){
	*actualNode = (*actualNode)->prox;
}

bool is_a_target_node(int counter, int value){
	return counter == value-1;
}

bool is_the_last_node(NO *actualNode, NO *lastNode){
	return actualNode == lastNode;
}

bool is_the_penultimate_node(NO *actualNode, NO *lastNode){
	return actualNode->prox == lastNode;
}

bool has_only_a_node(NO *firstNode, NO *lastNode){
	return firstNode == lastNode;
}

void restart_counter(int *counter){
	*counter = 1;
}

void increase_counter(int *counter){
	(*counter)++;
}

void Resta_Um(NO **Inicio, NO **Fim, int val){
	
	NO* actualNode = *Inicio;
	int counter = 1;

	while(!has_only_a_node(*Inicio, *Fim)){
		if(is_a_target_node(counter, val)){
			restart_counter(&counter);

			if(is_the_last_node(actualNode, *Fim)){
				Rem_Inicio(Inicio, Fim);
				change_to_first_node(*Inicio, &actualNode);
				continue;
			}

			else if(is_the_penultimate_node(actualNode, *Fim)){
				update_case_remove_last_node(Fim, actualNode);
				change_to_first_node(*Inicio, &actualNode);
				continue;
			}

			update_case_remove_middle_node(actualNode);
			change_to_next_node(&actualNode);
			continue;
		}

		increase_counter(&counter);

		if(actualNode == *Fim){
			change_to_first_node(*Inicio, &actualNode);
			continue;
		}

		change_to_next_node(&actualNode);
	}
}

main()
{
	NO *Inicio, *Fim;
	int op, val;
	
	
	Cria_LSE(&Inicio, &Fim);
	
	do
	{
		system("cls");
		puts("1 - Inserir no Inicio");
		puts("2 - Inserir no Fim");
		puts("3 - Imprimir a Lista");
		puts("4 - Remover inicio");
		puts("5 - Remover fim");
		puts("6 - trasnferir incio para o fim");
		puts("7 - trasnferir fim para o inicio");
		puts("11 - resta um");
		puts("0 - Sair do programa");
		
		printf("\nDigite a opcao: ");
		scanf("%d", &op);
		
		switch(op)
		{
			case 1: printf("\nDigite o valor: ");
			        scanf("%d", &val);
			        Ins_Inicio(&Inicio,&Fim, val);
			        break;
			        
			case 2: printf("\nDigite o valor: ");
			        scanf("%d", &val);
			        Ins_Fim(&Inicio,&Fim, val);
			        break;
			
			
			case 3: if (Inicio==NULL)
						printf("\nLista Vazia!");
					else
						Imprime(Inicio);
						
					system("Pause");		
					break;

			case 4: if(Inicio == NULL)
						printf("\nLista vazia!");
					else	
						Rem_Inicio(&Inicio, &Fim);
					system("pause");
					break;	

			case 5: if(Inicio == NULL)
						printf("\nLista vazia!");
					else 
						Rem_Fim(&Inicio, &Fim);	
					system("pause");
					break;	

			case 6: if(Inicio == NULL)
						printf("\nLista vazia!");
					else if(Inicio == Fim)
						printf("\nO primeiro ja eh o ultimo!");
					else
						Trans_Fim(&Inicio, &Fim);	
					system("pause");
					break;	

			case 7: if(Inicio == NULL)
						printf("\nLista vazia!");
					else if(Inicio == Fim)
						printf("\nO ultimo ja eh o primeiro!");
					else
						Trans_Inicio(&Inicio, &Fim);	
					system("pause");
					break;	

			case 11: if(Inicio == NULL)
						printf("\nLista vazia!");
					else if(Inicio == Fim)
						printf("\nHá apenas um valor!");
					else{
						printf("\ndigite a quantidade de passos: ");
			        	scanf("%d", &val);
						Resta_Um(&Inicio, &Fim, val);
					}
					system("pause");
					break;
		}
	}while (op!=0);
}
