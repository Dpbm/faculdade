package retangulo;

public class Retangulo{
  private int base, altura;

  public Retangulo(int base, int altura){
    this.base = base;
    this.altura = altura;
  }

  public int perimetro(){
    return 2*base + 2*altura;
  }

  public int area(){
    return base * altura;
  }
}
