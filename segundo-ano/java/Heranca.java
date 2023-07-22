/*
 * Integrantes: Alexandre Silva e Gabriela Stela
 * RA:		624071		e 628751
 */

class Fornecedor{
	private String nome, endereco, telefone;

	public Fornecedor(String nome, String endereco, String telefone){
		this.nome = nome;
		this.endereco = endereco;
		this.telefone = telefone;
	}

	public String getNome(){
		return this.nome;
	}

	public String getEndereco(){
		return this.endereco;
	}

	public String getTelefone(){
		return this.telefone;
	}
}

class Produto{
	private int codigo, qtdeVendida;
	private String descricao;
	private float preco;
	private Fornecedor fornecedor;

	public Produto(int codigo, String descricao, float preco, Fornecedor fornecedor){
		this.codigo = codigo;
		this.descricao = descricao;
		this.preco = preco;
		this.fornecedor = fornecedor;
		this.qtdeVendida = 0;
	}

	public int getCodigo(){
		return this.codigo;
	}

	public String getDescricao(){
		return this.descricao;
	}

	public Fornecedor getFornecedor(){
		return this.fornecedor;
	}

	public float getFaturamento(){
		return this.preco * this.qtdeVendida;
	}

	protected void updateQtdeVendida(int qtde){
		this.qtdeVendida += qtde;
	}
}

class Peca extends Produto{
	private int qtdeDisp;

	public Peca(int codigo, String descricao, float preco, Fornecedor fornecedor){
		super(codigo, descricao, preco, fornecedor);
		this.qtdeDisp = 0;
	}

	public boolean vender(int qtde){
		if(qtde <= 0 || this.qtdeDisp < qtde)
			return false;

		this.qtdeDisp -= qtde;
		this.updateQtdeVendida(qtde);
		return true;

	}

	public void repor(int qtde){
		this.qtdeDisp += qtde;
	}
}

class Servico extends Produto{
	private int tempoServico;
	
	public Servico(int codigo, String descricao, float preco, Fornecedor fornecedor, int tempoServico){
		super(codigo, descricao, preco, fornecedor);
		this.tempoServico = tempoServico;
	}

	public boolean vender(int qtde){
		this.updateQtdeVendida(qtde);
		return true;
	}
}

public class Heranca{
	public static void main(String[] args){
		Fornecedor fornecedorA = new Fornecedor("Jorge", "Rua sei la das quantas", "(11) 99999-9999");
		Fornecedor fornecedorB = new Fornecedor("Pedro Paulo", "Avenida padre fabio de melo", "(21) 88888-8888");

		Peca peca = new Peca(1, "motor de chevet", 2000, fornecedorA);
		Servico servico = new Servico(2, "mecanica", 5000, fornecedorB, 2);

		peca.repor(13);

		peca.vender(5);
		servico.vender(3);
		
		float pecaFaturamento = peca.getFaturamento();
		float servicoFaturamento = servico.getFaturamento();

		if(pecaFaturamento > servicoFaturamento)
			feedback(peca.getFornecedor().getNome(), "peca");
		else if(pecaFaturamento == servicoFaturamento)	
			System.out.println("Os dois produtos tiveram o mesmo faturamento");
		else
			feedback(servico.getFornecedor().getNome(), "servico");

	}

	private static void feedback(String nomeFornecedor, String produto){
		System.out.println("As vendas do " + produto + " fornecido pelo " + nomeFornecedor + " tiveram maior faturamento");
	}
}
