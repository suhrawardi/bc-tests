Feature: fetch Klanten on the OData endpoint


  @odata
  Scenario: fetching Klanten records
    Given an OData endpoint for "Klanten"
    When I fetch the first 2 records from the OData endpoint
    Then I received 2 records


  @odata
  Scenario: fetching a single Klanten record
    Given an OData endpoint for "Klanten"
    When I fetch "KVVV000000" from the OData endpoint
    Then I receive a record with
      | key                          | value                 |
      | Contract_Type_Code           | PC-FIX                |
      | Sell_to_Customer_No          | C00389                |
      | Sell_to_Contact_No           | CT00255               |
      | Template_Code                | TIPS ADVIES           |
      | Salesperson_Code             | PMU                   |
      | Order_Type_Code              | BACKORDER             |
      | Bill_to_Customer_No          | C00389                |
      | Bill_to_Contact_No           | CT00255               |
