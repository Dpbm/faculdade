#include <stdio.h>
#include <stdlib.h>

struct no_arvore{
	struct no_arvore *esq;
	int info;
	struct no_arvore *dir;
};

typedef struct no_arvore ARVORE;


ARVORE *CAPB(int n){
	ARVORE *r;
	if(n==0)
		r = NULL;
	else{
		r = (ARVORE*)calloc(1, sizeof(ARVORE));
		printf("Valor: ");
		scanf("%d", &r->info);
		r->esq = CAPB(n/2);
		r->dir = CAPB(n - (n/2) - 1);

	}
	return r;

}

void Imprime(ARVORE *Raiz){
	if(Raiz != NULL){
		printf("%d", Raiz->info);
		Imprime(Raiz->esq);
		Imprime(Raiz->dir);
	}

}

void Folhas(ARVORE *Raiz){
	if(Raiz == NULL)
		return;
	
	if(Raiz->esq == NULL && Raiz->dir == NULL)
		printf("-%d-", Raiz->info);
	
	Folhas(Raiz->esq);
	Folhas(Raiz->dir);
}


void Descendentes_Diretos(ARVORE *Raiz, int v){
	if(Raiz == NULL)
		return;

	if(Raiz->info == v){
		if(Raiz->esq != NULL)
			printf("%d ", Raiz->esq->info);
		if(Raiz->dir != NULL)
			printf("%d", Raiz->dir->info);
		printf("\n");
	}
	Descendentes_Diretos(Raiz->esq, v);
	Descendentes_Diretos(Raiz->dir, v);
}


void Descendentes(ARVORE *Raiz, int v){

	if(Raiz == NULL)
		return;
	if(Raiz->info == v){
		Imprime(Raiz);
		return;
	}
	Descendentes(Raiz->esq, v);
	Descendentes(Raiz->dir, v);

}

int main(){
	ARVORE *Raiz = NULL;
	Raiz = CAPB(7);
	//Folhas(Raiz);
	Imprime(Raiz);
	printf("\n");
	Descendentes(Raiz, 2);
	return 0;
}
