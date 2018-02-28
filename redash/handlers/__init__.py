from flask import jsonify
from flask_login import login_required

from redash.handlers.api import api
from redash.handlers.base import routes
from redash.monitor import get_status
from redash.permissions import require_super_admin


@routes.route('/ping', methods=['GET'])
def ping():
    # 这是一个测试URL
    return 'PONG.'


@routes.route('/status.json')
@login_required
@require_super_admin
def status_api():
    # 获取redashde的运行状态
    status = get_status()
    return jsonify(status)


def init_app(app):
    from redash.handlers import embed, queries, static, authentication, admin, setup
    app.register_blueprint(routes)
    # 注册路由的蓝本
    api.init_app(app)
