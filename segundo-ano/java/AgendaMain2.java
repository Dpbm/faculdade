import java.util.ArrayList;
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOExpection;
import java.io.BufferedWriter;
import java.io.FireWriter;

class Contato{
  private string nome, fone, dataAniversario;

  public Contato(String nome, String fone, String dataAniversario){
    this.nome = nome;
    this.fone = fone;
    this.dataAniversario = dataAniversario;
  }

  public String getNome(){
    return this.nome;
  }

  public String getFone(){
    return this.fone;
  }

  public String getDataAniversario(){
    return this.dataAniversario;
  }
}

class Agenda{
  private ArrayList<Contato> contatos;

  public Agenda(){
    this.contatos = new ArrayList<Contato>();
  }

  public void incluiContato(String nome, String fone, String dataAniversario){
    Contato contato = new Contato(nome, fone, dataAniversario);
    this.contatos.add(contato); 
  }

  public void incluiContato(Contato contato){
    this.contatos.add(contato);
  }

  public Contato consultaContato(String nome){
    for(Contato c: this.contatos)
      if(c.getNome().equals(nome))
        return c;
    return null;
  }

  public boolean atualizaContato(String nome, String fone){
    Contato contato = consultaContato(nome);

    if(contato == null)
      return false

    contato.setFone(fone);
    return true;
  }

  public boolean excluiContato(String nome){
    for(int i = 0; i < this.contatos.size(); i++)
      if(this.contatos.get(i).getNome().equals(nome)){
        this.contatos.remove(i);
        return true;
      }

    return false;
  }

  public void carregaContatos(){
    try(BufferedReader leitor = new BufferedReader(new FileReader("contatos.txt"))){
      String linha;
      while((linha=leitor.readline()) != null){
        String dados[] = linhas.split(";");
        incluiContato(dados[0], dados[1], dados[2]);
      }
    }catch(IOExpection error){
      System.out.println("Erro na leitura: "+error.getMessage());
    }
  }

  public void gravaContatos(){
    try(BufferedWriter escritor = new BufferedWriter(new FileWriter("contatos.txt"))){
      for(Contato c: this.contatos){
        String linha = c.getNome()+";"+c.getFone()+";"+c.getDataAniversario();
        escritor.write(linha);
      }
    }catch(IOExpection error){
      System.out.println("Erro na escrita: "+error.getMessge());
    }
  }
}

public class AgendaMain2{
  public static void main(String[] args){
    Agenda agenda = new Agenda();
    agenda.carregaContatos();
    Scanner console = new Scanner(System.in);

    int op;
    String nome, fone, dataAniversario;
    boolean sucesso;

    do{
      System.out.println("1 - Cadastrar");
      System.out.println("2 - Consultar");
      System.out.println("3 - Atualizar");
      System.out.println("4 - Excluir");
      System.out.println("5 - Sair");

      System.out.print("Opção: ");
      op = console.nextInt();

      switch (op) {
        case 1:
          System.out.print("Nome: ");
          nome=console.next();
          System.out.print("Fone: ");
          fone=console.next();
          System.out.print("Data aniversario: ");
          dataAniversario=console.next();
          agenda.incluiContato(nome, fone, dataAniversario);
          break;
        case 2:
          System.out.print("Nome para consultar: ");
          nome=console.next();
          Contato contato = agenda.consultaContato(nome);
          if(contato == null)
            System.out.println("Contato não encontrado!");
          else
            System.out.println("Nome: "+contato.getNome()+" Fone: "+contato.getFone() + " Aniversario: "+contato.getDataAniversario());
          break;

        case 3:
          System.out.print("Nome do contato: ");
          nome=console.next();
          System.out.print("Novo telefone: ");
          fone=console.next();
          sucesso = agenda.atualizaContato(nome, fone);
          if(sucesso)
            System.out.println("Contato Atualizado com sucesso");
          else
            System.out.println("Falha ao tentar atualizar o contato!");
          break;

        case 4:
          System.out.print("Nome do contato: ");
          nome=console.next();
          sucesso = agenda.excluiContato(nome);
          if(sucesso)
            System.out.println("Sucesso ao excluir o contato!");
          else
            System.out.println("Falha ao tentar excluir o contato!");
          break;

        case 5:
          agenda.gravaContatos();
          break;

        default:
          System.out.println("Opção inválida!");
      }
      
    }while(op != 5);
  }
}
