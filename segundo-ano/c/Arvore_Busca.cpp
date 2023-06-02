#include <stdio.h>
#include <stdlib.h>

struct no_arvore
{
	struct no_arvore *esq;
	int info;
	struct no_arvore *dir;
};

typedef struct no_arvore ARVORE;

void Insere(ARVORE **Raiz, int val)
{
	if (*Raiz==NULL)
	{
		(*Raiz) = (ARVORE *)calloc(1, sizeof(ARVORE));
		(*Raiz)->info = val;
		(*Raiz)->esq = NULL;
		(*Raiz)->dir = NULL;	
	}
	else
	    if (val < (*Raiz)->info)
	        Insere(&(*Raiz)->esq, val);
	    else
	        Insere(&(*Raiz)->dir, val);
}

void Pre_Order(ARVORE *Raiz)
{
	if (Raiz != NULL)
	{
		printf("%d ",Raiz->info);
		Pre_Order(Raiz->esq);
		Pre_Order(Raiz->dir);
	}
}

void In_Order(ARVORE *Raiz)
{
	if (Raiz != NULL)
	{
		In_Order(Raiz->esq);
		printf("%d ", Raiz->info);
		In_Order(Raiz->dir);
	}
}

void Pos_Order(ARVORE *Raiz)
{
	if (Raiz!=NULL)
	{
		Pos_Order(Raiz->esq);
		Pos_Order(Raiz->dir);
		printf("%d ", Raiz->info);
	}
}

ARVORE *Busca (ARVORE *Raiz, int val)
{
	if (Raiz==NULL)
	   return NULL;
	else
	   if (Raiz->info==val)
	      return Raiz;
	   else
	      if (Raiz->info > val)
		 	return Busca (Raiz->esq,val);
	      else
		 	return Busca (Raiz->dir,val);
}

ARVORE *Busca_Pai(ARVORE *Raiz, ARVORE *r)
{
	if ((Raiz->esq!=NULL && Raiz->esq==r) ||
	    (Raiz->dir!=NULL && Raiz->dir==r))
	    return Raiz;
	else
	    if (Raiz->info > r->info)
	       return Busca_Pai(Raiz->esq, r);
	    else
	       return Busca_Pai(Raiz->dir, r);	
}

void Remover (ARVORE *Raiz, ARVORE *r)
{
	ARVORE *pai, *menor;
	
	if (r->esq==NULL && r->dir==NULL) //r é folha
	{
		pai = Busca_Pai(Raiz, r);
		if (pai->esq==r)
		   pai->esq=NULL;
		else
		   pai->dir=NULL;
		free(r);
	}
	else
	    if (r->esq==NULL || r->dir==NULL) //1 filho
	    {
	    	pai = Busca_Pai(Raiz, r);
		    if (pai->esq==r)
		      
			    if (r->esq!=NULL)
		           pai->esq = r->esq;
		        else
		           pai->esq = r->dir;
			    
			else	
	    		if (r->esq!=NULL)
		           pai->dir = r->esq;
		        else
		           pai->dir = r->dir;
	    	free(r);
		}
		else
	    {
		ARVORE *menor = r->dir;
		while(menor->esq != NULL)
			menor = menor->esq;

		ARVORE *pai_menor = Busca_Pai(Raiz, menor);
		if(pai_menor == r)
			pai_menor->dir = menor->dir;
		else
			pai_menor->esq = menor->dir;
		
		r->info = menor->info;
		free(menor);
		
	    }
	
}



main()
{
	ARVORE *Raiz, *r, *pai;
	int op, val;
	
	Raiz = NULL; // Arvore Vazia
	
	do
	{
		system("cls");
		puts("1 - Inserir Valor");
		puts("2 - Percursos");
		puts("3 - Buscar um valor");
		puts("4 - Buscar pai de um No");
		
		puts("5 - Remover No da arvore");
		
		puts("0 - Sair do Programa");
		
		printf("\nDigite a opcao: ");
		scanf("%d", &op);
		
		switch(op)
		{
			case 1: printf("\nDigite o valor: ");
			        scanf("%d", &val);
			        Insere(&Raiz, val);
			        break;
			        
			case 2: if (Raiz == NULL)
			           printf("\nArvore vazia!");
			        else
			        {
			        	printf("\nPRE: ");
			        	Pre_Order(Raiz);
			        	printf("\nIN : ");
			        	In_Order(Raiz);
			        	printf("\nPOS: ");
			        	Pos_Order(Raiz);
			        	printf("\n");
			        }
			        system("Pause");
			        break;
			
			case 3: printf("\nDigite o valor a buscar:");
			        scanf("%d", &val);
			        
			        r = Busca(Raiz,val);
			        
			        if (r==NULL) 
			            printf("\nValor nao encontrado!");
			        else
			            printf("\nValor = %d", r->info);
			            
			        printf("\n");
			        system("Pause");
			        break;
			        
			case 4: printf("\nDigite o valor a buscar:");
			        scanf("%d", &val);
			        
			        r = Busca(Raiz,val);
			        
			        if (r==NULL) 
			            printf("\nValor nao encontrado!");
			        else
			         	if (r==Raiz)
			         	   printf("\nRaiz nao possui pai!");
			         	else
			         	{
			         		pai = Busca_Pai(Raiz, r);
			         		printf("\nO pai de %d = %d\n", r->info, pai->info);
			   			}
					system("Pause");
					break;
					
			case 5: printf("\nDigite o valor a remover:");
			        scanf("%d", &val);
			        
			        r = Busca(Raiz,val);
			        
			        if (r==NULL) 
			            printf("\nValor nao encontrado!");
			        else
			         	if (r==Raiz)
			         	    printf("\nRaiz nao deve ser removida!\n");
			         	else
			         	    Remover (Raiz, r);
			         	    
			        system("Pause");
			        break;
			        
		}
		
	}while (op!=0);
	
}


	   
	   
