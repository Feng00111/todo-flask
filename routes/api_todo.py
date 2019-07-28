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
import traceback

# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字, 以后会有用(add函数里面就用到了)
# 第二个参数是套路
main = Blueprint('api', __name__)


@main.route('/all')
def index():
    todo_list = TodoApi.all()
    todos = [t.__dict__ for t in todo_list]
    return jsonify(todos)


@main.route('/add', methods=['POST'])
def add():
    try:
        t = TodoApi.new(request.json)
    except Exception as e:
        traceback.print_exc()
        print(e)
        return jsonify({
            "success": False,
            "message": "todo添加失败",
            "code": 500
        })
    else:
        return jsonify({
            "success": True,
            "message": "todo添加成功",
            "code": 200
        })


@main.route('/update', methods=['POST'])
def update():
    try:
        todo_id = request.json.get("id")
        TodoApi.update(todo_id, request.json)
    except Exception as e:
        print(e)
        return jsonify({
            "success": False,
            "message": "todo更新失败",
            "code": 500
        })
    else:
        return jsonify({
            "success": True,
            "message": "todo更新成功",
            "code": 200
        })


@main.route('/delete')
def delete():
    """
    <int:todo_id> 的方式可以匹配一个 int 类型
    int 指定了它的类型，省略的话参数中的 todo_id 就是 str 类型
    """
    try:
        todo_id = request.args.get("id")
        TodoApi.delete(todo_id)
    except Exception as e:
        print(e)
        return jsonify({
            "success": False,
            "message": "todo删除失败",
            "code": 500
        })
    else:
        return jsonify({
            "success": True,
            "message": "todo删除成功",
            "code": 200
        })
