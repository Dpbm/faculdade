import java.util.ArrayList;

class Contato{
  private String nome, fone, dataAniversario;

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

  public void setFone(String fone){
    this.fone = fone;
  }
}

class Agenda{
  private ArrayList<Contato> contatos;

  public Agenda(){
    this.contatos = new ArrayList<Contato>();
  }

  public void cadastrar(String nome, String fone, String dataAniversario){
    Contato contato = new Contato(nome, fone, dataAniversario);
    this.contatos.add(contato);
  }

  public void cadastrar(Contato contato){
    this.contatos.add(contato);
  }

  public Contato consultar(String nome){
    for(Contato c: this.contatos)
      if(c.getNome().equals(nome))
        return c;
    return null;
  }
}

public class AgendaMain{
  public static void main(String[] args){
    Agenda agenda = new Agenda();
    Contato contato1 = new Contato("Jonathan", "11111", "12/23/1");
    Contato contato2 = new Contato("Jonathan2", "11111", "12/23/1");

    agenda.cadastrar(contato1);
    agenda.cadastrar(contato2);

    System.out.println(agenda.consultar("Jonathan").getFone());
  }

}
