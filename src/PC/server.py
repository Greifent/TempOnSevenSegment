#!/usr/bin/python
import web
import PCLIB.temp
urls = (
    '/', 'index'
)

class index:        #this is called every time someone connects
    def GET(self):
        return int(PCLIB.temp.temp.getTemp())

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()