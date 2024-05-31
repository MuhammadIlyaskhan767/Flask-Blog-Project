from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


# errorshandlers 404 errors response
@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404


# errorshandlers 403 errors response
@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403


# errorshandler 500 errors response
@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500