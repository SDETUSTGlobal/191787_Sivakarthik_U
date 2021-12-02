Feature: Outlook Login
  Scenario: Navigate to Outlook and login
     Given  chrome is launched
    When we navigate to Rediff website
    And we enter username "Siva@gmail.com" password "xxxx"
    And we press the login button
    Then we successfully navigate to login incorrect page
