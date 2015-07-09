import tornado.web


class TraceHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('tracer.html', port=self.application.settings.get('port'))
