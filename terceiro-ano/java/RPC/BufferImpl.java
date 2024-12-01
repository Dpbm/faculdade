import java.rmi.server.UnicastRemoteObject;

public class BufferImpl extends UnicastRemoteObject implements BufferInterface{
	private int buffer[];
	private int count = 0;
	private final int SIZE=5;

	public BufferImpl(){
		this.buffer = new int[this.SIZE];
	}

}
