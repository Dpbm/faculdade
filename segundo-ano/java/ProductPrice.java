import java.util.Scanner;

public class ProductPrice{
  public static void main(String[] args){
    float cost = getProductPrice();
    float profit = getCostSellerProfit(cost);
    float tax = getCostTax(cost);
    float finalPrice = getFinalPrice(cost, profit, tax);

    System.out.println("The final price is: %f\n", finalPrice);
  }

  public static float getProductPrice(){
    Scanner console = new Scanner(System.in);
    System.out.println("Product cost: ");
    float cost = console.nextFloat();
    return cost;
  }

  public static float getCostSellerProfit(float cost){
    float profitPercentage = 0.12f; //12%
    return cost * profitPercentage;
  }

  public static float getCostTax(float cost){
    float taxPercentage = 0.2695f;
    return cost * taxPercentage;
  }

  public static float getFinalPrice(float cost, float profit, float price){
    return cost + profit + price;
  }
}
