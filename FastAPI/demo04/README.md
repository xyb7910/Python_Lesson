# 查询参数
声明的参数不是路径参数时，路径操作函数会把该参数自动解释为**查询参数**。

注意：在一个路径中，我们可以同时声明多个路径参数和请求参数

学会如何提供参数变量的属性限制，默认值的设定， 可选属性限定。

# 请求参数校验
- 使用 `Union[str, None] = None` 限制字段为可选，类型为str，或者是空， 默认值为空。
- 使用 fastapi 中的 `Query` 进行校验。

