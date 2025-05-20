from hello import hello

def test_default():
    assert hello() =="hello, world"

def test_argument():
    assert hello("sai") =="hello, sai"    

def test_arg_loop():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"