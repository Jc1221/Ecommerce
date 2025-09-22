*** Settings ***
Library    SeleniumLibrary
Library    String
Library    Process
Library    BuiltIn

*** Variables ***
${URL}    http://localhost:8000
${BROWSER}    chrome
${PASSWORD}    testpass123
${DELAY}    0.65    # 添加延迟变量，单位为秒

*** Keywords ***
Log Step Status
    [Arguments]    ${step_name}
    Log To Console    ${step_name} PASS

Open Website
    Set Selenium Speed    ${DELAY}
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    ${DELAY}
    Log Step Status    Open Website

Close Website
    Close Browser
    Log Step Status    Close Website

Generate Random Email
    ${random_string} =    Generate Random String    10    [LOWER]
    ${email} =    Set Variable    ${random_string}@example.com
    Log Step Status    Generate Random Email
    RETURN    ${email}

Register User
    [Arguments]    ${email}
    Go To    ${URL}/register/
    Sleep    ${DELAY}
    Input Text    id=id_email    ${email}
    Input Text    id=id_password1    ${PASSWORD}
    Input Text    id=id_password2    ${PASSWORD}
    Sleep    ${DELAY}
    Click Button    xpath=//button[contains(text(),'Register')]
    Wait Until Location Contains    /login/
    Sleep    ${DELAY}
    Log Step Status    Register User

Login User
    [Arguments]    ${email}
    Go To    ${URL}/login/
    Sleep    ${DELAY}
    Input Text    id=id_email    ${email}
    Input Text    id=id_password    ${PASSWORD}
    Sleep    ${DELAY}
    Click Button    xpath=//button[contains(text(),'Login')]
    Wait Until Location Does Not Contain    /login/
    Sleep    ${DELAY}
    Log Step Status    Login User

View Product
    Go To    ${URL}/products/
    Sleep    ${DELAY}
    Wait Until Page Contains Element    xpath=//a[contains(@href,'/products/') and contains(@class,'btn-primary')]    timeout=10s
    Sleep    ${DELAY}
    Click Element    xpath=//a[contains(@href,'/products/') and contains(@class,'btn-primary')][1]
    Wait Until Page Contains Element    xpath=//button[contains(text(),'Add to Cart')]    timeout=10s
    Sleep    ${DELAY}
    Log Step Status    View Product
    Sleep    ${DELAY}

Add To Cart
    Click Button    xpath=//button[contains(text(),'Add to Cart')]
    Wait Until Location Contains    /cart/    timeout=10s
    Sleep    ${DELAY}
    Log Step Status    Add To Cart

Checkout
    Go To    ${URL}/cart/
    Sleep    ${DELAY}
    Click Link    xpath=//a[contains(@href,'/checkout/')]
    Sleep    ${DELAY}
    Log Step Status    Checkout
    # 填写 shipping 地址
    Input Text    id=id_address_line_1    123 Test St
    Input Text    id=id_address_line_2    Apt 4
    Input Text    id=id_city    Test City
    Input Text    id=id_country    United States
    Input Text    id=id_state    TS
    Input Text    id=id_postal_code    12345
    Sleep    ${DELAY}
    Click Button    xpath=//button[contains(text(),'Save Address & Continue')]
    # 等待 billing 表单加载
    Wait Until Page Contains Element    id=id_address_line_1    timeout=15s
    Wait Until Element Is Visible    id=id_address_line_1    timeout=15s
    Wait Until Element Is Enabled    id=id_address_line_1    timeout=15s
    Sleep    ${DELAY}
    # 填写 billing 地址
    Input Text    id=id_address_line_1    123 Test St
    Input Text    id=id_address_line_2    Apt 4
    Input Text    id=id_city    Test City
    Input Text    id=id_country    United States
    Input Text    id=id_state    TS
    Input Text    id=id_postal_code    12345
    Sleep    ${DELAY}
    Click Button    xpath=//button[contains(text(),'Save Address & Continue')]
    Sleep    ${DELAY}
    # 最终结账
    Wait Until Page Contains Element    xpath=//button[contains(text(),'Finalize Checkout')]    timeout=10s
    Sleep    ${DELAY}
    Click Button    xpath=//button[contains(text(),'Finalize Checkout')]
    Wait Until Page Contains    Thank you for your order    timeout=10s
    Sleep    ${DELAY}

Logout User
    Go To    ${URL}
    Sleep    ${DELAY}
    # 点击用户下拉菜单
    Wait Until Element Is Visible    id=userDropdown    timeout=10s
    Wait Until Element Is Enabled    id=userDropdown    timeout=10s
    Sleep    ${DELAY}
    Click Element    id=userDropdown
    Sleep    ${DELAY}
    # 点击退出链接
    Wait Until Element Is Visible    xpath=//a[contains(@href,'/logout/')]    timeout=10s
    Wait Until Element Is Enabled    xpath=//a[contains(@href,'/logout/')]    timeout=10s
    Sleep    ${DELAY}
    Click Link    xpath=//a[contains(@href,'/logout/')]    
    Log Step Status    Logout User
    Wait Until Location Contains    /login/
    Sleep    ${DELAY}