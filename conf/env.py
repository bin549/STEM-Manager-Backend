import os


DATABASE_ENGINE = "django.db.backends.postgresql"
DATABASE_NAME =  "stem"
DATABASE_HOST = "47.106.92.143"
DATABASE_USER = "postgres"
DATABASE_PASSWORD = "__2018bb"
DATABASE_PORT = "5432"

# REDIS_PASSWORD = ''
# REDIS_HOST = '127.0.0.1'
# REDIS_URL = f'redis://:{REDIS_PASSWORD or ""}@{REDIS_HOST}:6380'
# ************** 其他 配置  ************** #
DEBUG = True
ALLOWED_HOSTS = ["*"]
LOGIN_NO_CAPTCHA_AUTH = True
  # 登录接口 /api/token/ 是否需要验证码认证，用于测试，正式环境建议取消
