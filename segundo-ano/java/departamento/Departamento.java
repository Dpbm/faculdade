package departamento;

public class Departamento{
  private int codigo;
  private String nome, sigla;

  public Departamento(int codigo, String nome, String sigla){
    this.codigo = codigo;
    this.nome = nome;
    this.sigla = sigla;
  }

  public int getCodigo(){
    return this.codigo;
  }

  public String getNome(){
    return this.nome;
  }

  public String getSigla(){
    return this.sigla;
  }
}
