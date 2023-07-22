#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct dados
{
	int info;
	struct dados *prox;
};

typedef struct dados NO;

void Cria_LSE(NO **Inicio)
{
	*Inicio = NULL;
}

void Ins_Inicio(NO **Inicio, int v)
{
	NO *p;
	p = (NO *)calloc(1, sizeof(NO));
	p->info = v;
	p->prox = *Inicio;	
	*Inicio = p;
}

void Ins_Fim(NO **Inicio, int v)
{
	NO *p, *q;
	
	p = (NO *)calloc(1, sizeof(NO));	
	p->info = v;
	p->prox = NULL;
	
	if (*Inicio == NULL)
	    *Inicio = p;
	else
	{
		q =  *Inicio;
		while(q->prox!=NULL)
		    q = q->prox;
		    
		q->prox = p;
		
	}	
}

void Rem_Inicio(NO **Inicio)
{
	NO *p;
	p = *Inicio;
	*Inicio = p->prox;
	free(p);	
	
}

void Rem_Fim(NO **Inicio)
{
	NO *p, *q;
	
	p = *Inicio;
	if (p->prox==NULL)
	   *Inicio = NULL;
	else
	{
		while (p->prox!=NULL)
		{
			q = p;
			p = p->prox;
		}
		q->prox = NULL;
	}
	free(p);
}

NO * Consultar(NO *Inicio, int v)
{
	NO *p;
	
	p = Inicio;
	
	while(p!=NULL && p->info!=v)
	   p =p->prox;
	
	return p;
}

void Rem_Meio(NO *Inicio, NO *r)
{
	NO *p;
	
	p = Inicio;
	while (p->prox!=r)
	   p = p->prox;
	   
	p->prox = r->prox;
	free(r);
	
}


void Imprime(NO *Inicio)
{
	NO *p;
	p = Inicio;
	
	while (p != NULL)
	{
		printf("%d-->", p->info);
		p = p->prox;
	}
	printf("NULL\n");
}

void Ins_Depois(NO *r, int val)
{
	NO *p;
	
	p =(NO*)calloc(1, sizeof(NO));
	
	p->info= val;
	
	p->prox = r->prox;
	
	r->prox = p;
		
}

void Ins_Antes(NO *Inicio, NO *r, int val)
{
	NO *p, *q;
	
	p =(NO*)calloc(1, sizeof(NO));
	
	p->info= val;
	
	q = Inicio;
	while(q->prox!=r)	
	   q = q->prox;
	   
	p->prox = r;
	q->prox = p;
		
}

void Ins_Ord(NO **Inicio, int val)
{
	NO *q;
	
	if (*Inicio==NULL)
	     Ins_Inicio(Inicio, val);
	else
	{
		q = *Inicio;
		if (val < q->info)
		    Ins_Inicio(Inicio, val);
		else
		{
			while (q!=NULL && q->info<val)
			    q = q->prox;
			    
			if (q==NULL)    
			    Ins_Fim(Inicio,val);
			else
			    Ins_Antes(*Inicio, q, val);		   
	    }	
	}	
}

bool hasOnlyANode(NO *list){
    return list->prox == NULL;
}


bool nextValueIsDuplicate(NO* actualNode, int value){
	return actualNode->prox != NULL && actualNode->prox->info == value;
}


void setNextNode(NO *node, NO *newNode){
    node->prox = newNode;
}

void deleteNode(NO *node){
	free(node);
}

void removeNodesBasedOnItsValue(NO *node){
	NO* actualNode = node;
	int value = node->info;

	while(actualNode != NULL){

		if(nextValueIsDuplicate(actualNode, value)){
			NO* oldNext = actualNode->prox;
			setNextNode(actualNode, actualNode->prox->prox);
			deleteNode(oldNext);
			continue;
		}

		actualNode = actualNode->prox;
	}
}

void Rem_Repetidos(NO **list){
	NO *actualNode = *list;

	if(hasOnlyANode(actualNode))
		return;
	
	while(actualNode != NULL){
		removeNodesBasedOnItsValue(actualNode);
		actualNode = actualNode->prox;
	}
}




