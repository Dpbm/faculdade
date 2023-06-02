abstract class FormaGeometrica{
	protected float area, perimetro;
	private String nome;

	public FormaGeometrica(String nome){
		this.nome = nome;
	}

	public String getNome(){
		return this.nome;
	}

	public float getArea(){
		return this.area;
	}

	public float getPerimetro(){
		return this.perimetro;
	}

	public abstract void calcularArea();
	public abstract void calcularPerimetro();
}

class Circulo extends FormaGeometrica{
	private float raio;


	public Circulo(float raio){
		super("Círculo");
		this.raio = raio;
	}

	public void calcularArea(){
		this.area = ((float)Math.PI) * ((float)Math.pow((double)this.raio, 2));
	}

	public void calcularPerimetro(){
		this.perimetro = 2 * (float)Math.PI * this.raio;
	}
}
class Quadrado extends FormaGeometrica{
	private float lado;

	public Quadrado(float lado){
		super("Quadrado");
		this.lado = lado;
	}

	public void calcularArea(){
		this.area = (float)Math.pow((double)this.lado, 2);
	}

	public void calcularPerimetro(){
		this.perimetro = 4 * this.lado;
	}
}

class Retangulo extends FormaGeometrica{
	private float lado1;
	private float lado2;

	public Retangulo(float lado1, float lado2){
		super("Retângulo");
		this.lado1 = lado1;
		this.lado2 = lado2;
	}

	public void calcularArea(){
		this.area = this.lado1 * this.lado2;
	}

	public void calcularPerimetro(){
		this.perimetro = 2 * this.lado1 + 2 * this.lado2; 
	}
}

public class Exercicio_7{
	public static void main (String[] args){
		Circulo figura1 = new Circulo(10);
		Quadrado figura2 = new Quadrado(10);
		Retangulo figura3 = new Retangulo(4, 5);
		
		figura1.calcularArea();
		figura1.calcularPerimetro();

		figura2.calcularArea();
		figura2.calcularPerimetro();
		
		figura3.calcularArea();
		figura3.calcularPerimetro();
	
		float area_fig1 = figura1.getArea();
		float peri_fig1 = figura1.getPerimetro();

		float area_fig2 = figura2.getArea();
		float peri_fig2 = figura2.getPerimetro();

		float area_fig3 = figura3.getArea();
		float peri_fig3 = figura3.getPerimetro();

		if(area_fig1 > area_fig2 && area_fig1 > area_fig3)
			mostrarMaiorArea(figura1);
		else if(area_fig2 > area_fig3)
			mostrarMaiorArea(figura2);
		else
			mostrarMaiorArea(figura2);

		if(peri_fig1 > peri_fig2 && peri_fig1 > peri_fig3)
			mostrarMaiorPerimetro(figura1);
		else if(peri_fig2 > peri_fig3)
			mostrarMaiorPerimetro(figura2);
		else
			mostrarMaiorPerimetro(figura3);
		

	}

	public static void mostrarMaiorArea(FormaGeometrica forma){
		System.out.println("---Forma com maior area---");
		System.out.println("Nome: " + forma.getNome());
		System.out.println("Area: " + forma.getArea());
	}

	public static void mostrarMaiorPerimetro(FormaGeometrica forma){
		System.out.println("---Forma com maior perimetro---");
		System.out.println("Nome: " + forma.getNome());
		System.out.println("Perimetro: " + forma.getPerimetro());
	}
}
