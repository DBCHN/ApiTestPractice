# 对象
```
key:
  child-key:value
  child-key2:value2
```
等于

{"key"
   {"child-key":"calue",
    "child-key2":"value2"}
   }


# 数组
```
key:
  -A
  -B
  -C
```
等于{"key":[A,B,C]}

# 组合
```
key:
  -child-key:value
  child-key2:value2
```
等于
{"key"
   [{"child-key":"calue",
    "child-key2":"value2"}]
   }

# 数组嵌套
```
key:
  -
    -A
    -B
    -C
```
等于等于{"key":[[A,B,C]]}