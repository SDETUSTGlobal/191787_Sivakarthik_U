Feature: Myntra Product Browsing
  As a online buyer,
  I want to find new products online,
  So I can try out new products.

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

  Scenario: Basic Myntra Product Search For Shirts
    Given the Myntra home page is displayed
    When the user searches for "Shirts"
    Then results are shown for "Shirts"