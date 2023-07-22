#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

#define tam 10

void Cria_Fila(int *Inicio, int *Fim){
	*Inicio = 0;
	*Fim = 0;
}


int Proximo(int actual){
	return (actual+1)%tam;
}

bool Fila_cheia(int Inicio, int Fim){
	return Proximo(Fim) == Inicio;
}

bool Ins_Fila(int *Fila, int *Inicio, int *Fim, int val){
	if(Fila_cheia(*Inicio, *Fim))
		return 0; 
	
	*Fim = Proximo(*Fim);
	Fila[*Fim] = val;
	return 1;
}

bool Fila_Vazia(int Inicio, int Fim){
	return Inicio == Fim;
}

bool Rem_Fila(int *Fila, int *Inicio, int *Fim, int *val){
	if(Fila_Vazia(*Inicio, *Fim))
		return 0;

	*Inicio = Proximo(*Inicio);
	*val = Fila[*Inicio];
	return 1;
}

void Imprime_Fila(int *Fila, int Inicio, int Fim){
	int i = Inicio;
	do{
		i = Proximo(i);
		printf("[ %d ]", Fila[i]);
	}while(i != Fim);
	printf("\n");

}

int Tamanho_Fila(int Inicio, int Fim){
	return abs(Fim-Inicio);
}


int Tamanho_Fila_Cont(int Inicio, int Fim){
	int i = Inicio, cont = 0;
	do{
		i = Proximo(i);
		cont ++;
	}while(i!=Fim);
	return i;
}

void Esvaziar_Fila(int *Fila, int *Inicio, int *Fim){
	int i;
	int removed_value;
	
	while(!Fila_Vazia(*Inicio, *Fim)){
		i=Proximo(*Inicio);
		Imprime_Fila(Fila, *Inicio, *Fim);
		Rem_Fila(Fila, Inicio, Fim, &removed_value);
		printf("\nRemovido -> %d\n", removed_value);
	}

}


main(){
	int Fila[tam], Inicio, Fim, val, op;
	
	Cria_Fila(&Inicio, &Fim);

	do{
		system("cls");
		puts("1 - Inserir na fila");
		puts("2 - Remover da fila");
		puts("3 - Imprimir a fila");
		puts("4 - Tamanho da fila");
		puts("5 - Esvaziar a fila");
		puts("0 - sair");

		printf("\nDigite a opcao: ");
		scanf("%d", &op);
		
		switch(op){
			case 1: printf("\nDigite o valor a inserir: ");
				scanf("%d", &val);
				if(Ins_Fila(Fila, &Inicio, &Fim, val))
					printf("\nInsercao com sucesso");
				else
					printf("\nFila cheia");

				system("pause");
				break;
			
			case 2: if(Rem_Fila(Fila, &Inicio, &Fim, &val))
					printf("\nRemovido o valor: %d", val);
				else
					printf("\nFila Vazia");
				system("pause");
				break;

			case 3: if(Inicio == Fim)
					printf("\nFila vazia");
				else{
					printf("\nFila: ");
					Imprime_Fila(Fila, Inicio, Fim);
				}
				system("pause");
				break;
			
			case 4: if(Inicio == Fim)
					printf("\nFila vazia");
				else
					printf("\nTamanho = %d\n", Tamanho_Fila(Inicio, Fim));
				system("pause");
				break;

			case 5: if(Inicio == Fim)
					printf("\nFila Vazia");
				else
					Esvaziar_Fila(Fila, &Inicio, &Fim);
				system("pause");
				break;
		}

	}while(op != 0);

}
