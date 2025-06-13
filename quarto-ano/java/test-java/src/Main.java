import java.util.ArrayList;
import java.util.List;

public class Main {

    public static int getBattery(List<Integer> eventos){
        eventos.add(50); // uma vez que a bateria começa 50% carregada
        int total = 0;
        for (int i : eventos){
            int tmpSum = total+i;
            total = Math.min(tmpSum, 100); // uma vez que a bateria não pode ultrapassar 100%
        }

        return total;

    }

    public static void main(String[] args) {
        List<Integer> values = new ArrayList<>();
        values.add(10);
        values.add(-20);
        values.add(61);
        values.add(-15);
        System.out.println("Valor final: " + getBattery(values));
    }
}