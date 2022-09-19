#include <stdio.h>

const int quantity = 7;

typedef struct {
  char name[30];
  int code;
  float price;
} Product;

float getPrice(Product *products, int productQuantity, int product) {
  float price = 0;

  for (int i = 0; i < quantity; i++) {
    if (products[i].code == product)
      price += products[i].price * productQuantity;
  }

  return price;
}

int main() {
  float total = 0;
  int con = 1;

  printf("quantidade: ");
  scanf("%d", &quantity);

  Product products[quantity];

  for (int i = 0; i < quantity; i++) {
    printf("\nNome do produto: ");
    scanf("%s", &products[i].name);

    printf("Código do produto: ");
    scanf("%d", &products[i].code);

    printf("Preço do produto: ");
    scanf("%f", &products[i].price);
  }

  do {
    int productQuantity = 0;
    int selectedProduct;

    printf("\nProduto: ");
    scanf("%d", &selectedProduct);

    printf("Quantidade de produtos: ");
    scanf("%d", &productQuantity);

    total += getPrice(products, productQuantity, selectedProduct);

    printf("\nContinuar? :");
    scanf("%d", &con);
  } while (con);

  printf("total --> %.2f", total);

  return 0;
}
