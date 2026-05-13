import proj3.helloworld3 as hw

def test_helloworld3():
    assert hw.j3 == "hello world3"

def test_not_helloworld3():
    assert hw.j3 != "goodbye world"

def test_helloworld3_not_helloworld1():
    assert hw.j3 != "hello world1"

def test_helloworld3_not_helloworld2():
    assert hw.j3 != "hello world2"
