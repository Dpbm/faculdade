package venda;

import java.util.Date;
import comprador.Comprador;
import produto.Produto;

public class Venda{
  private Date data;
  private Comprador cliente;
  private int quantidade;
  private float valorTotal;

  public Venda(Date data){
    this.data = data;
  }

  public void setCliente(Comprador comprador){
    this.cliente = comprador;
  }

  public Comprador getCliente(){
    return this.cliente;
  }

  public Produto getProduto(){
    return this.produto;
  }

  public float getValorTotal(){
    return this.valorTotal;
  }

  public boolean venderProduto(Produto produto, int quantidade){
    if(produto.vender(quantidade)){
      this.produto = produto;
      this.quantidade = quantidade;
      this.valorTotal = produto.getPreco() * quantidade;
      return true;
    }
    return false;
  }
}
