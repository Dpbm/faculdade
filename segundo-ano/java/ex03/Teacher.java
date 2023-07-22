package teacher;

public class Teacher{
    private String name, education, titulation;

    public Teacher(String name, String education, String titulation){
        this.name = name;
        this.education = education;
        this.titulation = titulation;
    }

    public String getName(){
        return this.name;
    }
}