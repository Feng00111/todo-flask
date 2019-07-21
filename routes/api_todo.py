from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    jsonify,
)
# 一次性引入多个 flask 里面的名字
# 注意最后一个后面也应该加上逗号
# 这样的好处是方便和一致性

from models.todo import TodoApi


# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字, 以后会有用(add函数里面就用到了)
# 第二个参数是套路
main = Blueprint('api', __name__)


@main.route('/all')
def index():
    # 查找所有的 todo 并返回
    todo_list = TodoApi.all()
    todos = [t.__dict__ for t in todo_list]
    return jsonify(todos)


@main.route('/add', methods=['POST'])
def add():
    form = request.json
    TodoApi.new(form)
    # t.save()
    # 蓝图中的 url_for 需要加上蓝图的名字，这里是 todo
    return jsonify({
        "success": True,
        "message": "todo添加成功",
        "code": 200
    })


@main.route('/delete/<int:todo_id>/')
def delete(todo_id):
    """
    <int:todo_id> 的方式可以匹配一个 int 类型
    int 指定了它的类型，省略的话参数中的 todo_id 就是 str 类型
    """
    # 通过 id 删除 todo
    TodoApi.delete(todo_id)
    # 引用蓝图内部的路由函数的时候，可以省略名字只用 .
    return jsonify({
        "success": True,
        "message": "todo删除成功",
        "code": 200
    })
