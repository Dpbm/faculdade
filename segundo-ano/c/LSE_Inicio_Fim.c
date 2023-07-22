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



void Resta_Um(NO **Inicio, NO **Fim, int val){
	
	NO* actualNode = *Inicio;
	int counter = 1;

	while(*Inicio != *Fim){
		if(counter == val-1){
			counter = 1;

			if(actualNode == *Fim){
				NO* p = *Inicio;
				*Inicio = p->prox;
				
				actualNode = *Inicio;
				continue;
			}

			else if(actualNode->prox == *Fim){
				NO* p = actualNode;
				p->prox = NULL;
				*Fim = p;

				actualNode = *Inicio;
				continue;
			}

			NO* p = actualNode->prox;
			actualNode->prox = p->prox;
			actualNode = actualNode->prox;
			continue;
		}

		counter++;

		if(actualNode == *Fim){
			actualNode = *Inicio;
			continue;
		}

		actualNode = actualNode->prox;
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
