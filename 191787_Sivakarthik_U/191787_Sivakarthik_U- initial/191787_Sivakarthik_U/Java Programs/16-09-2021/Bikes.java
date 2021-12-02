import java.io.*;
class Factory
{
	
	void Car()
	{
		System.out.println("Manufacturing ");
	}
}
class Bikes{
	Factory f;
	
	void parts()
	{
		f = new Factory();
		f.Car();
	}
	public static void main(String args[])
	{
		Bikes b =  new Bikes();
		b.parts();
		int arr[]={1,2,3,4};
	int i;
	for( i=0;i<arr.length;i++)
	{
	   System.out.println(arr[i]);
	}
		
	}
}
 
   
	 
   
 