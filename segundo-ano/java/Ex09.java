import java.util.Scanner;

public class Ex09{
  public static void main(String[] args){
    Scanner console = new Scanner(System.in);
    System.out.println("Digite a frase: ");
    String text = console.nextLine();

    for(int i = text.length() - 1; i >= 0; i--){
      char actualChar = text.charAt(i);
      System.out.print(actualChar);
    }

    System.out.println();
  }
}
