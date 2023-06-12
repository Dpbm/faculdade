abstract class Empregado{
  private int nro;
  private String nome;

  public Empregado(int nro, String nome){
    this.nro = nro;
    this.nome = nome;
  }

  public int getNro(){
    return this.nro;
  }

  public String getNome(){
    return this.nome;
  }

  public abstract float getSalario();
}


class Vendedor extends Empregado{
  private float salarioBase, totalVendasMes, comissao;

  public Vendedor(int nro, String nome){
    super(nro, nome);
  }

  public void setSalarioBase(float salarioBase){
    this.salarioBase = salarioBase;
  }

  public void setTotalVendasMes(float totalVendasMes){
    this.totalVendasMes = totalVendasMes;
  }

  public void setComissao(flaot comissao){
    this.comissao = comissao;
  }

  public float getSalario(){
    return this.salarioBase + (this.totalVendasMes * (this.comissao / 100));
  }
}

class Gerente extends Empregado{
  private float salario;

  public Gerente(int nro, String nome){
    super(nro, nome);
  }

  public void setSalario(float salario){
    this.salario = salario;
  }

  public float getSalario(){
    return this.salario;
  }
}

class Horista extends Empregado{
  private int horas;
  private float valorHora;

  public Horista(int nro, String nome){
    super(nro, nome);
  }

  public void setHoras(int horas){
    this.horas = horas;
  }

  public void setValorHora(flaot valorHora){
    this.valorHora = valorHora;
  }

  public float getSalario(){
    return this.valorHora * this.horas;
  }
}

public class EmpregadoMain{
  public static void main(String[] args){
    Vendedor v = new Vendedor(1, "jorge");
    v.setSalarioBase(12000);
    v.setComissao(0.32f);
    v.setTotalVendasMes(10000);
    System.out.println(v.getSalario());

    Gerente g = new Gerente(2, "Roiberiro");
    g.setSalario(1001010);
    System.out.println(g.getSalario());

    Horista h = new Horista(3, "Marid");
    h.setHoras(10000);
    h.setValorHora(10);
    System.out.println(h.getSalario());

  }
}
