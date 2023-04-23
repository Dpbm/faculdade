 import produto.Produto;
 import comprador.Comprador;
 import venda.Venda;
 import java.util.Date;

 public class Main{
   public static void main(String[] args){
     Comprador comprador = new Comprador("Joao da Silva", "endereco", "telefone");
     Produto produto = new Produto(10, 50, "mouse gyuaimer");
     Venda venda = new Venda(new Date());
     venda.setCliente(comprador);
     boolean vendido = venda.venderProduto(produto, 1);
     if(vendido)
      System.out.println("Venda realizada com sucesso\ntotal da venda: "+venda.getValorTotal());
     else
      System.out.println("Nao foi possivel realizar a venda!");
   }
 }
