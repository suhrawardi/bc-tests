Feature: fetch contract details on the SOAP endpoint


  @soap
  Scenario: fetching a contract details record
    Given a contract details SOAP endpoint
    When I fetch "KVVV100187" from the SOAP endpoint
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


  @soap
  Scenario: fetching a contract details record that does not exist
    Given a contract details SOAP endpoint
    When I fetch "KVVV000000" from the SOAP endpoint
    Then I do not receive a record
