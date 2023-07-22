import calculadora.Calculadora;

public class Main {
    public static void main(String[] args){
        Calculadora calculadora = new Calculadora(10, 10);

        System.out.println(calculadora.retornaSoma());
        System.out.println(calculadora.retornaMultiplicacao());

        calculadora.setaNumeros(20.4f, 20.5f);

        System.out.println(calculadora.retornaSoma());
        System.out.println(calculadora.retornaMultiplicacao());

    }
}