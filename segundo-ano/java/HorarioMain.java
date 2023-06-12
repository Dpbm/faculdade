interface MeuHorario{
  public int getHora();
  public int getMinuto();
  public int getSegundo();
  public void setHora(int hora);
  public void setMinuto(int minuto);
  public void setSegundo(int segundo);
  public String toString();
}

class Horario implements MeuHorario{
  private int hora, minuto, segundo;

  public int getHora(){
    return this.hora;
  }

  public int getMinuto(){
    return this.minuto;
  }

  public int getSegundo(){
    return this.segundo;
  }

  public void setHora(int hora){
    this.hora = hora;
  }

  public void setMinuto(int minuto){
    this.minuto = minuto;
  }

  public void setSegundo(int segundo){
    this.segundo = segundo;
  }

  public String toString(){
    return this.hora":"this.minuto+":"+this.segundo;
  }
}

public class HorarioMain{
  public static void main(String[] args){
    Horario horario = new Horario();
    horario.setHora(10);
    horario.setMinuto(3);
    horario.setSegundo(43);
    System.out.println(horario.toString());
  }
}
