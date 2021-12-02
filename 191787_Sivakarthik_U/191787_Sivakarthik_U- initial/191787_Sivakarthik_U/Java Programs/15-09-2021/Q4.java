class Q4
{
	public static void main(String args[])
	{
		char grade;
		grade = 'A';
		switch(grade)
		{
			case 'A' : 
			{
			  for(int i =1;i<=100;i++)
			  {
				  if((i%2)!=0)
				  {
					  System.out.println(i);
				  }
			  }
			  break;
			}
			case 'B' :
			  {
				  for(int i=1;i<=100;i++)
				  {
					  if((i%2)==0)
					  {
						  System.out.println(i);
					  }
				  }
				  break;
			  }
			  case 'C' :
			  {
				  int n =16;
				  int s=(int)Math.sqrt(n);
				  if(n==s)
				  {
					  System.out.println("It is a Perfect Square.");
				  }
				  else
				  {
					  System.out.println("It is not a Perfect Square.");
				  }
				  break;
			  }
			  case 'D' :
			  {
				  int d=3;
				  if(d>0)
				  {
					  System.out.println("It is a Positive Integer.");
				  }
				  else
				  {
					  System.out.println("It is a Negative Integer .");
				  }
				  break;
			  }
			  case 'E' :
			  {
				  int a =1;
				  int b=3;
				  int c=5;
				  if((a>b)&&(a>c))
				  {
					  System.out.println(a+"is greater than"+b);
				  }
				  else if((b>a)&&(b>c))
				  {
					  System.out.println(b+"is greater than"+c);
				  }
				  else
				  {
					  System.out.println(c+"is greater");
				  }
				  break;
			  }
			  case 'F' :
			  {
				 int num =123;
				 int r=0;
				 int rem;
				 while(num!=0)
				 {
					rem=num%10;
					r=r*10+rem;
					num=num/10;
				 }
				 System.out.println("Reversed output : "+r);
				 break;
			  }
			  default : 
			  {
				  System.out.println("Invaid input");
			  }
		}
	}
}
				 
				 
					 
				  