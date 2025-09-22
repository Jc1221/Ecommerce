def start_keyword(name, attributes):
    # 只显示顶层关键字（测试步骤）
    if attributes['type'] == 'Keyword' and attributes['libname'] != 'BuiltIn':
        keyword_name = attributes['kwname']
        if keyword_name in ['Open Website', 'Generate Random Email', 'Register User', 'Login User', 'View Product', 'Add To Cart', 'Checkout', 'Logout User', 'Close Website']:
            print(f"执行: {keyword_name}")

def end_keyword(name, attributes):
    # 只显示顶层关键字（测试步骤）
    if attributes['type'] == 'Keyword' and attributes['libname'] != 'BuiltIn':
        keyword_name = attributes['kwname']
        if keyword_name in ['Open Website', 'Generate Random Email', 'Register User', 'Login User', 'View Product', 'Add To Cart', 'Checkout', 'Logout User', 'Close Website']:
            status = "PASS" if attributes['status'] == 'PASS' else "FAIL"
            print(f"{keyword_name} {status}")

def start_test(name, attributes):
    print(f"\n开始测试: {name}")

def end_test(name, attributes):
    status = "PASS" if attributes['status'] == 'PASS' else "FAIL"
    print(f"测试结束: {name} | {status}")

ROBOT_LISTENER_API_VERSION = 2