from ..common import env

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": env.db("DATABASE_URL", "postgres://postgres@localhost:5432/django?conn_max_age=3600", "postgres")
}
