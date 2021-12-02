public class Problem extends Exception
{  
 int a=70;
 int b=50;

 static int c=0;
 public Problem(String s)
 {
    super(s);
 }
  
  
 void change(Problem p)
 {  
 p.a=p.a+101;
 }  
 void update(int d)
 {  
   b=b+101;
 }  
static void values() throws Problem
{    
        c++;
        if(c>3)
           {throw new Problem("c > 3");  } 
       else
        {
			System.out.println(c);  
		}
        
         values();
        }
    
 public static void main(String args[])
 throws ClassNotFoundException
    {
  try {
           
           Class temp=Class.forName("Problem");
           int k = 20; 
Integer f=Integer.valueOf(k);

System.out.println(k+" "+f);  
            }
        catch (ClassNotFoundException e) 
		{
           
            System.out.println("Class does not exist check the name of the class");
        }
     
   Problem p=new Problem("c < 3");  
   System.out.println("Prior to  change "+p.a);  
   p.change(p);
   System.out.println("After change "+p.a);  
   System.out.println("Prior to change "+p.b);  
   p.update(500);  
   System.out.println("After change "+p.b);  
    
   int g[]={8,4,2,6};
for(int i=0;i<g.length;i++)
System.out.println(g[i]);  
try{
     System.out.println(g[2]/0);
   }catch(ArithmeticException e)
   {
	   System.out.println(e);
	}  
    
 try{
values();
}
catch( Problem ex)  
        {  
            System.out.println("Caught the exception");  
     System.out.println("Exception occured: " + ex);  
        }  

   
  
 }  
}  