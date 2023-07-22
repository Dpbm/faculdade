#include <stdio.h>
#include <stdlib.h>

struct dados
{
	struct dados *esq;
	int info;
	struct dados *dir;
};

typedef struct dados NO;

void Cria_LDE(NO **Inicio, NO **Fim)
{
	*Inicio = NULL;
	*Fim = NULL;
}

void Ins_Inicio(NO **Inicio, NO **Fim, int val)
{
	NO *p;
	
	p = (NO *)calloc(1, sizeof(NO));
	p->info = val;
	p->esq = NULL;
	p->dir = *Inicio;
	if (*Inicio == NULL)
	    *Fim = p;
	else
	    (*Inicio)->esq = p;
	    
	*Inicio = p;
}

void Ins_Fim(NO **Inicio, NO **Fim, int val)
{
	NO *p;
	
	p = (NO *)calloc(1, sizeof(NO));
	p->info = val;
	p->dir = NULL;
	p->esq = *Fim;
	if (*Inicio == NULL)
	    *Inicio = p;
	else
	    (*Fim)->dir = p;
	*Fim = p;
	
}

void Imprime(NO *Inicio)
{
	NO *p;
	
	p = Inicio;
	printf("\nNULL");
	while (p!=NULL)
	{
		printf("<--%d-->", p->info);
		p = p->dir;
	}
	printf("NULL\n\n");
}

void Rem_Inicio(NO **Inicio, NO **Fim)
{
	NO *p;
	
	p = *Inicio;
	
	if (*Inicio==*Fim)  // s� existe 1 n� na lista
	{
		*Inicio=NULL;
		*Fim=NULL;
	}
	else
	{
		*Inicio = p->dir;
		(*Inicio)->esq = NULL;
	}
	free(p);
}

void Rem_Fim(NO **Inicio, NO **Fim)
{
	NO *p;
	
	p = *Fim;
	if (*Inicio == *Fim)
	{
		*Inicio = NULL;
		*Fim = NULL;
	}
	else
	{
		*Fim = p->esq;
		(*Fim)->dir = NULL;
	}
	free(p);
}
	
NO * Consulta(NO *Inicio, int val)
{
	NO *p = Inicio;
	
	while (p!=NULL && p->info!= val)
	   p=p->dir;
	   
	return p;
}

void Ins_ordenado(NO **Inicio, NO **Fim, int val){

	if(val <= (*Inicio)->info){
		Ins_Inicio(Inicio, Fim,  val);
		return;
	}

	if(val >= (*Fim)->info){
		Ins_Fim(Inicio, Fim, val);
		return;
	}

	NO* actualNode = *Inicio;
	while(actualNode->info < val)
		actualNode = actualNode->dir;

	NO* newNode = (NO*)calloc(1, sizeof(NO));
	NO* leftNode = actualNode->esq;

	newNode->info = val;
	newNode->dir = actualNode;
	newNode->esq = leftNode;

	leftNode->dir = newNode;
	actualNode->esq = newNode;
}

main()
{
	NO *Inicio, *Fim, *r;
	int val, op;
	
	Cria_LDE(&Inicio, &Fim);
	
	do
	{
		system("cls");
		puts("1 - Inserir no Inicio");
		puts("2 - Inserir no Fim");
		puts("3 - Imprimir a Lista");
		puts("4 - Remover no Inicio");
		puts("5 - Remover no Fim");
		puts("6 - Consultar Valor");
		puts("7 - Inserir ordernado");

		puts("0 - Sair do programa");
		printf("\nDigite a opcao:");
		scanf("%d", &op);
		
		switch(op)
		{
			case 1: printf("\nDigite o valor: ");
			        scanf("%d", &val);
				    Ins_Inicio(&Inicio,&Fim,val);
				    break;
				    
			case 2: printf("\nDigite o valor: ");
			        scanf("%d", &val);
				    Ins_Fim(&Inicio,&Fim,val);
				    break;
				    
			case 3: if (Inicio==NULL)  
			            printf("\nLista Vazia!");
			        else
			        {
			        	printf("\nLista:\n");
			        	Imprime(Inicio);
					}
					system("Pause");
					break;
					
			case 4: if (Inicio==NULL)  
			            printf("\nLista Vazia!");
			        else
			            Rem_Inicio(&Inicio,&Fim);
			            
			        break;
			 		   
			case 5: if (Inicio==NULL)  
			            printf("\nLista Vazia!");
			        else
			            Rem_Fim(&Inicio,&Fim);
			            
			        break;
			        
			case 6: printf("\nDigite o valor a procurar:");
			        scanf("%d", &val);
			         
			        r = Consulta(Inicio, val);
			         
			        if (r==NULL)
			             printf("\nValor nao existe!\n");
			        else
			             printf("\nValor = %d\n", r->info);
			             
			        system("Pause");
			        break;
			        
			case 7: printf("\nDigite o valor: ");
			        scanf("%d", &val); 
					if(Inicio == NULL)
				    	Ins_Inicio(&Inicio,&Fim,val);
					else
						Ins_ordenado(&Inicio,&Fim,val);
				    break;
			         
		}
		
		
				
	}while(op!=0);
	
	
	
	
	
	
}





