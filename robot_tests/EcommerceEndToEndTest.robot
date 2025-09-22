*** Settings ***
Resource    Test_Resources.robot
Library    BuiltIn

*** Test Cases ***
Open Website Test
    Open Website

Generate Random Email Test
    ${email} =    Generate Random Email
    Set Suite Variable    ${EMAIL}    ${email}

Register User Test
    Register User    ${EMAIL}

Login User Test
    Login User    ${EMAIL}

View Product Test
    View Product

Add To Cart Test
    Add To Cart

Checkout Test
    Checkout

Logout User Test
    Logout User

Close Website Test
    Close Website

Summary Test
    Log    End To End Completed