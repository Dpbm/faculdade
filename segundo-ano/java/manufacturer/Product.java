package product;

import manufacturer.Manufacturer;

public class Product{
  private String description;
  private float price;
  private int quantity;
  private Manufacturer manufacturer;

  public Product(String description, float price, int quantity){
    this.description = description;
    this.price = price;
    this.quantity = quantity;
  }

  public void replanish(int quantity){
    this.quantity += quantity;
  }

  public boolean sell(int quantity){
    boolean canSellProductQuantity = this.canSell(quantity);

    if(canSellProductQuantity)
      this.quantity -= quantity;

    return canSellProductQuantity;
  }

  private boolean canSell(int quantity){
    return this.quantity >= quantity;
  }

  private void setManufacturer(Manufacturer manufacturer){
    this.manufacturer = manufacturer;
  }

  public Manufacturer getManufacturer(){
    return this.manufacturer;
  }
}
