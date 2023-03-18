import java.util.Scanner;
import account.Account;

public class Main{
  private static Scanner console = new Scanner(System.in);
  private static Account account = new Account(11111, "dsa", 1.3f);

  public static void main(String[] args){
    int userInput = 0;
    do{
      showMenu();
      userInput = getUserMenuInput();
      doAccountFunction(userInput);
    }while(userInput != 4);
  }

  private static void showMenu(){
    System.out.println("CONTA CORRENTE");

    System.out.println("1 - Deposito");
    System.out.println("2 - Saque");
    System.out.println("3 - Consulta saldo");
    System.out.println("4 - Finalizar");
  }

  private static int getUserMenuInput(){
    int userInput = console.nextInt();
    return userInput;
  }

  private static void doAccountFunction(int function){
    switch (function) {
      case 1:
        deposit();
        break;

      case 2:
        withdraw();
        break;

      case 3:
        showBalance();
        break;

      default:
        break;
    }
  }

  private static void deposit(){
    float value = getDepositValue();
    account.deposit(value);
  }

  private static float getDepositValue(){
    System.out.print("Valor do deposito: ");
    float value = console.nextFloat();
    return value;
  }

  private static void withdraw(){
    float value = getWithdrawValue();
    account.withdraw(value);
  }

  private static float getWithdrawValue(){
    System.out.print("Valor do saque: ");
    float value = console.nextFloat();
    return value;
  }

  private static void showBalance(){
    System.out.println("Seu saldo é de R$" + account.getBalance());
  }
}
