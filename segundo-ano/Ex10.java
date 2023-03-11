impot java.util.Scanner;

public class Ex10{
  public static void main(String[] args){
    Scanner console = new Scanner(System.in);
    System.out.print("Digite uma frase: ");
    String text = console.nextLine();
    String newText = "";
    for(int i = 0; i < text.length(); i++){
      char actualChar = text.charAt(i);
      newText = actualChar + newText;
    }
    System.out.println(newText);
  }
}
