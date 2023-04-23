import funcionario.Funcionario;
import departamento.Departamento;

public class Main{
  public static void main(String[] args){
    Departamento departamento1 = new Departamento(1, "Recursos Humanos", "RH");
    Departamento departamento2 = new Departamento(2, "Marketing", "MKT");

    Funcionario funcionario1 = new Funcionario(1, "Jorge Ronaldo", 4000);
    Funcionario funcionario2 = new Funcionario(2, "Marcelo Cleiton da Silva", 4500);

    funcionario1.setDepartamento(departamento2);
    funcionario2.setDepartamento(departamento1);
  
    if(funcionario1.getSalario() > funcionario2.getSalario()){
      System.out.println(funcionario1.getNome() + " - " + funcionario1.getDepartamento().getNome());
      return;
    }

    System.out.println(funcionario2.getNome() + " - " + funcionario2.getDepartamento().getNome());

  }
}
