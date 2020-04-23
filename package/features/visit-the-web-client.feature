Feature: visit the web client


  @fixture.browser
  Scenario: visit the web client
    When I visit the web client
    And I log in
    And I click on "Sales Invoice"
    Then I see the "Sales Invoice" form
    When I fill in "Customer Name" with "Bruce"
    And I click on "C00329"
    And I select "Item" from "Type"
