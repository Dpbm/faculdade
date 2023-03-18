package account;

public class Account{
  private int accountNumber;
  private String name;
  private float balance;

  public Account(int accountNumber, String name, float balance){
    this.accountNumber = accountNumber;
    this.name = name;
    this.balance = balance;
  }

  public void deposit(float value){
    balance += value;
  }

  public boolean withdraw(float value){
    boolan canDoWithdraw = canWithdraw(value);
    if(canDoWithdraw)
      doWithdraw(value);
    return canDoWithdraw;
  }

  public boolean canWithdraw(float value){
    return value <= balance;
  }

  public void doWithdraw(float value){
    balance -= value;
  }

  public float getBalance(){
    return balance;
  }

  public int getAccountNumber(){
    return accountNumber;
  }
  
  public String getName(){
    return name;
  }
}
