import java.io.*;
public class StudentTest 
{

   public static void main(String args[]) 
   {
     
      Student stOne = new Student("ABC");
      Student stTwo = new Student("DEF");
	  Student stThree = new Student("GHI");

     
      stOne.stAge(20);
      stOne.stMark(50);
	  stOne.printStudent();
      
	  
	  stTwo.stAge(21);
      stTwo.stMark(70);
	  stTwo.printStudent();
	  
	  stThree.stAge(19);
      stThree.stMark(85);
	  stThree.printStudent();
	  
   }
}