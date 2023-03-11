package random;

public class Random{
  public String generateRandomNumbersSequence(int size){
    String finalText = "";
    for(int i = 0; i < size; i++)
      finalText += getRandomNumber();
    return finalText;
  }

  private int getRandomNumber(){
    return (int)(9 * Math.random());
  }
}
