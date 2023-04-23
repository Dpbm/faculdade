package produto;

public class Produto{
  private String descricao;
  private float preco;
  private int quantidade;

  public Produto(int quantidade, float preco, String descricao){
    this.quantidade = quantidade;
    this.preco = preco;
    this.descricao = descricao;
  }

  public String getDescricao(){
    return this.descricao;
  }

  public float getPreco(){
    return this.preco;
  }

  public int getQuantidade(){
    return this.quantidade;
  }

  public void repor(int quantidade){
    this.quantidade += quantidade;
  }

  public boolean vender(int quantidade){
    if(quantidade <= 0 || quantidade > this.quantidade)
      return false;

    this.quantidade -= quantidade;
    return true;
  }
}
