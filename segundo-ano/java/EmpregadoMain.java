import java.util.Scanner;

class Empregado{
  private int nro;
  private String nome;

  public Empregado(){
    Scanner console = new Scanner(System.in);

    System.out.print("Digite o nome: ");
    this.nome = console.nextLine();
    System.out.print("Digite o numero: ");
    this.nro = console.nextInt();
  }

  public String getNome(){
    return this.nome;
  }

  public int getNro(){
    return this.nro;
  }
}

class Vendedor extends Empregado{
  private float salarioBase, totalVendas, porcentagemComissao;

  public Vendedor(float salarioBase, float totalVendas, float porcentagemComissao){
    this.salarioBase = salarioBase;
    this.totalVendas = totalVendas;
    this.porcentagemComissao = porcentagemComissao;
  }

  public float getSalario(){
    return this.salarioBase + (this.porcentagemComissao * this.totalVendas);
  }

}

class Gerente extends Empregado{
  private float salarioMensal;

  public Gerente(float salarioMensal){
    this.salarioMensal = salarioMensal;
  }

  public float getSalario(){
    return this.salarioMensal;
  }
}

class Horista extends Empregado{
  private float valorHora;
  private int horasTrabalhadas;

  public Horista(float valorHora, int horasTrabalhadas){
    this.valorHora = valorHora;
    this.horasTrabalhadas = horasTrabalhadas;
  }

  public float getSalario(){
    return this.valorHora * this.horasTrabalhadas;
  }
}

public class EmpregadoMain{
  public static void main(String[] args){
    Vendedor e1 = new Vendedor(1500, 20000, 10);
    Gerente e2 = new Gerente(4000);
    Horista e3 = new Horista(50, 100);

    float s1 = e1.getSalario();
    float s2 = e2.getSalario();
    float s3 = e3.getSalario();

    if(s1 > s2 && s2 > s3)
      System.out.println(e1.getNome());
    else if(s2 > s3)
      System.out.println(e2.getNome());
    else
      System.out.println(e3.getNome());
  }
}
