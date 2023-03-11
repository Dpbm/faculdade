public class Ex05{
  public static int numbers[] = {5, 7, 9, 11, 6, 4, 8, 16, 3, 1};
  public static int totalPositions = 10;

  public static void main(String[] args){
    int totalOddPositions = getTotalOddPositions();
    int[] oddPositionedNumbers = new int[totalOddPositions];
    oddPositionedNumbers = getNumbersAtOddPositions();
    showOddPositionedNumbers(oddPositionedNumbers);
  }

  puublic static void showOddPositionedNumbers(int[] oddPositionedNumbers){
    int totalOddPositions = getTotalOddPositions();
    for(int i = 0; i < totalPositions; i++)
      System.out.println("%d ", oddPositionedNumbers[i]);
    System.out.println();
  }

  public static int getTotalOddPositions(){
    return (totalPositions - 1) / 2;
  }

  public static int[] getNumbersAtOddPositions(){
    int totalOddPositions = getTotalOddPositions();
    int[] oddPositionedNumbers = new int[totalOddPositions];

    for(int i = 0; i < totalOddPositions; i++)
      oddPositionedNumbers[i] = numbers[i+1];
    return oddPositionedNumbers;
  }

}
