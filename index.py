from app.app import create_app
from flask_sqlalchemy import SQLAlchemy

app = create_app()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:devLGM123@39.100.101.91:3306/flask-api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 连接数据库
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    author = db.Column(db.Integer, nullable=False, default=1)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
