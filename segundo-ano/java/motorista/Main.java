import motorista.Motorista;
import veiculo.Veiculo;

public class Main{
  public static void main(String[] args){
    Veiculo veiculo1 = new Veiculo("12HC333", "randam", "TOTOTOT", "rosa choque");
    Veiculo veiculo2 = new Veiculo("12BC333", "rindim", "FIRTID", "preto violao");

    Motorista motorista = new Motorista("ROnadldid", "11111111111", "j");

    motorista.setVeiculo(veiculo1);

    System.out.println(motorista.getVeiculo().getModelo());

    motorista.setVeiculo(veiculo2);


    System.out.println(motorista.getVeiculo().getModelo());

  }
}
