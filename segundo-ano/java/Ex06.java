import java.util.Scanner;

public class Ex06{
  public static int rows = 4;
  public static int cols = 4;

  public static void main(String[] args){
    int[][] matrix = new int[rows][cols];
    matrix = generateMatrix();
    int mainDiagonalSum = getMainDiagonalSum(matrix);

    System.out.println("Soma da diagonal Principal: %d\n", mainDiagonalSum);
  }

  public static int[][] generateMatrix(){
    int[][] matrix = new int[rows][cols];
    Scanner console = new Scanner(System.in);
    
    for(int i = 0; i < rows; i++)
      for(int j = 0; j < cols; j++){
        System.out.printf("Valor da posição [ %d ][ %d ]: ", i, j);
        matrix[i][j] = console.nextInt();
      }

    return matrix;
  }

  public static int getMainDiagonalSum(int[][] matrix){
    int mainDiagonalSum = 0;
    for(int i = 0; i < rows; i++)
      mainDiagonalSum += matrix[i][i];
    return mainDiagonalSum;
  }

}
