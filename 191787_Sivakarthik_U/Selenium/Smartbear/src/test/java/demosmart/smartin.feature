Feature: Login Functonality

Scenario: Successful Login with Valid Credentials
 Given User is on Home page
 
 When User enters Credentials to Login
  | Tester | test |
  Then message displayed Login Successful