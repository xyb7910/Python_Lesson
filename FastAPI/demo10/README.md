# ORM
初始学习Tortoise ORM
## 查询操作
以下都是类方法的使用。
### all
返回完整的数据，查询全部数据，返回一个`QuerySet`
### first
返回第一条数据，注意返回的为一个 `QuerySetSingle`
### get
获取制定信息的数据，并且返回结果为一个 `QuerySetSingle`
## 增加操作
### create
向数据库增加一条记录，并返回一个`object`
