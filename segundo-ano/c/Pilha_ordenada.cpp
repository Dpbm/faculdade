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

int Converter(PILHA p, int v)
{
	int bin=0,x;
	
	while (v > 0)
	{
		Push(&p, v%2);
		v /= 2;
	}
	while (!Vazia(&p))
	{
		Pop(&p,&x);
		bin = bin*10+x; //converter
	}
	return bin;
}
void Remover(PILHA *p, PILHA *a, int v)
{
	int x;
	
	while (!Vazia(p) && (p->info[p->topo] != v))
	{
		Pop(p,&x);
		Push(a,x);
	}
	
	if (Vazia(p))
		printf("\nValor nao encontrado!\n");
	else
	{
		Pop(p,&x);
		printf("\nValor removido!\n");
	}
	while (!Vazia(a))
	{
		Pop(a,&x);
		Push(p,x);
	}
}

int Push_ordenado(PILHA *p, PILHA *aux, int v)
{
	if (Cheia(p))
		return 0; //pilha cheia

	

	if(p->info[p->topo] > v || Vazia(p)){
		Push(p, v);
		return 1;
	}

	int tmp;
	while(!Vazia(p) && p->info[p->topo] < v){
		Pop(p, &tmp);
		Push(aux, tmp);
	}

	Push(p, v);
	
	while(!Vazia(aux)){
		Pop(aux, &tmp);
		Push(p, tmp);
	}

	return 1;
}

main()
{
	PILHA s, aux;
	int op, val, binario;
	
	Inicializa(&s);
	
	do
	{
		system("cls");
		puts("1 - Inserir na Pilha");
		puts("2 - Remover da Pilha");
		puts("3 - Imprimir a Pilha");
		puts("4 - Converter decimal para binario");
		puts("5 - Remover um valor da Pilha");
		puts("6 - Inserir ordenado");
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
			
			case 4: printf("\nDigite um valor em dicimal: ");
					scanf("%d",&val);
					
				    Inicializa(&s);
					binario = Converter(s,val);
					
					printf("\n%d em binario = %d\n", val, binario);
					
					system("Pause");
					break;
					
			case 5: printf("\nDigite o valor a remover:");
					scanf("%d", &val);
					Inicializa(&aux);
					
					Remover(&s,&aux,val);
					system("Pause");
					break;
			

			case 6: printf("\nDigite o valor:");
			        scanf("%d", &val);
			        if (Push_ordenado(&s,&aux,val))
			            printf("\nInsercao com sucesso!\n");
			        else
			            printf("\nPilha Cheia!\n");
			        system("Pause");
			        break;
		}
		
		
	}while (op!=0);	
}





