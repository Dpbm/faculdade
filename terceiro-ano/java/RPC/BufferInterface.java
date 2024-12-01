import java.rmi.Remote;
import java.rmi.RemoteException;

public interface BufferInterface extends Remote{
	void produzir(int item) throws RemoteException, InterruptedException;
}
