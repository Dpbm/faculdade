import teacher.Teacher;
import subject.Subject;

public class Main{
    public static void main(String[] args){
        Subject subject = new Subject(1234, 80, "Programacao orientada a objetos");
        Teacher teacher1 = new Teacher("marmo", "ciencias da computacao", "Doutor");
        Teacher teacher2 = new Teacher("marmo2", "ciencias da computacao", "Doutor");

        subject.setTeacher(teacher1);

        System.out.println(subject.getTeacher().getName());
    }
}