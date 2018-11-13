from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from objects.Location import Location
from objects.User import User
from db import db



class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


# setup an admin interface and provide the models.
def admin(app):
    from flask_admin import Admin
    admin = Admin(app, name='Admin', template_mode='bootstrap3')
    admin.add_view(AdminModelView(User, db.session))
    admin.add_view(AdminModelView(Location, db.session))
