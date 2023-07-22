#include <stdio.h>
#include <stdlib.h>

#define tam 10

typedef struct 
{
	int topo;
	int info[tam];
}PILHA;

void Inicializa(PILHA *p)
{
	p->topo=-1;
}

int Cheia(PILHA *p)
{
    return (p->topo==tam-1);
}

int Vazia(PILHA *p)
{
	return (p->topo==-1);
}

int Push(PILHA *p, int v)
{
	if (Cheia(p))
		return 0; //pilha cheia
	p->info[++p->topo] = v;
	return 1;
}

int Pop(PILHA *p, int *v)
{
	if(Vazia(p))
	    return 0; //pilha vazia
	
	*v = p->info[p->topo--];
	return 1;
}

void Imprime(PILHA p)
{
	int i;
	
	for (i=p.topo; i>=0; i--)
	    printf("[ %d ]\n", p.info[i]);
}

int Converter(PILHA p, int val){
	int bin = 0, x;
	
	while(val > 0){
		Push(&p, val%2);
		val /= 2;
	}

	while(!Vazia(&p)){
		Pop(&p, &x);
		bin = bin*10 + x;
	}

	return bin;
}

void Remove(PILHA *s, PILHA *aux, int val){
	int tmp;

	while(!Vazia(s)){
		Pop(s, &tmp);
		
		if(tmp == val)
			break;

		Push(aux, tmp);
		
	}
	
	while (!Vazia(aux)){
		Pop(aux, &tmp);
		Push(s, tmp);
	}
}


main()
{
	PILHA s, aux;
	int op, val, binario;

	Inicializa(&s);
	Inicializa(&aux);

	do
	{
		system("cls");
		puts("1 - Inserir na Pilha");
		puts("2 - Remover da Pilha");
		puts("3 - Imprimir a Pilha");
		puts("4 - Converter para binario");
		puts("5 - Remover um valor da pilha");
		puts("0 - Sair do programa");
		
		printf("\nDigite a opcao: ");
		scanf("%d", &op);
		
		switch(op)
		{
			case 1: printf("\nDigite o valor:");
			        scanf("%d", &val);
			        if (Push(&s,val))
			            printf("\nInsercao com sucesso!\n");
			        else
			            printf("\nPilha Cheia!\n");
			        system("Pause");
			        break;
			        
			case 2: if (Pop(&s, &val))
			            printf("\nValor removido: %d\n", val);
			        else
			            printf("\nPilha Vazia!\n");
			        system("Pause");
			        break;
			        
			case 3: if (Vazia(&s))
			            printf("\nPilha Vazia!\n");
			        else
			        {
			        	printf("Pilha:\n");
			        	Imprime(s);
					}
					system("Pause");
					break;

			case 4: printf("\nDigite um valor em decimal: ");
					scanf("%d", &val);
					Inicializa(&s);

					binario = Converter(s, val);
					printf("\n%d em binario = %d\n", val, binario);
					system("Pause");
					break;
			case 5: printf("\nDigite uma valor para remover: ");
				scanf("%d", &val);
				Remove(&s, &aux, val);
				break;
		
		}
		
		
	}while (op!=0);	
}





