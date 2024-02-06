# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path
from flask import Flask, jsonify, render_template
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from config import config

# set sys path
# root = Path(__file__).absolute().parent.parent
# sys.path.extend([os.path.join(root, '.'), os.path.join(root, 'recommend')])

# start flask app
app = Flask(__name__)
app.config.from_mapping(
    JSON_AS_ASCII=False,  # 解决中文乱码问题
)


def register_api():
    # set up rest api
    from handler import apis as apis_handler
    from algorithm import apis as apis_algorithm
    apis = apis_handler + apis_algorithm
    for api in apis:
        app.register_blueprint(api)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/platformInfo')
def platform_info():
    """
    平台系统信息
    ---
    tags:
    - 平台系统信息
    """
    import platform
    system_type = platform.system()
    python_version = platform.python_version()
    sys_arch = platform.architecture()
    return jsonify({
        '系统类型': system_type,
        '系统位数': sys_arch,
        'Python版本': python_version,
        'app name': app.name
    })


@app.route('/swagger')
def swagger_index():
    return render_template("swagger/index.html", **{
        "url": "/spec"
    })


@app.route('/spec')
def spec():
    swag = swagger(app)
    swag['info']['title'] = 'Recommend System API'
    swag['info']['version'] = '1.0'
    return jsonify(swag)


SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/spec'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)
register_api()
if __name__ == "__main__":
    """
    Flask-Swagger 示例.
    """

    # start application
    app.run(debug=config.DEBUG,
            host=config.IP_ADDRESS,
            port=config.PORT,
            threaded=True
            )
