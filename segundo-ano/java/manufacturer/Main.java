import manufacturer.Manufacturer;
import product.Product;

public class Main{
  public static void main(String[] args){
    Manufacturer manufacturer = new Manufacturer("aaaaa", "bbbb", "cccc");
    Product product = new Product("carro", 30.3f, 10);

    product.setManufacturer(manufacturer);

    product.sell(10);
    product.replanish(20);
    product.sell(4);

    System.out.println(procut.getManufacturer().getPhone());
  }
}
