from src.load_env_vars import *

db_url = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_PATH}:{DB_PORT}/{DB_NAME}"
