import proj1.helloworld1 as hw

def test_helloworld1():
    assert hw.j1 == "hello world1"

def test_not_helloworld1():
    assert hw.j1 != "goodbye world"

def test_helloworld1_not_helloworld2():
    assert hw.j1 != "hello world2"
