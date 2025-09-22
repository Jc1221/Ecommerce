*** Settings ***
Library    SeleniumLibrary
Library    BuiltIn
Resource    Test_Resources.robot
Suite Setup    Open Website
Suite Teardown    Close Browser

*** Test Cases ***
Verify Homepage Loads
    Page Should Contain    Hello World!
    Title Should Be    ecommerce.com

User Login Success
    [Documentation]    Test successful user login with valid credentials
    Navigate To Home Page
    Navigate To Login Page
    Input Email    test1@example.com
    Input Password    testpassword123
    Click Login Button
    Verify Login Success    test1@example.com

User Login Fails With Wrong Password
    [Documentation]    Test login failure with incorrect password
    Navigate To Home Page
    Navigate To Login Page
    Input Email    test1@example.com
    Input Password    wrongpassword
    Click Login Button
    Verify Login Failure

User Can Browse Products
    [Documentation]    Test product browsing functionality
    Navigate To Home Page
    Navigate To Products Page
    Click View Button For Product    1
    Verify Product Details Page    Product

User Can Add Product To Cart
    [Documentation]    Test adding product to shopping cart
    Navigate To Home Page
    Navigate To Products Page
    Click View Button For Product    1
    Add Product To Cart
    Navigate To Cart
    Verify Cart Contains Product    Product