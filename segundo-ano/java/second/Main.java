import product.Product;

public class Main{
  public static void main(String[] args){
    Product product = new Product("Um produto bem legal", 10.3f);
    product.updateQuantity(20);
    product.sell(3);
    product.showData();
  }
}
