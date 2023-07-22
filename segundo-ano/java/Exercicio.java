class Conta{
	private int numero;
	private String tipo;
	private float saldo;

	public Conta(int numero, String tipo, float saldo){
		this.numero = numero;
		this.tipo = tipo;
		this.saldo = saldo;
	}

	public int getNumero(){
		return this.numero;
	}

	public String getTipo(){
		return this.tipo;
	}

	public float getSaldo(){
		return this.saldo;
	}

	public void depositar(float valor){
		this.saldo += valor;
	}

	public boolean sacar(float valor){
		boolean ePossivelSacar = podeSacar(valor);
		
		if(ePossivelSacar)
			this.saldo -= valor;

		return ePossivelSacar;
	}

	private boolean podeSacar(float valor){
		return this.saldo >= valor;
	}

	public boolean transferir(float valor, Conta destino){
		boolean saqueFeito = sacar(valor);

		if(saqueFeito)
			destino.depositar(valor);

		return saqueFeito;
	}
}	

class Cliente{
	private String nome, cpf, endereco, telefone;
	private Conta conta;

	public Cliente(String nome, String cpf, String endereco, String telefone, Conta conta){
		this.nome = nome;
		this.cpf = cpf;
		this.endereco = endereco;
		this.telefone = telefone;
		this.conta = conta;
	}
	
	public String getNome(){
		return this.nome;
	}

	public String getCPF(){
		return this.cpf;
	}

	public String getEndereco(){
		return this.endereco;
	}

	public String getTelefone(){
		return this.telefone;
	}

	public Conta getConta(){
		return this.conta;
	}
}

public class Exercicio{
	public static void main(String[] args){
		Conta conta1 = new Conta(1, "CC", 1200);
		Conta conta2 = new Conta(2, "CP", 1400);

		Cliente cliente1 = new Cliente("Joao", "057.586.840-66", "avenida 123456", "(11) 1111-1111", conta1);
		Cliente cliente2 = new Cliente("Jorge", "485.316.670-03", "rua 456", "(11) 3333-3333", conta2);


		cliente1.getConta().depositar(1000);
		cliente2.getConta().depositar(2000);
		
		float valorSaque1 = 500;
		float valorSaque2 = 150;
		boolean sucessoSaqueConta1 = cliente1.getConta().sacar(valorSaque1);
		boolean sucessoSaqueConta2 = cliente2.getConta().sacar(valorSaque2);

		feedbackSaque(sucessoSaqueConta1, cliente1, valorSaque1);
		feedbackSaque(sucessoSaqueConta2, cliente2, valorSaque2);
		
		float valorTransferencia = 7000;
		boolean sucessoTransferencia = cliente1.getConta().transferir(valorTransferencia, cliente2.getConta());
		feedbackTransferencia(sucessoTransferencia, cliente1, cliente2, valorTransferencia);
	}

	private static void feedbackSaque(boolean sucesso, Cliente cliente, float valor){
		if(sucesso){
			System.out.println("Sucesso ao realizar o saque de R$"+valor+" para "+cliente.getNome()); 
			return;
		}

		System.out.println("Falha ao tentar realizar o saque de R$"+valor+" para "+cliente.getNome()); 
	}

	private static void feedbackTransferencia(boolean sucesso, Cliente cliente1, Cliente cliente2, float valor){
		if(sucesso){
			System.out.println("Sucesso ao realizar a transferencia de R$"+valor+" de "+cliente1.getNome()+" para "+cliente2.getNome());
			return;
		}

		System.out.println("Falha ao realizar a transferencia de R$"+valor+" de "+cliente1.getNome()+" para "+cliente2.getNome());
	}
}
