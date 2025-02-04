from werkzeug.middleware.proxy_fix import ProxyFix
import os
from membership import app

if __name__ == "__main__":
    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )
    app.run()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Heroku's dynamic port
    app.run(host="0.0.0.0", port=port)
