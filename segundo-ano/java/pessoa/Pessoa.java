package pessoa;

import java.util.Scanner;

public class Pessoa {
    private String nome, telefone;
    private int idade;

    private Scanner console = new Scanner(System.in);

    public Pessoa(String n, String t, int i ){
        this.nome = n;
        this.telefone = t;
        this.idade = i;
    }

    public Pessoa(String n){
        this.nome = n;
    }

    public String getNome(){
        return this.nome;
    }

    public String getTelefone(){
        return this.telefone;
    }

    public int getIdade(){
        return this.idade;
    }

    public void setTelefone(String t){
        this.telefone = t;
    }

    public void setIdade(int i){
        this.idade = i;
    }


}