package Mokito9;
import static org.junit.Assert.*;  
import static org.mockito.Mockito.mock;  
import static org.mockito.Mockito.when;  
  import java.util.List;  
import org.junit.Test;  
import org.mockito.Mockito;
import static org.mockito.Mockito.mock;

public class TestList {  
     @Test(expected = RuntimeException.class)  
      public void testList_ThrowsException() {  
               List<String> mocklist = mock(List.class);  
              when(mocklist.get(Mockito.anyInt())).thenThrow(new RuntimeException("Error.."));  
      mocklist.get(0);  
      }  
 }  


