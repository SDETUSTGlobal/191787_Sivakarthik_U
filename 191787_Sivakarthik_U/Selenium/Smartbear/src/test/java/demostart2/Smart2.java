package demostart2;
import org.openqa.selenium.By;  
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;  
import cucumber.annotation.en.Given;  
import cucumber.annotation.en.Then;  
import cucumber.annotation.en.When;
public class Smart2 
{

WebDriver driver= null;
 @Given("^I am on user login page$")  
 public void goToWebLogin() 
 {  
 
	 System.setProperty("webdriver.chrome.driver", "D://Selenium//chromedriver_win32//chromedriver.exe");
 driver= new ChromeDriver();
 driver.navigate().to("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Products.aspx");  
 }  
   
 @When("^I enter valid data on the page$")  
 public void inputData()
 {
   driver.findElement(By.linkText("View all products")).click();
 }

 @Then("^User login should be successful$")  
 public void User_login_should_be_successful() 
 { 
	 if(driver.getTitle().equalsIgnoreCase("Web Orders"))
	 {  
 
     System.out.println("Test Pass");  
     } 
 else 
 {  
     System.out.println("Test Failed");  
  }  
 }
}
 