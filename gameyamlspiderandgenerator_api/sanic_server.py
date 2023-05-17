from sanic import Sanic, text ,BadRequest
from gameyamlspiderandgenerator import produce_yaml
from gameyamlspiderandgenerator.util.config import config
from gameyamlspiderandgenerator.util.plugin_manager import pkg
from loguru import logger
config.load("../config.yaml")
pkg.__init__()
app = Sanic(name='api')


@app.route('/')
async def tag_handler(request):
    if "url" not in request.args:
        raise BadRequest("Missing parameter URL")
    rzt = produce_yaml(request.args["url"][0])
    if rzt is None:
        raise BadRequest("URL Invalid")
    return text(str(rzt))
