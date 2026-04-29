import proj2.helloworld2 as hw2

def test_helloworld2():
    assert hw2.j2 == "hello world2"

def test_not_helloworld2():
    print("Running test_not_helloworld2")
    assert hw2.j2 != "goodbye world"
    