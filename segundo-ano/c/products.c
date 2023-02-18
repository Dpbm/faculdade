#include <stdio.h>

#define SIZE 2

typedef struct {
  int code;
  char name[30];
  float price;
} Product;

int main(){
  Product product[SIZE];
  int i;

  for (i = 0; i < SIZE; i++){
    fflush(stdin);
    puts("\n\nProduct name: ");
    gets(product[i].name);

    puts("Product code: ");
    scanf("%d", &product[i].code);

    puts("Product price: ");
    scanf("%f", &product[i].price);
  }

  printf("\n\nProducts: \n");

  for(i = 0; i < SIZE; i++)
    printf("%d %s %.2f\n", product[i].code, product[i].name, product[i].price);

  return 0;
}
