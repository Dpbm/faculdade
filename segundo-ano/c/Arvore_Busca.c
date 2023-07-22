#include <stdio.h>
#include <stdlib.h>

typedef struct no_arvore
{
	struct no_arvore *esq;
	int info;
	struct no_arvore *dir;
} no_arvore;

typedef no_arvore ARVORE;

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
{			case 5: printf("\nDigite o valor do no a ser removido: ");

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


ARVORE *Busca_pai(ARVORE *Raiz, ARVORE *r)
{
        if ((Raiz->esq != NULL && Raiz->esq == r) || 
	    (Raiz->dir != NULL && Raiz->dir == r)
	)
		return Raiz;
	else
		if(Raiz->info > r->info)
			return Busca_pai(Raiz->esq, r);
		else
			return Busca_pai(Raiz->dir, r);
}


void Remove(ARVORE *Raiz, ARVORE *no){
	ARVORE *pai = Busca_Pai(Raiz, no);
	
	if(no->esq == NULL && no->dir == NULL){
		if(pai->dir == no)
			pai->dir = NULL;
		else
			pai->esq = NULL;

		free(no);
		return;
	}
	else if((no->esq == NULL && no->dir != NULL) || (no->esq != NULL && no->dir == NULL)){
		ARVORE *filho = NULL;
		if(no->dir != NULL)
			filho = no->dir;
		else
			filho = no->esq;

		if(pai->dir == no)
			pai->dir = filho;
		else
			pai->esq = filho;

		free(no);
		return;
			
	}
	else{
		ARVORE *menor = NULL;
		while(no->esq != NULL)
			menor = no->esq;
		ARVORE *pai_menor = Busca_pai(no, menor);
		no->info = menor->info;
		
		if(menor->dir != NULL)
			pai_menor->esq = menor->dir;
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
		puts("5 - Remover um no");	
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
				    if(r==Raiz)
					printf("\nRaiz nao possui pai!");
				    else{
					pai = Busca_Pai(Raiz, r);
					printf("\nO pai de %d = %d\n", r->info, pai->info);
				    }
				system("Pause");
			        break;
			
			case 5: printf("\nDigite o valor a remover: ");
				scanf("%d", &val);

			        r = Busca(Raiz,val);
			        
			        if (r==NULL) 
			        	printf("\nValor nao encontrado!");
			        else{
					if(r == Raiz)
						printf("\nRaiz nao deve ser removida!");
					else
						Remove(Raiz, r);
				}
				system("Pause");
			        break;
				
		}
		
	}while (op!=0);
	
}
