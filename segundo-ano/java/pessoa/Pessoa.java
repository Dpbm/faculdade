package pessoa;

public class Pessoa{
  private int idade;
  private String nome, fone;

  public Pessoa(String nome, String fone, int idade){
    this.nome = nome;
    this.fone = fone;
    this.idade = idade;
  }

  public void fazAniversario(){
    idade++;
  }

  public void atualizaFone(String fone){
    this.fone = fone;
  }

  public int getIdade(){
    return idade;
  }

  public String getNome(){
    return nome;
  }

  public String getFone(){
    return fone;
  }
}
