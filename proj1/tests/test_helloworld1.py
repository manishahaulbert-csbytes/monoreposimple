import proj1.helloworld1 as hw

def test_helloworld1():
    assert hw.j1 == "hello world1"

def test_not_helloworld1():
    assert hw.j1 != "goodbye world"

def test_helloworld1_not_helloworld2():
    assert hw.j1 != "hello world2"

def test_helloworld1_not_helloworld2_not_helloworld3():
    assert hw.j1 != "hello world3"

def test_helloworld1_not_helloworld2_not_helloworld3_not_helloworld4():
    assert hw.j1 != "hello world4"
