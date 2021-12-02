class Q3
{
	static String ClgName = "MITS";
	String name = "Siva";
	int rollno = 50;
	public static void main(String args[])
	{
		display();
		Q3 ob=new Q3();
		ob.show();
	}
	static void display()
	{
		System.out.println(Q3.ClgName);
	}
	void show()
	{
		System.out.println("Name :"+name);
		System.out.println("Roll No :"+rollno);
	}
}
	