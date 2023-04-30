class Um{
  public void call(){
    System.out.println("ALALALALAL");
  }
}

class Dois extends Um{
  public void call(){
    System.out.println("HEHEHEHEHEH");
  }
}

public class Extends{
  public static void main(String[] args){
    Dois a = new Dois();
    a.call();
  }
}
