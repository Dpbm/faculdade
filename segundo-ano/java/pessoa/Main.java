import pessoa.Pessoa;

public class Main {
    public static void main(String[] args){
        Pessoa pessoa = new Pessoa("dsadadsa");
        System.out.println(pessoa.getNome());

        pessoa.setIdade(10);
        pessoa.setTelefone("344444444444444");
        System.out.println(pessoa.getNome());
        System.out.println(pessoa.getTelefone());
        System.out.println(pessoa.getIdade());

    }
}