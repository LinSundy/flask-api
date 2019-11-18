from utils.utils import RedPrint

api = RedPrint('author')


@api.route('/')
def index():
    return 'Get Author'
