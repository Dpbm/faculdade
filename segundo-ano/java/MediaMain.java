class Media{
  public int Media(int a, int b){
    return (a+b)/2;
  }

  public double Media(double a, double b){
    return (a+b)/2;
  }
}

public class MediaMain{
  public static void main(String[] args){
    Media m = new Media();
    System.out.println(m.Media(1, 2));
  }
}
