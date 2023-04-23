package funcionario;

import departamento.Departamento;

public class Funcionario{
  private int codigo;
  private String nome;
  private float salario;
  private Departamento departamento;

  public Funcionario(int codigo, String nome, float salario){
    this.codigo = codigo;
    this.nome = nome;
    this.salario = salario;
  }

  public int getCodigo(){
    return this.codigo;
  }

  public String getNome(){
    return this.nome;
  }

  public float getSalario(){
    return this.salario;
  }

  public void setDepartamento(Departamento departamento){
    this.departamento = departamento;
  }

  public Departamento getDepartamento(){
    return this.departamento;
  }

  public void setSalario(float salario){
    this.salario = salario;
  }
}
