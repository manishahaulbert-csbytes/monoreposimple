import proj2.helloworld2 as hw2

def test_helloworld2():
    print("Running test_helloworld2")
    print(f"Value of j2: {hw2.j2}")
    assert hw2.j2 != "hello world2"

def test_not_helloworld2():
    print("Running test_not_helloworld2")
    assert hw2.j2 != "goodbye world"
    print(f"Value of j2: {hw2.j2}")


def test_helloworld2_not_helloworld1():
    print("Running test_helloworld2_not_helloworld1")
    print(f"Value of j2: {hw2.j2}")
    print("This test should fail because j2 is not equal to 'hello world1'")
    assert hw2.j2 != "hello world1"