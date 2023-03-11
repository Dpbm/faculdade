import pessoa.Pessoa;

public class Main{
  public static void main(String[] args){
    Pessoa pessoa = new Pessoa("marco", "1111111111", 10);
    for(int i = 0; i < 10; i++)
      pessoa.fazAniversario();
    System.out.println(pessoa.getIdade());
  }
}
