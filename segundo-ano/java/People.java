import java.util.Scanner;

class Pessoa{
  private String nome, sobrenome;

  public Pessoa(){
    Scanner console = new Scanner(System.in);
    System.out.print("Nome: ");
    this.nome = console.nextLine();
    System.out.print("Sobrenome: ");
    this.sobrenome = console.nextLine();
  }

  public Pessoa(String nome, String sobrenome){
    this.nome = nome;
    this.sobrenome = sobrenome;
  }

  public String getNome(){
    return this.nome;
  }

  public String getSobrenome(){
    return this.sobrenome;
  }

  public String getNomeCompleto(){
    return this.nome + " " + this.sobrenome;
  }
}

class Funcionario extends Pessoa{
  private int numeroMatricula;
  private float salario;

  public Funcionario(String nome, String sobrenome, int numeroMatricula, float salario){
    super(nome, sobrenome);
    this.numeroMatricula = numeroMatricula;
    this.salario = salario;
  }

  public Funcionario(int numeroMatricula, float salario){
    this.numeroMatricula = numeroMatricula;
    this.salario = salario;
  }

  public void setSalario(float salario){
    this.salario = salario;
  }

  public float getPrimeiraParcelaSalario(){
    return this.salario * 0.6f;
  }

  public float getSegundaParcelaSalario(){
    return this.salario * 0.4f;
  }

  public int getNumeroMatricula(){
    return this.numeroMatricula;
  }
}

class Professor extends Funcionario{
  private String formacao;

  public Professor(String nome, String sobrenome, int numeroMatricula, float salario, String formacao){
    super(nome, sobrenome, numeroMatricula, salario);
    this.formacao = formacao;
  }

  public Professor(int numeroMatricula, float salario, String formacao){
    super(numeroMatricula, salario);
    this.formacao = formacao;
  }

  public float getPrimeiraParcelaSalario(){
    return this.salario;
  }

  public float getSegundaParcelaSalario(){
    return 0;
  }
}

public class People{
  public static void main(String[] args){
    Funcionario f = new Funcionario("Marcos", "jonathan", 10, 1300.49f);
    Professor p = new Professor("Jilberto", "Clei", 11, 3400.32f, "Psicologia");
    System.out.println(f.getPrimeiraParcelaSalario());
    System.out.println(p.getPrimeiraParcelaSalario());
  }

}
