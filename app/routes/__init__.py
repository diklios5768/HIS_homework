from .index import bp_idx
from .manager import bp_manager
from .user import bp_user


def init_app(app):
    app.register_blueprint(bp_idx)
    app.register_blueprint(bp_manager)
    app.register_blueprint(bp_user)
