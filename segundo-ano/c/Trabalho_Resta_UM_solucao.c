#include <stdio.h>
#include <stdlib.h>

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

void Rem_Inicio(NO **Inicio, NO **Fim)
{
	NO *p = *Inicio;
	
	if (p==*Fim) //so existe um n�
	{
		*Inicio=NULL;
		*Fim=NULL;
	}
	else
		*Inicio = p->prox;
		
	free(p);
}

void Rem_Fim(NO **Inicio, NO **Fim)
{
	NO *p = *Fim, *q;
	
	if (p==*Inicio) // so tem um n�
	{
		*Inicio=NULL;
		*Fim=NULL;
	}
	else
	{
		q = *Inicio;
		while (q->prox!=p)
		    q = q->prox;
		    
		q->prox = NULL;
		*Fim = q;
	}
	free(p);
}

void Trans_Fim(NO **Inicio, NO **Fim)
{
	NO *p;
	
	p=*Inicio;
	*Inicio = p->prox;
	p->prox=NULL;
	
	(*Fim)->prox = p;
	
	*Fim=p;
}

void Trans_Inicio(NO **Inicio, NO **Fim)
{
	NO *p, * q;
	
	p=*Fim;
	q = *Inicio;
	while (q->prox!=p)
	    q = q->prox;
	    
	p->prox=*Inicio;
	*Inicio = p;
	q->prox=NULL;
	*Fim = q;		
}

void remove_selected_node(NO **Inicio, NO *selected){
	NO *actual = *Inicio;
	while(actual->prox != selected)
		actual = actual->prox;
	
	actual->prox = selected->prox;
}

void remove_node(NO **Inicio, NO **Fim, NO *actual){
	if(*Inicio ==  actual){
		Rem_Inicio(Inicio, Fim);
		return;
	}

	if(*Fim == actual){
		Rem_Fim(Inicio, Fim);
		return;
	}
		
	remove_selected_node(Inicio, actual);
	free(actual);
}

void increment_counter(int *counter){
	(*counter)++;
}

void restart_counter(int *counter){
	*counter = 1;
}

void update_actual_node(NO **actualNode){
	*actualNode = (*actualNode)->prox;
}

void Resta_Um(NO **Inicio, NO **Fim, int val){
	if(val <= 0)
		return;

	NO* actualNode = *Inicio;
	int counter = 1;
	
	Imprime(*Inicio);

	while(*Inicio != *Fim){
		

		if(counter == val){
			NO *tmp = actualNode;
			update_actual_node(&actualNode);
			remove_node(Inicio, Fim, tmp);
			Imprime(*Inicio);
			restart_counter(&counter);
		}
		else{
			increment_counter(&counter);
			update_actual_node(&actualNode);
		}
		
		if(actualNode == NULL)
			actualNode = *Inicio;
		
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
		puts("4 - Remover no Inicio");
		puts("5 - Remover no Fim");
		puts("6 - Transferir Inicio para o Fim");
		puts("7 - Transferir Fim para o Inicio");
		
		puts("8 - Resta UM");
		
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
					
			case 4: if (Inicio==NULL)				
						printf("\nLista Vazia!");
					else
						Rem_Inicio(&Inicio, &Fim);
						
					system("Pause");
					break;
					
			case 5: if (Inicio==NULL)				
						printf("\nLista Vazia!");
					else
						Rem_Fim(&Inicio, &Fim);
						
					system("Pause");
					break;
					
			case 6: if (Inicio==NULL)
						printf("\nLista Vazia!");
					else
					    if(Inicio==Fim)//so 1 no
					       printf("\nO primeiro ja eh o ultimo");
					    else
					       Trans_Fim(&Inicio, &Fim);
					system("Pause");
					break;
					
						
			case 7: if (Inicio==NULL)
						printf("\nLista Vazia!");
					else
					    if(Inicio==Fim)//so 1 no
					       printf("\nO ultimo ja eh o primeiro");
					    else
					       Trans_Inicio(&Inicio, &Fim);
					system("Pause");
					break;
					
			case 8: if (Inicio==NULL)
						printf("\nLista Vazia!");
					else
					    if(Inicio==Fim)//so 1 no
					       printf("\nA lista ja esta com um no!");
					       
					    else
				    	{
				    		printf("\nDigite o valor da contagem:");
				    		scanf("%d", &val);
				    		Resta_Um(&Inicio, &Fim, val);
					    }
					system("pause");
					break;
					
					
		}
	}while (op!=0);
}
