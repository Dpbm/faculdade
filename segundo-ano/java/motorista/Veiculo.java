package veiculo;

public class Veiculo{
  private String placa, marca, modelo, cor;

  public Veiculo(String placa, String marca, String modelo, String cor){
    this.placa = placa;
    this.marca = marca;
    this.modelo = modelo;
    this.cor = cor;
  }

  public String getPlaca(){
    return this.placa;
  }

  public String getMarca(){
    return this.marca;
  }

  public String getModelo(){
    return this.modelo;
  }

  public String getCor(){
    return this.cor;
  }
}
