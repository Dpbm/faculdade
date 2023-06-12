interface Pagamento{
  public float calcularPagamento();
  public void exibirRecibo();
}

class PagamentoBoleto implements Pagamento{
  private float valor;

  public PagamentoBoleto(float valor){
    this.valor = valor;
  }

  public float calcularPagamento(){
    return this.valor;
  }

  public void exibirRecibo(){  
    System.out.println("Valor - R$", this.valor);
    System.out.println("Pagamento Realizado usando boleto");
  }
}

class PagamentoCartao implements Pagamento{
  private float valor;
  private String tipo;

  public PagamentoCartao(float valor, String tipo){
    this.valor = valor;
    this.tipo = tipo;
  }

  public float calcularPagamento(){
    return this.valor;
  }

  public void exibirRecibo(){
    System.out.println("Valor - R$", this.valor);
    System.out.println("Pagamento Realizado usando cartao de "+this.tipo);
  }
}

public class PagamentoMain{
  public static void main(String[] args){
    //PagamentoBoleto boleto = new PagamentoBoleto(10.30f);
    Pagamento boleto = new  PagamentoBoleto(10.30f);
    //PagamentoCartao cartao = new PagamentoCartao(30.23f, "debito");
    Pagamento cartao = new PagamentoCartao(30.23f, "debito");
    boleto.exibirRecibo();
    cartao.exibirRecibo();
  }
}
