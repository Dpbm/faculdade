#include <stdio.h>
#include <stdlib.h>

struct dados{
  struct dados *esq;
  int info;
  struct dados *dir;
};
typedef struct dados NO;

void Cria_LDE(NO **Inicio, NO **Fim){
  *Inicio = NULL;
  *Fim = NULL;
}

void Ins_Inicio(NO **Inicio, NO **Fim, int val){
  NO *p;
  p = (NO*)calloc(1, sizeof(NO));
  p->info = val;
  p->esq = NULL;
  p->dir = *Inicio;

  if(*Inicio == NULL)
    *Fim = p;
  else
    (*Inicio)->esq = p;

  *Inicio = p;
}

void Ins_Fim(NO **Inicio, NO **Fim, int val){
  NO *p;
  p = (NO*)calloc(1, sizeof(NO));
  p->info = val;
  p->dir = NULL;
  p->esq = *Fim;

  if(*Inicio == NULL)
    *Inicio = p;
  else
    (*Fim)->dir = p;

  *Fim = p;
}

void Imprime(NO *Inicio){
  NO *p;
  p = Inicio;

  printf("\nNULL");
  while(p != NULL){
    printf("<--%d-->", p->info);
    p = p->dir;
  }
  printf("NULL\n");
}

void Rem_Inicio(NO **Inicio, NO **Fim){
  if(*Inicio == *Fim){
    free(*Inicio);
    Cria_LDE(Inicio, Fim);
    return;
  }

  NO *p = *Inicio;
  *Inicio = p->dir;
  (*Inicio)->esq = NULL;
  free(p);
}

void Rem_Fim(NO **Inicio, NO **Fim){
  if(*Inicio == *Fim){
    free(*Inicio);
    Cria_LDE(Inicio, Fim);
    return;
  }

  NO *p = *Fim;
  *Fim = p->esq;
  (*Fim)->dir = NULL;
  free(p);
}

NO *Ache_Val(NO *Inicio, int val){
  NO *p = Inicio;
  while(p!=NULL && p->info!=val)
    p = p->dir;
  return p;
}

int main(){
  NO *Inicio, *Fim;
  int val, op;
  
  Cria_LDE(&Inicio, &Fim);

  do{
    system("cls");
    puts("1 - Inserir no inicio");
    puts("2 - Inserir no fim");
    puts("3 - Imprimir lista");
    puts("4 - Remover do inicio");
    puts("5 - Remover do fim");
    puts("6 - Encontrar valor");
    puts("0 - Sair");

    printf("\nDigite a opcao: ");
    scanf("%d", &op);

    switch (op) {
      case 1: printf("\nDigite o valor: ");
              scanf("%d", &val);
              Ins_Inicio(&Inicio, &Fim, val);
              break;

      case 2: printf("\nDigite o valor: ");
              scanf("%d", &val);
              Ins_Fim(&Inicio, &Fim, val);
              break;

      case 3: if(Inicio == NULL)
                printf("\nLista Vazia!\n");
              else
                Imprime(Inicio);
              break;
      
      case 4: if(Inicio == NULL)
                printf("\nLista Vazia!\n");
              else
                Rem_Inicio(&Inicio, &Fim);
              break;
      
      case 5: if(Inicio == NULL)
                printf("\nLista Vazia!\n");
              else
                Rem_Fim(&Inicio, &Fim);
              break;


      case 6: if(Inicio == NULL)
                printf("\nLista Vazia!\n");
              else{
                printf("\nDigite o valor: ");
                scanf("%d", &val);
                NO *encontrado = Ache_Val(Inicio, val);
                if(encontrado == NULL)
                  printf("\nValor nao encontrado!\n");
                else
                  printf("\nValor encontrado!!!!\n");
                system("pause");
              }
              break;

      default: break;
    }
  }while(op != 0);

  return 0;
}
