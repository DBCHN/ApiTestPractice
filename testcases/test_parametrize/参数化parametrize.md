# 参数化（parametrize)
参数化可以组装测试数据，在测试前定义好测试数据，并在测试用例中使用

## 单次循环
```
@pytest.mark.parametrize("a",["b"])
def test_parametrize(a):
    print(a)
```

## 多次循环
```
@pytest.mark.parametrize("a,b",[("c","d"),("e","f")])
def test_parametrize(a,b):
    print(a,b)
```

