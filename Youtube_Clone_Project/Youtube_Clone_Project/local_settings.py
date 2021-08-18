SECRET_KEY = 'django-insecure-l-0atdz^i+x(-&#u+^1$qf7#kmorh@ogzdw)y^dvnspo2c1jo7'


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'Youtube_Clone_Database',
        'USER': 'root',
        'PASSWORD': 'rabbit',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }

}  }
