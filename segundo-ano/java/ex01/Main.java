import java.util.Scanner;
import bomba.BombaCombustivel;

public class Main{
	private static Scanner console = new Scanner(System.in);

	private static int nroBomba = 10;
	private static int tipoCombustivel = 0;//etanol
	private static float litrosCombustivel = 200.45f;
	private static float preco = 3.3f;
	private static BombaCombustivel bomba = new BombaCombustivel(nroBomba, tipoCombustivel, litrosCombustivel, preco);



	public static void main(String[] args){
		int opcaoAtual = 0;

		do{
			mostrarMenu();
			opcaoAtual = pegaOpcaoMenu();

			executarFuncaoPedidaPeloUsuario(opcaoAtual);

			separarLinhas();
		}while(opcaoAtual != 5);
	}


	private static void mostrarMenu(){
		System.out.println("Bomba Combustível");
		System.out.println("1 - Abastecer por valor");
		System.out.println("2 - Abastecer por litros");
		System.out.println("3 - Atualizar preço");
		System.out.println("4 - Reabastecer tanque");
		System.out.println("5 - Finalizar");
		System.out.print("Opção: ");
	}

	private static int pegaOpcaoMenu(){
		int opcao = console.nextInt();
		return opcao;
	}

	private static void separarLinhas(){
		System.out.println();
	}

	private static void executarFuncaoPedidaPeloUsuario(int opcao){
		switch(opcao){
			case 1:
				funcaoAbastecerPorValor();
				break;

			case 2:
				funcaoAbastecerPorLitros();
				break;

			case 3:
				funcaoAtualizarPreco();
				break;

			case 4:
				funcaoReabastecerTanque();
				break;

			default:
				break;
		}

	}

	private static void funcaoAbastecerPorValor(){
		float valor = pegarValorParaAbastecer();
		float totalDeLitrosAbastecidos = bomba.abastecerPorValor(valor);
		System.out.println("Abstecido " + totalDeLitrosAbastecidos + "l");
	}

	private static float pegarValorParaAbastecer(){
		System.out.print("Valor para abastecer: ");
		float valor = console.nextFloat(); 
		return valor;
	}

	private static void funcaoAbastecerPorLitros(){
		float litros = pegarTotalDeLitrosParaAbastecer();
		float precoTotal = bomba.abastecerPorLitros(litros);
		System.out.println("Preço total pago: R$" +precoTotal);
	}

	private static float pegarTotalDeLitrosParaAbastecer(){
		System.out.print("Total de litros para abastecer: ");
		float litros = console.nextFloat();
		return litros;
	}

	private static void funcaoAtualizarPreco(){
		float novoPreco = pegarNovoPreco();
		bomba.alterarPreco(novoPreco);
		System.out.println("Preço atualizado!");
	}

	private static float pegarNovoPreco(){
		System.out.print("Novo Preço do combustível: ");
		float novoPreco = console.nextFloat();
		return novoPreco;
	}

	private static void funcaoReabastecerTanque(){
		float litros = pegarLitrosParaReabastecer();
		bomba.reabastecerTanque(litros);
		System.out.println("Reabastecido!");
	}

	private static float pegarLitrosParaReabastecer(){
		System.out.print("Total de litros para reabastecer: ");
		float litros = console.nextFloat();
		return litros;
	}
}
