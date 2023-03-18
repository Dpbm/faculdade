package product;

public class Product{
  private String description;
  private float price;
  private int totalSold, totalAvailable;

  public Product(String description, float price){
    this.description = description;
    this.price = price;
  }

  public void updateQuantity(int quantity){
    totalAvailable += quantity;
  }

  public boolean sell(int quantity){
    boolean hasQuantityInStock = hasInStock(quantity);
    if(hasQuantityInStock){
      updateStock(quantity);
      updateTotalSold(quantity);
    }

    return hasQuantityInStock;
  }

  private boolean hasInStock(int quantity){
    return totalAvailable >= quantity;
  }

  private void updateStock(int soldQuantity){
    totalAvailable -= soldQuantity;
  }

  private void updateTotalSold(int soldQuantity){
    totalSold += soldQuantity;
  }

  public void showData(){
    System.out.println("Descrição: " + description);
    System.out.println("Preço: " + price);
    System.out.println("Total vendido: " + totalSold);
    System.out.println("Total em estoque: " + totalAvailable);
  }
}
