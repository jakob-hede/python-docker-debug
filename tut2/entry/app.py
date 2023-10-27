from __future__ import annotations
import os
import sys
from pathlib import Path
import json


class App(object):
    def __init__(self) -> None:
        super().__init__()
        file = Path(__file__).absolute()
        self.entry_dir = file.parents[1]
        self.lode_dir = self.entry_dir / 'lode'
        self.conf_file = self.lode_dir / 'run.conf.json'
        self._conf_data = {}

    @property
    def conf_data(self):
        return self._conf_data

    def contemplate(self) -> bool:
        self.debug(f'contemplate')
        self.debug(f'entry_dir: {self.entry_dir}')
        # self.do_stuff()
        if not self.lode_dir.exists():
            self.debug(f'ABORT lode_dir NOT found: {self.lode_dir}')
            return False
        self.proceed()
        return True

    def proceed(self):
        self.debug(f'proceed')
        self._conf_data = self.read_conf()
        self.check_dobug()
        self.proceed_post_debugpyfy()

    def proceed_post_debugpyfy(self):
        self.debug(f'proceed_post_debugpyfy')
        # if str(entry_dir) in sys.path:
        #     sys.path.remove(str(entry_dir))
        py_source_dir = self.lode_dir / 'py'
        if str(py_source_dir) not in sys.path:
            self.debug(f'inserting {py_source_dir}/ into sys.path')
            sys.path.insert(0, str(py_source_dir))
        # sys_path = sys.path
        # object
        from pytut.entre import Entre  # noqa
        Entre.spawn(self)

    def read_conf(self):
        if self.conf_file.exists():
            txt = self.conf_file.read_text()
            conf_data = json.loads(txt)
            return conf_data
        return {}

    def check_dobug(self) -> bool:
        self.debug('check_dobug')
        dobug = self._conf_data.get('do_debug', 'nope').lower() == 'yes'
        if dobug:
            self.debug(f'dobug: {dobug}')
            habitat = os.environ.get('HABITAT', 'wateva').lower()
            is_habitat_container = 'container' in habitat
            self.debug(f'"{habitat}"  is_habitat_container: {is_habitat_container}')
            if not is_habitat_container:
                self.debug(f'Habitat is NOT a container, so NOT debugpyfying.')
                return False
            product_stage = os.environ.get('PRODUCT_STAGE', 'wateva').lower()
            is_product_stage_production = 'production' in product_stage
            self.debug(f'"{product_stage}"  is_product_stage_production: {is_product_stage_production}')
            if is_product_stage_production:
                self.debug(f'product_stage is *production*, so NOT debugpyfying.')
                return False
            self.debugpyfy()
            return True

    @staticmethod
    def debug(*args):
        # print in purple color
        print(f'\033[95m{" ".join(map(str, args))}\033[0m')

    def do_stuff(self):
        from stuffy import Stuffy
        stuffo = Stuffy.spawn(self)

    def debugpyfy(self):
        self.debug(f'debugpyfy')
        import debugpy
        debugpy.listen(("0.0.0.0", 5678))
        debugpy.wait_for_client()

    @classmethod
    def spawn(cls):
        # product_stage = os.environ.get('PRODUCT_STAGE', 'wateva').lower()
        # print(f'product_stage: "{product_stage}"')
        obj = cls()
        obj.contemplate()


if __name__ == '__main__':
    print(f'main BEGIN {__file__}')
    App.spawn()
    print('main DONE')
