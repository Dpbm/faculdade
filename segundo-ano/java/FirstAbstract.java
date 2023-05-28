abstract class Test{
  private int ad;

  public abstract int a();
  public abstract float b();

  public Test(int ad){
    this.ad = ad;
  }

  public int getAd(){
    return this.ad;
  }
}

class C extends Test{
  public C(){
    super(34);
  }

  public int a(){
    return 10;
  }

  public float b(){
    return 3.1415f;
  }
}

public class FirstAbstract{
  public static void main(String[] args){
    C c = new C();
    System.out.println(c.getAd());
    System.out.println(c.a());
    System.out.println(c.b());
  }
}
