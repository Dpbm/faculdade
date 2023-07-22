import java.util.Date;

interface Radio{
	public int FM=0;
	public int AM=1;
	public void setBanda(int banda);
	public int getBanda();
	public void setSintonia(float frequencia);
	public float getSintonia();
	public void setVolumeRadio(int volume);
	public int getVolumeRadio();
	public void ligaRadio();
	public void desligaRadio();
}

interface Relogio{
	public String getHorario();
	public String getAlarme();
	public void setAlarme(int hora, int min);
	public void ligaAlarme();
	public void desligaAlarme();
	public int getStatusAlarme();
	public int getVolumeAlarme();
	public void setVolumeAlarme(int volume);
}

class RadioRelogio implements Radio, Relogio{
	public int banda, volumeRadio, volumeAlarme, horaAlarme, minutoAlarme;
	public float frequencia;
	public boolean alarmeLigado, radioLigado;
	
	public RadioRelogio(int banda, int vr, int va, float frequencia){
		this.banda = banda;
		this.volumeRadio = vr;
		this.volumeAlarme = va;
		this.frequencia = frequencia;
	}

	public int getBanda(){
		return this.banda;
	}

	public void setBanda(int banda){
		if(this.radioLigado)
			this.banda = banda;
	}

	public float getSintonia(){
		return this.frequencia;
	}

	public void setSintonia(float frequencia){
		if(this.radioLigado)
			this.frequencia = frequencia;
	}
	
	public void ligaRadio(){
		this.radioLigado = true;
	}

	public void desligaRadio(){
		this.radioLigado = false;
	}

	public int getVolumeRadio(){
		return this.volumeRadio;
	}

	public void setVolumeRadio(int volume){
		this.volumeRadio = volume;
	}

	public String getHorario(){
		Date hoje = new Date();
		return hoje.getHours()+":"+hoje.getMinutes()+":"+hoje.getSeconds();
	}
	
	public String getAlarme(){
		return this.horaAlarme + ":" + this.minutoAlarme + ":00";
	}

	public void setAlarme(int hora, int minuto){
		this.horaAlarme = hora;
		this.minutoAlarme = minuto;
	}

	public void desligaAlarme(){
		this.alarmeLigado = false;
	}

	public void ligaAlarme(){
		this.alarmeLigado = true;
	}

	public int getVolumeAlarme(){
		return this.volumeAlarme;
	}

	public void setVolumeAlarme(int volume){
		this.volumeAlarme = volume;
	}

	public int getStatusAlarme(){
		return this.alarmeLigado ? 1 : 0;
	}
}

public class RadioRelogioMain{
	public static void main(String[] args){
		RadioRelogio rr = new RadioRelogio(Radio.FM, 50, 50, 88);

		rr.ligaRadio();
		rr.setVolumeRadio(70);
		rr.setSintonia(100);

		rr.setAlarme(20, 40);
		rr.ligaAlarme();
		rr.setVolumeAlarme(30);
		
		System.out.println("Banda: "+rr.getBanda());
		System.out.println("Frequencia: "+rr.getSintonia());
		System.out.println("Volume Radio: "+rr.getVolumeRadio());
		System.out.println("Hora: "+rr.getHorario());
		System.out.println("Status: "+rr.getStatusAlarme());
		System.out.println("Hora Alarme: "+rr.getAlarme());
		System.out.println("Volume Alarme: "+rr.getVolumeAlarme());

	}
}
