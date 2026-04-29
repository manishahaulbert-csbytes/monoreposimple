import proj1.helloworld1 as hw

def test_helloworld1():
    assert hw.j1 == "hello world1"

def test_not_helloworld1():
    print("Running test_not_helloworld1")
    assert hw.j1 != "goodbye world"

def test_helloworld1_not_helloworld2():
    print("Running test_helloworld1_not_helloworld2")
    print(f"Value of j1: {hw.j1}")
    print("This test should fail because j1 is not equal to 'hello world2'")
    assert hw.j1 == "hello world2"

def test_helloworld1_not_helloworld2_not_helloworld3():
    print("Running test_helloworld1_not_helloworld2_not_helloworld3")
    assert hw.j1 == "hello world3"

def test_helloworld1_not_helloworld2_not_helloworld3_not_helloworld4():
    print("Running test_helloworld1_not_helloworld2_not_helloworld3_not_helloworld4")
    assert hw.j1 == "hello world4"

def test_helloworld1_not_helloworld2_not_helloworld3_not_helloworld4_not_helloworld5():
    print("Running test_helloworld1_not_helloworld2_not_helloworld3_not_helloworld4_not_helloworld5")
    print("This test should fail because j1 is not equal to 'hello world5'")
    print(f"Value of j1: {hw.j1}")
    assert hw.j1 == "hello world5"
