class Pessoa{
	private String nome;
	private int idade;

	public Pessoa(String nome, int idade){
		this.nome = nome;
		this.idade = idade;
	}
	
	public String getNome(){
		return this.nome;
	}

	public int getIdade(){
		return this.idade;
	}
}

abstract class PessoaIMC extends Pessoa{
	private float peso,altura;

	public PessoaIMC(String nome, int idade, float peso, float altura){
		super(nome, idade);
		this.peso = peso;
		this.altura = altura;
	}

	public float getPeso(){
		return this.peso;
	}

	public float getAltura(){
		return this.altura;
	}

	public float calcularIMC(){
		return this.peso / ((float)Math.pow(this.altura, 2));
	}

	public abstract String resultadoIMC();
}

class Homem extends PessoaIMC{
	private String time;

	public Homem(String nome, int idade, float peso, float altura, String time){
		super(nome, idade, peso, altura);
		this.time = time;
	}

	public void setTime(String time){
		this.time = time;
	}

	public String getTime(){
		return this.time;
	}

	public String resultadoIMC(){
		float imc = this.calcularIMC();
		if(imc < 20.7)
			return "Abaixo do peso ideal";
		if(imc < 26.4)
			return "Peso ideal";
		return "Acima do peso ideal";
	}
}

class Mulher extends PessoaIMC{
	private String signo;

	public Mulher(String nome, int idade, float peso, float altura, String signo){
		super(nome, idade, peso, altura);
		this.signo = signo;
	}

	public void setSigno(String signo){
		this.signo = signo;
	}

	public String getSigno(){
		return this.signo;
	}
	

	public String resultadoIMC(){
		float imc = this.calcularIMC();
		if(imc < 19)
			return "Abaixo do peso ideal";
		if(imc < 25.8)
			return "Peso ideal";
		return "Acima do peso ideal";
	}

}

public class PessoaMain{
	public static void main(String[] args){
		Homem homem = new Homem("Robertao", 10, 30.4f, 1.7f, "Boa vista");
		Mulher mulher = new Mulher("Clara", 34, 150.8f, 1.9f, "Honda Civic tunado");

		System.out.println(homem.getNome()+" " +homem.getIdade() + " "+homem.getPeso()+" "+homem.getAltura()+" "+homem.getTime() + " "+homem.resultadoIMC());
		System.out.println(mulher.getNome()+" " +mulher.getIdade() + " "+mulher.getPeso()+" "+mulher.getAltura()+" "+mulher.getSigno()+" "+mulher.resultadoIMC());

		if(homem.getPeso() > mulher.getPeso())
			System.out.println("\n"+homem.getNome() + " "+homem.getPeso());
		else
			System.out.println("\n"+mulher.getNome() + " "+mulher.getPeso());

		
		if(homem.getAltura() > mulher.getAltura())
			System.out.println("\n"+homem.getNome() + " "+homem.getAltura());
		else
			System.out.println("\n"+mulher.getNome() + " "+mulher.getAltura());
	}
}
