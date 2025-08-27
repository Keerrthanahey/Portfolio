// Simple Java program demonstrating OOP concepts

class Student {
    String name;
    int age;
    String course;

    // Constructor
    Student(String name, int age, String course) {
        this.name = name;
        this.age = age;
        this.course = course;
    }

    // Method
    void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Course: " + course);
    }
}

public class StudentDemo {
    public static void main(String[] args) {
        Student s1 = new Student("Keerthana", 17, "Mechanical Engineering");
        s1.displayDetails();
    }
}
