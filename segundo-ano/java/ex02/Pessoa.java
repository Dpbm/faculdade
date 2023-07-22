package pessoa;

public class Pessoa{
	private String nome, telefone;
	private int idade;

	public Pessoa(String nome, String telefone, int idade){
		this.nome = nome;
		this.telefone = telefone;
		this.idade = idade;
	}

	public Pessoa(String nome){
		this.nome = nome;
	}

	public String pegarNome(){
		return this.nome;
	}

	public String pegarTelefone(){
		return this.telefone;
	}

	public int pegarIdade(){
		return this.idade;
	}

	public void setTelefone(String telefone){
		this.telefone = telefone;
	}

	public void setIdade(int idade){
		this.idade = idade;
	}
}
