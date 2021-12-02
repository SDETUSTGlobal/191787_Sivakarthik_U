package com.app.mockito;
import static org.junit.Assert.*; 
import java.util.List; 
import org.junit.Test; 
  public class ToDoBusinessstub { 
      @Test 
    public void test() { 
            ToDoService doServicestub = new ToDoServicestub();  
                      ToDoBusiness business = new ToDoBusiness(doServicestub); 
              List<String> retrievedtodos = business.getTodosforSpring(" Dummy "); 
                  assertEquals(2, retrievedtodos.size()); 
       System.out.println(" Stub is working correctly...!!"); 
       }  //https://drive.google.com/drive/folders/1ftEfIslWqco39pKT8v-DDZzHugaTBhLu
 
 }  
  




