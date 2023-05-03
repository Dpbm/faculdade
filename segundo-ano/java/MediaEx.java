class Media{
  private int soma, contador;

  public void acumula(int valor){
    this.soma += valor;
    this.contador++;
  }

  public float mediaAtual(){
    return this.soma / (float)this.contador;
    //se for dois inteiros ele retorna inteiro (no caso um float truncado)
  }

  protected int getContador(){
    return this.contador;
  }
}

class MaiorMenor extends Media{
  private int maiorValor, menorValor;

  public void acumula(int valor){
    if(valor > this.maiorValor)
      this.maiorValor = valor;
    else if(this.getContador() == 0 || valor < this.menorValor)
      this.menorValor = valor;

    super.acumula(valor);
  }

  public int getMaiorValor(){
    return this.maiorValor;
  }

  public int getMenorValor(){
    return this.menorValor;
  }
}

public class MeidaEx{
  public static void main(String[] args){
    MaiorMenor mm = new MaiorMenor();
    mm.acumula(4);
    mm.acumula(1);
    mm.acumula(0);
    mm.acumula(1);
    mm.acumula(3);

    System.out.println(mm.getMenorValor());
    System.out.println(mm.getMaiorValor());
    System.out.println(mm.mediaAtual());
  }
}
