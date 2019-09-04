from . import  auth


@auth.route('/login')
def login():
    return  'login'

@auth.route('/logout')
def logout():
    return  'logout'