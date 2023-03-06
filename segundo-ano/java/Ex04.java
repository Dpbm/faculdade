public class Ex04{
  public static void main(String[] args){
    checkDivisibleNumbersAndSumThem(1, 1000);
  }

  public static void checkDivisibleNumbersAndSumThem(int min, int max){
    int sum = 0;
    for(int i = min; i < max; i++)
      if(isDivisibleByTwoFiveAndSeven(i)){
        sum += i;
        System.out.println("%d ", i);
      }
  }

  public static boolean isDivisibleByTwoFiveAndSeven(int i){
    return numberIsDivisibleBy(i, 2) && numberIsDivisibleBy(i, 5) && numberIsDivisibleBy(i, 7);
  }

  public static boolean numberIsDivisibleBy(int number, int by){
    return number % by == 0;
  }
}
