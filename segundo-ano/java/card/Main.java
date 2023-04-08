import account.Account;
import account.Card;
import java.util.Scanner;

public class Main{
  public static void main(String[] args){
    Scanner console = new Scanner(System.in);
    Card card = new Card("hello world");
    Account account = new Account("111111", 100000.3f, card);

    String password = console.nextLine();

    if(!account.getCard().verifyPassword(password)){
      System.out.println("Senha invalida!");
      return;
    }

    account.withdraw(10.3f);
    System.out.println(account.getBalance());

  }
}
