from __future__ import annotations
from stuff.loggor import Loggor
from stuff.testor1 import Testor1


class Entre:
    singleton: Entre = None

    def __init__(self, app):
        self._app = app
        self.loggor = Loggor()

    @property
    def app(self):
        return self._app

    def enter(self):
        self.loggor.debug('enter')
        testor1 = Testor1()
        testor1.test1()
        testor1.test2()
        testor1.test3()

    @classmethod
    def spawn(cls, app):
        obj = cls(app)
        cls.singleton = obj
        obj.enter()
