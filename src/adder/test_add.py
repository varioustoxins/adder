from .add  import add

def test_basic_add():
    result  = add("1 2".split())
    
    assert result == 3

def test_null_add():
    result = add()
     
    assert result == 0
