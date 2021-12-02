package Travel;  

public class Place implements visit
{  
 public static void main(String args[])
   {  
	Place obj = new Place();
	obj.display();
    System.out.println("Safe Journey");  
   }  
}

interface visit
{
		default void display()
		{
			System.out.println("Hello Travellers");
		}
}
	