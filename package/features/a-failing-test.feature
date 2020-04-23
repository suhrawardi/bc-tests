Feature: This test fails


  @fixture.browser
  Scenario: this test fails
    When I visit the web client
    And I log in
    And I go to the "Sales Orders" page
    Then I see "Bruce Schwarz"
    When I click on "1011"
    Then I see "1011 ∙ Bruce Schwarz"
    And I see "some bogus content"
