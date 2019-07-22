# todo-flask
简单的后台  todo-api
```
"""
/api/todo/all GET 
[
  {
    "id": 2,
    "todothing": "多喝热水",
    "time": "2017-10-12",
    "user_id": -1,
    "ct": 1539391977,
    "ut": 1539391977
  },
  {
    "id": 2,
    "todothing": "多喝热水",
    "time": "2017-10-12",
    "user_id": -1,
    "ct": 1539391977,
    "ut": 1539391977
  }
]

/api/todo/delete GET
请求:
{
    "id": 1
}
成功：
{
    "success": True,
    "message": "todo删除成功",
    "code": 200
}

/api/todo/add POST
请求:
{
    "todothing": "多喝热水",
    "time": "2017-10-12",
}
成功:
{
    "success": True,
    "message": "todo添加成功",
    "code": 200
}

/api/todo/update POST
请求:
{
    "id": 1,
    "todothing": "多喝热水",
    "time": "2017-10-12",
}
成功:
{
    "success": True,
    "message": "todo添加成功",
    "code": 200
}
"""
```