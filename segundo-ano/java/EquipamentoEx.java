class Equipamento{
  private boolean ligado;

  public void ligar(){
    this.ligado = true;
  }

  public void desligar(){
    this.ligado = false;
  }

  public boolean getLigado(){
    return this.ligado;
  }
}

class EquipamentoSonoro extends Equipamento{
  private int volume;
  private boolean stereo;

  public int getVolume(){
    return this.volume;
  }

  public boolean getStereo(){
    return this.stereo;
  }

  public void setVolume(int volume){
    this.volume = volume;
  }

  public void setStereo(){
    this.stereo = true;
  }
  
  public void setMono(){
    this.stereo = false;
  }

  public void ligar(){
    super.ligar();
    this.setVolume(5);
  }
}

public class EquipamentoEx{
  public static void main(String[] args){
    EquipamentoSonoro radio = new EquipamentoSonoro();
    radio.ligar();

    radio.setVolume(8);

    if(radio.getLigado())
      System.out.println("estado: ligado\nvolume: " + radio.getVolume());
    else
      System.out.println("estado: desligado!");
  }
}
