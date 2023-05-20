import java.util.Scanner;
import java.util.InputMismatchException;

public class ExampleError{
  public static void main(String[] args){
    System.out.print("Number: ");
    Scanner console = new Scanner(System.in);
    try {
      console.nextInt();
    } catch (InputMismatchException error) {
      System.out.println("Invalid!");
    }
  }
}
