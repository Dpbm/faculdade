interface Func{
  public int exec(int n);
}


class Reentrant implements Func{
  public int exec(int n){
    int a = 0;
    for(int i = 0; i < n; i++)
      a += i;
    return a;
  }
}

class NonReentrant implements Func{
  private int a = 0; 

  public int exec(int n){
    for(int i = 0; i < n; i++)
      a += i;
    return a;
  }
}


class TestThread extends Thread{
  private String name;
  private Func func;
  private int n;

  public TestThread(String name, Func func, int n){
    this.name = name;
    this.func = func;
    this.n = n;
  }


  public void run(){
    System.out.println("Executing Thread: " + this.name);
    int result = this.func.exec(this.n);

    System.out.println("Result from Thread " + this.name + "= "+result);
  }
}

public class ThreadsTest{
  public static void main(String[] args) {
    //Func reentrant = new Reentrant();
    Func nonReentrant = new NonReentrant();


    //System.out.println("---Reentrant Test---");
    //Thread t1 = new TestThread("T1", reentrant, 5);
    //Thread t2 = new TestThread("T2", reentrant, 6);
    //
    //t1.start();
    //t2.start();
    
    System.out.println("---Non Reentrant Test---");
    Thread t1 = new TestThread("T1", nonReentrant, 5);
    Thread t2 = new TestThread("T2", nonReentrant, 6);

    t1.start();
    t2.start();
  }
}
