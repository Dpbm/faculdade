public class Matrix{
  public static void main(String[] args){
    int rows = 10;
    int cols = 10;

    int[][] a = new int[rows][cols];
    
    for(int i = 0; i < rows; i++)
      for(int j = 0; j < cols; j++)
        a[i][j] = i+j;

    for(int i = 0; i < rows; i++){
      for(int j = 0; j < cols; j++)
        System.out.println(a[i][j] + "");
      System.out.println();
    }
      
  }
}
