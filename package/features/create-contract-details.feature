Feature: create contract details on the SOAP endpoint


  @soap
  Scenario: create contract details on the SOAP endpoint
    Given a contract details SOAP endpoint
    When I fetch the first 3 records from the SOAP endpoint filtered by
      | filter                       | value                 |
      | Contract_Type_Code           | PC-FIX                |
    Then I received 3 records
    When I create a new record on the SOAP endpoint with
      | key                          | value                 |
      | Contract_Type_Code           | PC-FIX                |
      | Sell_to_Customer_No          | C00389                |
      | Sell_to_Contact_No           | CT00255               |
      | Order_Date                   | 2020-03-30            |
      | Template_Code                | TIPS ADVIES           |
      | Salesperson_Code             | PMU                   |
      | Order_Type_Code              | BACKORDER             |
      | Bill_to_Customer_No          | C00389                |
      | Bill_to_Contact_No           | CT00255               |
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
    When I fetch the created record from the SOAP endpoint
    Then I receive a record with
      | key                          | value                 |
      | Contract_Type_Code           | PC-FIX                |
      | Sell_to_Customer_No          | C00389                |
      | Sell_to_Contact_No           | CT00255               |
      | Sell_to_Cont_Alt_Addr_Code   | _MAIN                 |
      | Sell_to_Name                 | Institute of Medicine |
      | Sell_to_Address              | 611 Huse Road         |
      | Sell_to_Post_Code            | 03103                 |
      | Sell_to_City                 | Manchester            |
      | Sell_to_Country_Region_Code  | US                    |
      | Sell_to_Contact              | Melanie Nicholson     |
      | Template_Code                | TIPS ADVIES           |
      | Salesperson_Code             | PMU                   |
      | Order_Type_Code              | BACKORDER             |
      | Bill_to_Customer_No          | C00389                |
      | Bill_to_Contact_No           | CT00255               |
      | Bill_to_Cont_Alt_Addr_Code   | _MAIN                 |
      | Bill_to_Name                 | Institute of Medicine |
      | Bill_to_Address              | 611 Huse Road         |
      | Bill_to_Post_Code            | 03103                 |
      | Bill_to_City                 | Manchester            |
      | Bill_to_Country_Region_Code  | US                    |
      | Bill_to_Contact              | Melanie Nicholson     |
    When I delete the created record from the SOAP endpoint
    Then the delete succeeded
    When I fetch the created record from the SOAP endpoint
    Then I do not receive a record
