abstract class Animal{
  public abstract void emitirSom();

  public void dormir(){
    System.out.println("O animal esta dormindo....");
  }
}

class Cachorro extends Animal{
  public void emitirSom(){
    System.out.println("AU AU");
  }
}

class Gato extends Animal{
  public void emitirSom(){
    System.out.println("MIAU");
  }
}

public class Som{
  public static void main(String[] args){
    Cachorro cachorro = new Cachorro();
    Gato gato = new Gato();
    cachorro.emitirSom();
    cachorro.dormir();

    gato.emitirSom();
    gato.dormir();
  }
}
