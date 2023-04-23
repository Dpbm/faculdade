package comprador;

public class Comprador{
  private String nome, endereco, telefone;

  public Comprador(String nome, String endereco, String telefone){
    this.nome = nome;
    this.endereco = endereco;
    this.telefone = telefone;
  }

  public String getNome(){
    return this.nome;
  }

  public String getEndereco(){
    return this.endereco;
  }

  public String getTelefone(){
    return this.telefone;
  }
}
