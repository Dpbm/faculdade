import java.util.Scanner

public class Input{
  public static void main(String[] args){
    Scanner console = new Scanner(system.in);
    int a = console.nextInt();

    String textWithNoSpaces = console.next();
    System.out.println("Entrada text sem espaços: " + textWithNoSpaces);

    // isso não vai pegar o valor correto já que fizemos uma leitura acima
    String text = console.nextLine();
    System.out.println("Entrada text: " + text);
  }
}
