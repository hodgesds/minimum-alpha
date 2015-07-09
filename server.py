import os
import argparse
from   tornado.ioloop import IOLoop
from   tornado.web import RequestHandler, Application, url
from   handlers import WsHandler, TraceHandler


def run_server(args):
    ioloop = IOLoop.current()
    path   = os.path.dirname(os.path.realpath(__file__))
    settings = {
        'template_path': path + os.sep + 'templates',
        'port': args.port,
    }
    app = Application([
        url(r"/ws", WsHandler),
        url(r"/", TraceHandler),
        ],
        **settings
    )
    app.listen(args.port)
    app.clients = {}
    ioloop.start()

def main():
    parser = argparse.ArgumentParser(description='Less is less')
    parser.add_argument(
        '-p', '--port',
        dest    = 'port',
        type    = int,
        default = 8888,
    )
    parser.set_defaults(func=run_server)
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
