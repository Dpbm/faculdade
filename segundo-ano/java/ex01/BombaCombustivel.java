package bomba;

public class BombaCombustivel{
	private int nroBomba, tipoCombustivel;
	private float litrosCombustivel, preco;

	public BombaCombustivel(int nroBomba, int tipoCombustivel, float litrosCombustivel, float preco){
		this.nroBomba = nroBomba;
		this.tipoCombustivel = tipoCombustivel;
		this.litrosCombustivel = litrosCombustivel;
		this.preco = preco;
	}

	public float abastecerPorValor(float valor){
		float totalDeLitros = totalDeLitrosPeloValor(valor);

		atualizarLitrosCombustivel(totalDeLitros);	

		return totalDeLitros;

	}
	
	private float totalDeLitrosPeloValor(float valor){
		if(valor <= 0) 
			return 0;

		return this.preco / valor;
	}


	private void atualizarLitrosCombustivel(float totalLitrosRemovido){
		this.litrosCombustivel -= totalLitrosRemovido;
	}

	public float abastecerPorLitros(float litros){
		float precoTotal = precoTotalPelosLitros(litros);
	
		atualizarLitrosCombustivel(litros);

		return precoTotal;
	}


	private float precoTotalPelosLitros(float litros){
		return litros * this.preco;
	}

	public void reabastecerTanque(float qtdeLitros){
		atualizarLitrosCombustivel(qtdeLitros);
	}
	
	public void alterarPreco(float novoPreco){
		this.preco = novoPreco;
	}
}


