# setup/teardown

模块级 —— setup_medule/teardown_medule 开始于模块始末，生效一次

函数级 —— setup_function/teardown_function 对每条函数用例生效（不在类中）

类级 —— setup_class/teardown_class 只能在类中前后运行一次（在类中）

方法级 —— setup_method/teardown_method 开始于方法始末（在类中）