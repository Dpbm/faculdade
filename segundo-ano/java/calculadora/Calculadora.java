package calculadora;

public class Calculadora{
    private float numero1, numero2;

    public Calculadora(int n1, int n2){
        this.numero1 = n1;
        this.numero2 = n2;
    }

    public Calculadora(float n1, float n2){
        this.numero1 = n1;
        this.numero2 = n2;
    }

    public float retornaSoma(){
        return this.numero1 + this.numero2;
    }

    public float retornaMultiplicacao(){
        return this.numero1 * this.numero2;
    }

    public void setaNumeros(int n1, int n2){
        this.numero1 = n1;
        this.numero2 = n2;
    }

    public void setaNumeros(float n1, float n2){
        this.numero1 = n1;
        this.numero2 = n2;
    }
}