main()
{
	NO *Inicio, *r;
	
	int op, val;
	
	Cria_LSE(&Inicio); 

	do
	{
		system("cls");
		puts("1 - Inserir no Inicio");
		puts("2 - Imprimir a Lista");
		puts("3 - Inserir no Fim");
		puts("4 - Remover no Inicio");
		puts("5 - Remover no Fim");
		puts("6 - Consultar um Valor");
		puts("7 - Remover um Valor");		
		puts("8 - Inserir depois de um Valor");		
		puts("9 - Inserir antes de um Valor");		
		puts("10  - Inserir de forma ordenada");
		
		//Vai compor nota continuada
		
		puts("11 - Remover ocorrencias repetidas");
		
		puts("0 - Sair do programa");
		
		printf("\nDigite a opcao:");
		scanf("%d", &op);
		
		switch(op)
		{
			case 1: printf("\nDigite o valor:");
			        scanf("%d", &val);
			        Ins_Inicio(&Inicio, val);
			        break;
			        
			case 2: if (Inicio==NULL)
			            puts("Lista Vazia!");
			        else
			        	Imprime(Inicio);
			        	
			        system("Pause");
			        break;
			        
			case 3: printf("\nDigite o valor:");
			        scanf("%d", &val);
			        Ins_Fim(&Inicio, val);
			        break;
			        
			case 4: if (Inicio==NULL)
			            puts("Lista Vazia!");
			        else
			            Rem_Inicio(&Inicio);
			        break;
			        
			case 5: if (Inicio==NULL)
			            puts("Lista Vazia!");
			        else
			            Rem_Fim(&Inicio);
			        break;
			        
			case 6: printf("\nDigite o valor a procurar:");
			        scanf("%d", &val);
			        
			        r = Consultar(Inicio, val);
			        
			        if (r==NULL)
			           printf("\nValor nao existe na lista!\n");
			        else
			           printf("\nValor = %d\n", r->info);
			           
			        system("Pause");
			        break;
			        
			case 7: printf("\nDigite o valor a remover:");
			        scanf("%d", &val);
			        
			        r = Consultar(Inicio, val);
			        
			        if (r==NULL)
			           printf("\nValor nao existe na lista!\n");
			        else
			           if (r==Inicio)
			               Rem_Inicio(&Inicio);
			           else
			               if (r->prox==NULL)    
			                   Rem_Fim(&Inicio);
			               else
						       Rem_Meio(Inicio, r);
						       
					break;
					
			case 8: printf("\nDigite o valor a procurar:");
			        scanf("%d", &val);
			        
			        r = Consultar(Inicio, val);
			        
			        if (r==NULL)
			           printf("\nValor nao existe na lista!\n");
			        else
					{
						printf("\nDigite o valor a inserir:");
						scanf("%d", &val);
						if (r->prox==NULL) // r � o �ltimo
						    Ins_Fim(&Inicio, val);
						else
						    Ins_Depois(r, val);
					 	
					}
					break;
					
			case 9: printf("\nDigite o valor a procurar:");
			        scanf("%d", &val);
			        
			        r = Consultar(Inicio, val);
			        
			        if (r==NULL)
			           printf("\nValor nao existe na lista!\n");
			        else
					{
						printf("\nDigite o valor a inserir:");
						scanf("%d", &val);
						
						if(r == Inicio)
						    Ins_Inicio(&Inicio, val);
						else
						    Ins_Antes(Inicio, r, val);
						    
				    }
			        break;
			        
			case 10: printf("\nDigite o valor a inserir:");
			         scanf("%d", &val);
			         Ins_Ord (&Inicio, val);
			         break;
			         
			         
			case 11: if (Inicio==NULL)
			             printf("\nLista Vazia!");
			         else
					     Rem_Repetidos(&Inicio) ;
					 break;
			             
			         
			        
			        
		}
	}while (op!=0);	
}
