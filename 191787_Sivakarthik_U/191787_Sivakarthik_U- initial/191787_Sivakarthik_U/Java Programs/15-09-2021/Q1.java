class Q1
{
	int a;
	int b;
	int c;
	String name;
	
	Q1()
	{
	}
	
	Q1(int i)
	{
		a=i;
	}
	Q1(int i,String s)
	{
		a=i;
		name=s;
	}
	Q1(int i,int j,int k,String s)
	{
		a=i;
		b=j;
		c=k;
		name=s;
	}
	
	void addition()
	{
		System.out.println(a+b+c);
		System.out.println(name);
	}
	void subtraction()
	{
		System.out.println((a-b)-c);
		System.out.println(name);
	}
	void multiplication()
	{
		System.out.println(a*b*c);
		System.out.println(name);
	}
	void division()
	{
		System.out.println((a/b)/c);
		System.out.println(name);
	}
	public static void main(String args[])
	{
		Q1 ob1=new Q1();
		Q1 ob2=new Q1(34);
		Q1 ob3=new Q1(34,"Siva");
		Q1 ob4=new Q1(34,11,99,"Siva");
		
		ob1.a=34;
		ob1.b=11;
		ob1.c=99;
		ob1.name="Siva";
		
		ob2.b=11;
		ob2.c=99;
		ob2.name="Siva";
		
		ob3.b=11;
		ob3.c=99;
		
		System.out.println("A=34,B=11,C=99,name=Siva");
		System.out.println("Addition :");
		ob1.addition();
		System.out.println("Subtraction : ");
		ob2.subtraction();
		System.out.println("Multiplication : ");
		ob3.multiplication();
		System.out.println("Division : ");
		ob4.division();
	}
}