package account;

import account.Card;

public class Account{
  private Card card;
  private String accountNumber;
  private float balance;

  public Account(String accountNumber, float balance, Card card){
    this.accountNumber = accountNumber;
    this.balance = balance;
    this.card = card;
  }

  public String getAccountNumber(){
    return this.accountNumber;
  }

  public float getBalance(){
    return this.balance;
  }

  public void deposit(float value){
    this.balance += value;
  }

  public void withdraw(float value){
    if(!this.canDoWithdraw(value))
      return;

    this.balance -= value;
  }

  public boolean canDoWithdraw(float value){
    return this.balance >= value;
  }

  public Card getCard(){
    return this.card;
  }
}
