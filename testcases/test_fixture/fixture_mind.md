## fixture夹具，`@pytest.fixture`

`(scop="function")`每一个函数或方法都会调用，需方法中加入参数才可生效，不加不生效

`(scop="class")`每一个类调用一次

`(scop="module")`每一个.py文件调用一次

`(scop="session")`是多个文件调用一次，.py文件就是module

fixture的作用范围：session>module>class>function