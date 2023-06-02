class Fornecedor{
	private int codigo;
	private String nome, endereco, telefone;

	public Fornecedor(int codigo, String nome, String endereco, String telefone){
		this.codigo = codigo;
		this.nome = nome;
		this.endereco = endereco;
		this.telefone = telefone;
	}

	public int getCodigo(){
		return this.codigo;
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

	public void setNome(String nome){
		this.nome = nome;
	}

	public void setEndereco(String endereco){
		this.endereco = endereco;
	}

	public void setTelefone(String telefone){
		this.telefone = telefone;
	}
}

abstract class Produto{
	private int codigo;
	private String descricao;
	private float preco;
	private Fornecedor fornecedor;

	public Produto(int codigo, String descricao, float preco){
		this.codigo = codigo;
		this.descricao = descricao;
		this.preco = preco;
	}

	public int getCodigo(){
		return this.codigo;
	}

	public String getDescricao(){
		return this.descricao;
	}

	public float getPreco(){
		return this.preco;
	}

	public Fornecedor getFornecedor(){
		return this.fornecedor;
	}

	public void setFornecedor(Fornecedor fornecedor){
		this.fornecedor = fornecedor;
	}

	public abstract boolean vender(float v);
	public abstract void repor(float v);
}


class Pacote extends Produto{
	private int qtde;
	public Pacote(int codigo, String descricao, float preco, int qtde){
		super(codigo, descricao, preco);
		this.qtde = qtde;
	}

	public boolean vender(float qtde){
		if(qtde <= 0 || qtde > this.qtde)
			return false;
		
		this.qtde -= qtde;
		return true;
	}

	public void repor(float qtde){
		this.qtde += qtde;
	}
}

class Granel extends Produto{
	private float peso;

	public Granel(int codigo, String descricao, float preco, float peso){
		super(codigo, descricao, preco);
		this.peso = peso;
	}

	public boolean vender(float peso){
		if(peso <= 0 || peso > this.peso)
			return false;

		this.peso -= peso;
		return true;
	}

	public void repor(float peso){
		this.peso += peso;
	}
}

class Liquido extends Produto{
	private float volume;

	public Liquido(int codigo, String descricao, float preco, float volume){
		super(codigo, descricao, preco);
		this.volume = volume;
	}

	public boolean vender(float volume){
		if(volume <= 0 || volume > this.volume)
			return false;

		this.volume -= volume;
		return true;
	}

	public void repor(float volume){
		this.volume += volume;
	}
}

public class Exercicio_6{
	public static void main(String[] args){
		Fornecedor f1 = new Fornecedor(1, "fornecedor A", "avenida das dores 1", "111111111");
		Fornecedor f2 = new Fornecedor(2, "fornecedor B", "avenida das dores 2", "222222222");
		Fornecedor f3 = new Fornecedor(3, "fornecedor C", "avenida das dores 3", "333333333");

		Pacote p1 = new Pacote(1, "produto A", 10.5f, 10);
		Granel p2 = new Granel(2, "produto B", 30.4f, 2.5f);
		Liquido p3 = new Liquido(3, "produto C", 45.49f, 4.3f);

		p1.setFornecedor(f1);
		p2.setFornecedor(f2);
		p3.setFornecedor(f3);

		p1.vender(4);
		p2.repor(40);

		float p1_preco = p1.getPreco();	
		float p2_preco = p2.getPreco();	
		float p3_preco = p3.getPreco();	

		if(p1_preco > p2_preco && p1_preco > p3_preco)
			mostrarFornecedor(p1.getFornecedor());
		else if (p2_preco > p3_preco)
			mostrarFornecedor(p2.getFornecedor());
		else
			mostrarFornecedor(p3.getFornecedor());

	}

	public static void mostrarFornecedor(Fornecedor fornecedor){
		System.out.println("-----Fornecedor-----");
		System.out.println("codigo: " +fornecedor.getCodigo());
		System.out.println("nome: " +fornecedor.getNome());
		System.out.println("endereco: " +fornecedor.getEndereco());
		System.out.println("telefone: " +fornecedor.getTelefone());

	}
}
		
