#include <stdio.h>
#include <stdlib.h>

struct no_arvore{
	struct no_arvore *esq;
	struct no_arvore *dir;
	int info;
};

typedef struct no_arvore ARVORE;

void Insere(ARVORE **Raiz, int val){
	if(*Raiz == NULL){
		*Raiz = (ARVORE*)calloc(1, sizeof(ARVORE));
		(*Raiz)->esq = NULL;
		(*Raiz)->dir = NULL;
		(*Raiz)->info = val;
	}else{
		if(val < (*Raiz)->info)
			Insere(&(*Raiz)->esq, val);
		else
			Insere(&(*Raiz)->dir, val);
		

	}
}

void In_Order(ARVORE *Raiz){
	if(Raiz == NULL)
		return;
	else
		In_Order(Raiz->esq);
		printf("%d ",Raiz->info);
		In_Order(Raiz->dir);
}


ARVORE *Busca(ARVORE *Raiz, int val){
	if(Raiz == NULL)
		return NULL;
	else if(Raiz->info == val)
		return Raiz;
	else if(val < Raiz->info)
		Busca(Raiz->esq, val);
	else
		Busca(Raiz->dir, val);
}

ARVORE *Pai(ARVORE *Raiz, int v){
	if(Raiz != NULL){
		
		Pai(Raiz->esq, v);
		if((Raiz->esq != NULL && Raiz->esq->info == v) || (Raiz->dir != NULL && Raiz->dir->info == v))
			return Raiz;
		Pai(Raiz->dir, v);

	}
}

void Remove(ARVORE **Raiz, int val){
	if((*Raiz) == NULL)
		return;
	else{
		ARVORE *found = Busca(*Raiz, val);
		
		if(found == NULL)
			return;
		
		ARVORE *pai = Pai(*Raiz, val);
		
		if(found->esq == NULL && found->dir == NULL){
			if(pai->esq != NULL && pai->esq->info == val)
				pai->esq = NULL;
			else
				pai->dir = NULL;
			free(found);
			return;
			
		}
		else if((found->dir != NULL && found->esq == NULL) || (found->dir == NULL && found->esq != NULL)){
			
			ARVORE *filho;
			if(found->dir != NULL)
				filho = found->dir;
			else
				filho = found->esq;
			
			
			if(pai->esq != NULL && pai->esq->info == val)
				pai->esq = filho;
			else
				pai->dir = filho;

			free(found);
			return;

		}
		else{
			if((found->dir != NULL && found->esq == NULL) || (found->dir == NULL && found->esq != NULL)){

			Remove(Raiz, val);

		}
	}
}


int main(){
	ARVORE *Raiz = NULL;

	Insere(&Raiz, 50);
	Insere(&Raiz, 40);
	Insere(&Raiz, 80);
	Insere(&Raiz, 30);
	Insere(&Raiz, 20);
	Insere(&Raiz, 60);
	Insere(&Raiz, 90);
	Insere(&Raiz, 10);
	Insere(&Raiz, 30);
	Insere(&Raiz, 55);
	Insere(&Raiz, 70);	
	In_Order(Raiz);
	
	ARVORE *found;

	found = Busca(Raiz, 90);
	printf("\nfound: %d\n", found->info);
	
	found = Busca(Raiz, 55);
	printf("found: %d\n", found->info);

	found = Busca(Raiz, 30);
	printf("found: %d\n", found->info);
	return 0;
}
