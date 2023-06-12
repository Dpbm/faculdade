interface MinhaData{
  public string[] meses = {"Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"};

  public int getDia();
  public int getMes();
  public int getAno();
  public void setDia(int dia);
  public void setMes(int mes);
  public void setAno(int ano);
  public String mostraData();
}

class Data implements MinhaData{
  private int dia, mes, ano;

  public int getDia(){
    return this.dia;
  }

  public int getMes(){
    return this.mes;
  }

  public int getAno(){
    return this.ano;
  }

  public void setDia(int dia){
    if(dia > 31)
      return;
    this.dia = dia;
  }

  public void setMes(int mes){
    if(mes > 12)
      return;
    this.mes = mes;
  }

  public void setAno(int ano){
    this.ano = ano;
  }

  public String mostraData(){
    return this.dia+" de "+this.meses[this.mes-1]+" de "+this.ano;
  }
}

public class DataMain{
  public static void main(String[] args){
    Data data = new Data();
    data.setDia(14);
    data.setMes(1);
    data.setAno(2023);
    System.out.println(data.mostraData());
  }
}
