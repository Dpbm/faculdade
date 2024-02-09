namespace hello_2;

public class Fibo{
	public int f(int n){
		if(n<=1)
			return 1;
		return f(n-1)+f(n-2);
	}
}

public class Program
{

    static void Main(string[] args)
    {
	Fibo fib = new Fibo();	
        Console.WriteLine(fib.f(10));
    }	
}

