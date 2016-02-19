from app.core.helper import create_app
from app.core.db import db

# Development Config
config = 'config.dev'
# Production Config
# config = 'config.Prod'

app = create_app(config)
db.init_app(app)

# register blueprint
