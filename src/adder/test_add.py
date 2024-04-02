from .add  import add

def test_basic_add():
    result  = add("1 2".split())
    
    assert result == 3
