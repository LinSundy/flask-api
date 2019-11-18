https://www.cnblogs.com/donghaoblogs/p/10389696.html

#  marshallow库的使用
`from flask_restful import fields, marshal_with`

https://flask-restful.readthedocs.io/en/latest/fields.html
```python
from flask_restful import Resource, fields, marshal_with

resource_fields = {
    'name': fields.String,
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='rfc822'),
}

class Todo(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self, **kwargs):
        return db_get_todo()  # Some function that queries the db
```

```python
class Todo(Resource):
    def get(self, **kwargs):
        return marshal(db_get_todo(), resource_fields), 200
```

@marshal_with
该 marshal_with()装饰将应用所描述的转变 resource_fields。从对象中提取的唯一字段是task。该 fields.Url字段是一个特殊字段，它采用端点名称并在响应中为该端点生成URL。您需要的许多字段类型已包含在内。

# reqparse
`from flask_restful import reqparse`
> Flask-Restful插件提供了类似WTForms来验证提交的数据是否合法的包，叫做reqparse。以下是基本用法：

```parser = reqparse.RequestParser()
parser.add_argument('username',type=str,help='请输入用户名')
args = parser.parse_args()
add_argument可以指定这个字段的名字，这个字段的数据类型等。以下将对这个方法的一些参数做详细讲解：

default：默认值，如果这个参数没有值，那么将使用这个参数指定的值。
required：是否必须。默认为False，如果设置为True，那么这个参数就必须提交上来。
type：这个参数的数据类型，如果指定，那么将使用指定的数据类型来强制转换提交上来的值。
choices：选项。提交上来的值只有满足这个选项中的值才符合验证通过，否则验证不通过。
help：错误信息。如果验证失败后，将会使用这个参数指定的值作为错误信息。
trim：是否要去掉前后的空格。
```
其中的type，可以使用python自带的一些数据类型，也可以使用flask_restful.inputs下的一些特定的数据类型来强制转换。比如一些常用的：

url：会判断这个参数的值是否是一个url，如果不是，那么就会抛出异常。
regex：正则表达式。
date：将这个字符串转换为datetime.date数据类型。如果转换不成功，则会抛出一个异常。