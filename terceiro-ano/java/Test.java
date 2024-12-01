class Data{
	public synchronized void print(){
		for(int i = 0; i < 10; i++){
			System.out.println("Data: " +i);
		}
	}
}


class Default extends Thread{
	private Data data = new Data();

	public void run(){
		data.print();
	}
}

class Atomic extends Thread{
	private Data data;

	public Atomic(Data data){
		this.data = data;
	}

	public void run(){
		this.data.print();	
	}
}


public class Test {
	public static void main(String[] args){
		Default d1 = new Default();
		Default d2 = new Default();
		
		try{
			d1.start();
			d2.start();

			d1.join();
			d2.join();
		}catch(Exception e){}


		Data data = new Data();
		Atomic a1 = new Atomic(data);
		Atomic a2 = new Atomic(data);		
		

		System.out.println("Atomic...");
		try{
			a1.start();
			a2.start();

			a1.join();
			a2.join();
		}catch(Exception e){}
	}

}
