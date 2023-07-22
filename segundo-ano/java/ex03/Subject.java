package subject;

import teacher.Teacher;

public class Subject{
    private int code, totalHours;
    private String name;

    private Teacher teacher;

    public Subject(int code, int totalHours, String name){
        this.code = code;
        this.totalHours = totalHours;
        this.name = name;
    }

    public void setTeacher(Teacher teacher){
        this.teacher = teacher;
    }

    public Teacher getTeacher(){
        return this.teacher;
    }

    public String getName(){
        return this.name;
    }

}