interface A{
  int a = 23;
  public void show();
}

interface B extends A{
  public void show25();
}

class C implements B{
  public void show(){
    System.out.println(a);
  }
  public void show25(){
    System.out.println(25);
  }
}

public class X{
  public static void main(String[] args){
    C c = new C();
    c.show();
    c.show25();
  }
}
