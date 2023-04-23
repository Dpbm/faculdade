package motorista;

import veiculo.Veiculo;

public class Motorista{
  private String nome, cnh, categoria;
  private Veiculo carro;

  public Motorista(String nome, String cnh, String categoria){
    this.nome = nome;
    this.cnh = cnh;
    this.categoria = categoria;
  }

  public String getNome(){
    return this.nome;
  }

  public String getCNH(){
    return this.cnh;
  }

  public String getCategoria(){
    return this.categoria;
  }

  public void setVeiculo(Veiculo carro){
    this.carro = carro;
  }

  public Veiculo getVeiculo(){
    return this.veiculo;
  }

}
