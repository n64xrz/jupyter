import os

c = globals().get('c', None)  # type: ignore
c.ServerApp.ip = '0.0.0.0'
c.ServerApp.notebook_dir = f'{os.getenv("HOME")}/src'
c.ServerApp.open_browser = False
c.ServerApp.allow_root = True
c.ServerApp.port = os.getenv("PORT_JUPYTER", '9000')
c.ServerApp.token = ''
c.ServerApp.password = ''
c.ServerApp.allow_origin = '*'
c.ServerApp.allow_remote_access = True
c.ServerApp.authenticate_prometheus = False
c.ServerApp.base_url = os.getenv("NB_PREFIX", '/')
