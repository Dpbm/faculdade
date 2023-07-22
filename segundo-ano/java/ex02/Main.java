import pessoa.Pessoa;

public class Main{
	public static void main(String[] args){
		Pessoa pessoa = new Pessoa("Roberto");
		
		System.out.println("Nome:     " + pessoa.pegarNome());
		System.out.println("Telefone: " + pessoa.pegarTelefone());
		System.out.println("Idade:    " + pessoa.pegarIdade());

		pessoa.setIdade(34);
		pessoa.setTelefone("15997137268");

		
		System.out.println("\nNome:     " + pessoa.pegarNome());
		System.out.println("Telefone: " + pessoa.pegarTelefone());
		System.out.println("Idade:    " + pessoa.pegarIdade());

	}
}
