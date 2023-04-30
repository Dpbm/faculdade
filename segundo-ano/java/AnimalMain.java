class Animal{
  private String tipo, cor;

  public Animal(String tipo, String cor){
    this.tipo = tipo;
    this.cor = cor;
  }

  public void exibirTipoCor(){
    System.out.println("Eu sou " + this.tipo + " " + this.cor);
  }
}

class Cachorro extends Animal{
  private String raca, nome;
  public Cachorro(String raca, String nome, String cor){
    super("cachorro", cor);
    this.raca = raca;
    this.cor = cor;
  }

  public void exibirNomeRaca(){
    System.out.println(this.nome + " da raca " + this.raca);
  }
}

public class AnimalMain{
  public static void main(String[] args){
    Cachorro toto = new Cachorro("Vira Lata", "Toto", "caramelo");
    toto.exibirTipoCor();
    toto.exibirNomeRaca();
  }
}
