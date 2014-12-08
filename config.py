import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "db_repository")

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '1578641885698624',
        'secret': '7568929e0d956a654c92fa23b9ed277f'
    },
    'twitter': {
        'id': 'AipExyBDMu3NoejXmPw32iKDU',
        'secret': 'eiIT5CtHCSle0I9IupORzLlIU7uNf81thkWKYznBUBKHY01rWF'
    },
    'vkontakte': {
        'id': '4661519',
        'secret': 'QcPeNSfyzb2iqp5qv6KG'
    },
    'google': {
            'id' : '995429479325-brvpv6fmp16kismlj5el5krjia6cp7va.apps.googleusercontent.com',
            'secret': 'NjcPpYnyVODZ9tS8ozxV_bUz'
    }
}


