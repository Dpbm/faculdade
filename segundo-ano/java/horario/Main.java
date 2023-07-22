import horario.Horario;

public class Main{
	public static void main(String[] args){
		Horario horario = new Horario(2, 14, 37);
		System.out.println(horario.getHorario());
		System.out.println(horario.horarioEmSegundos());

		System.out.println(horario.somaHorario(3000));

	}
}
