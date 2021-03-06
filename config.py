import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "db_repository")

MAX_SEARCH_RESULTS = 50

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

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


