namespace hello_1;

class Program{
    static int fibonacci(int n){
    	if(n<=1)
		return 1;
	return fibonacci(n-1)+fibonacci(n-2);
    }

    static void Main(string[] args){
        int last_fib = 1;
	int pen_fib = 1;
	int n = 10;
	int fib = 1;

	for(int i = 1; i < n; i++){
		fib = last_fib+pen_fib;
		pen_fib = last_fib;
		last_fib = fib;
	}
	Console.WriteLine(fib);
	//Console.WriteLine(fibonacci(10));
    }
}
