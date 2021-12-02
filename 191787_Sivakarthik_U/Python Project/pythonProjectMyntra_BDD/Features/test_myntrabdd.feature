Feature: Myntra.com.in search
  Scenario: Search Sunglasses on Myntra.com
     Given  chrome is launched
    When we navigate to Myntra website
    And we enter product "Sunglasses" in search bar
    And we press the search button
    Then we successfully navigate to the product list page



