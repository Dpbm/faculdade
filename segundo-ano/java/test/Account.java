package account;

import random.Random;

public class Account{
  private String accountNumber;
  private double balance;

  public Account(){
    accountNumber = generateAccountNumber();
    balance = 0;
  }

  private String generateAccountNumber(){
    Random random = new Random();
    String firstFourDigits = random.generateRandomNumbersSequence(4);
    String lastDigit = random.generateRandomNumbersSequence(1);
    return firstFourDigits + "-" + lastDigit;
  }

  public void increaseBalance(double increasedMoney){
    balance += increasedMoney;
  }

  public void showAccountNumber(){
    System.out.println(accountNumber);
  }

  public void showTotalBalance(){
    System.out.println(balance);
  }
}
