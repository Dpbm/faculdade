package account;

public class Card{
  private String password;

  public Card(String password){
    this.password = password;
  }

  public boolean verifyPassword(String inputPassword){
    return this.password.equals(inputPassword);
  }
}
