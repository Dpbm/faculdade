package horario;

public class Horario{
	private int hora, minuto, segundo;

	public Horario(int h, int m, int s){
		this.hora = h;
		this.minuto = m;
		this.segundo = s;
	}

	public Horario(int s){
		this.hora = convertSecondsToHours(s);
		this.minuto = convertSecondsToMinutes(s);
		this.segundo = getRemainSeconds(s);
	}

	private int convertSecondsToHours(int seconds){
		return seconds / 3600;
	}

	private int convertSecondsToMinutes(int seconds){
		return (seconds % 3600) / 60;
	}

	private int getRemainSeconds(int seconds){
		return (seconds % 3600) % 60;
	}

	public String getHorario(){
		return this.hora+":"+this.minuto+":"+this.segundo;
	}

	public int horarioEmSegundos(){
		return this.hora * 3600 + this.minuto * 60 + this.segundo;
	}
	
	public String somaHorario(int hora, int minuto, int segundo){
		int totalSeconds = horarioEmSegundos() + 
				   hora * 3600 + minuto * 60 + segundo;

		int horas = convertSecondsToHours(totalSeconds);
		int minutos = convertSecondsToMinutes(totalSeconds);
		int segundos = getRemainSeconds(totalSeconds);

		return horas + "h " + minutos + "min " + segundos + "s"; 
	}

	public String somaHorario(int segundo){
		int totalSeconds = horarioEmSegundos() + segundo;

		int horas = convertSecondsToHours(totalSeconds);
		int minutos = convertSecondsToMinutes(totalSeconds);
		int segundos = getRemainSeconds(totalSeconds);

		return horas + "h " + minutos + "min " + segundos + "s"; 
	}

}

