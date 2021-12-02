Feature: Amazon.in search
  Scenario: Search iphone on Amazon.in
     Given  chrome is launched
    When we navigate to Amazon website
    And we enter product "Ear buds" in search bar
    And we press the search button
    Then we successfully navigate to the product list page
