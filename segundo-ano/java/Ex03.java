public class Ex03{
  public static void main(String[] args){
    checkDivisibleNumbers(1, 1000);
  }

  public static void checkDivisibleNumbers(int min, int max){
    for(int i = min; i < max; i++)
      if(isDivisibleByThreeAndFour(i))
        System.out.print("%d ",  i);
  }

  public static boolean isDivisibleByThreeAndFour(int i){
    return isDivisibleByThree(i) && isDivisibleByFour(i);
  }

  public static boolean isDivisibleByThree(int i ){
    return i % 3 == 0;
  }
  
  public static boolean isDivisibleByFour(int i){
    return i % 4 == 0;
  }
}
