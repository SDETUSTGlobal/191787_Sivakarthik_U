import java.io.*;
public class Student
 {
   String name;
   int age;
  
   double mark;

   public Student(String name)
   {
      this.name = name;
   }

   
   public void stAge(int stAge)
   {
      age = stAge;
   }

   
   

   
   public void stMark(double stMark) 
   {
      mark = stMark;
   }

   
   public void printStudent() 
   {
      System.out.println("Name:"+ name );
      System.out.println("Age:" + age );
     
      System.out.println("Marks:" + mark);
   }
}