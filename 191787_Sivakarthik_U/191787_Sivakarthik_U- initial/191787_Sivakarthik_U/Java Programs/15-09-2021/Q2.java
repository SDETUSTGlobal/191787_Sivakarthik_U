class Q2
{
  double n1,n2,n3,n4,n5,k;
  public void num(int a,double b,int c,double d,int e)
  {
    n1=a;
	n2=b;
	n3=c;
	n4=d;
	n5=e;
	k=(n1+n2+n3+n4+n5)/100;
	System.out.println(k);
  }
   public void num(double a,int b,double c,int d,double e)
  {
    n1=a;
	n2=b;
	n3=c;
	n4=d;
	n5=e;
	k=(n1+n2+n3+n4+n5)/5;
	System.out.println(k);
  }
  public void num(double a,double b,int c,int d,int e)
  {
    n1=a;
	n2=b;
	n3=c;
	n4=d;
	n5=e;
	System.out.println(c);
  }
  public void num(int a,int b)
  {
    n1=a;
	n2=b;
	if(n1>n2)
	{
	   System.out.println(n1);
	}
	else
	{
	   System.out.println(n2);
	}
  }
  public void num(double a,int b)
  {
    n1=a;
	n2=b;
	if(n1<n2)
	{
	   System.out.println(n1);
	}
	else
	{
	   System.out.println(n2);
	}
  }
  public static void main(String args[])
  {
    System.out.println("Numbers : 1,2,3,4,5");
	Q2 ob=new Q2();
	
	System.out.println("Percentage :" 	);
	ob.num(1,2.0,3,4.0,5);
	
	System.out.println("Average :" );
	ob.num(1.0,2,3.0,4,5.0);
	
	System.out.println("Median  :");
	ob.num(1.0,2.0,3,4,5);
	
	System.out.println("Maximum : ");
    ob.num(3,4);

    System.out.println("Minimum : ");
    ob.num(2.0,3);
  }
}
  
	
	