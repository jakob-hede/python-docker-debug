import os
import sys
from pathlib import Path


class Stuffy(object):
    def __init__(self, app) -> None:
        super().__init__()
        self.app = app
        self.debug(f'{__class__.__name__}.__init__')
        # file = Path(__file__).absolute()
        # self.entry_dir = file.parent

    @staticmethod
    def debug(*args):
        # print in cyan color
        print(f'\033[96m{" ".join(map(str, args))}\033[0m')

    def examine_environs(self):
        self.debug('examine_environs')
        env_file = self.app.entry_dir / '.env'
        txt = env_file.read_text()
        # self.debug(f'env_file: {env_file}')
        # self.debug(f'txt: {txt}')
        lines = txt.splitlines()
        for line in lines:
            # self.debug(f'line: {line}')
            if line.startswith('#'):
                continue
            if '=' not in line:
                continue
            key, val = line.split('=', 1)
            env_val = os.environ.get(key)
            self.debug(f' - {key}: "{val}" "{env_val}"')
            # os.environ[key] = val

    def write_run_conf(self):
        import json
        self.debug('write_run_conf')
        data = {
            'DO_DEBUG': 'yes',
        }
        file = self.app.entry_dir / 'run.conf.json'
        txt = json.dumps(data, indent=4)
        file.write_text(txt)

    @classmethod
    def spawn(cls, app):
        obj = cls(app)
        # obj.examine_environs()
        # obj.write_run_conf()
        return obj


##############


# def xmain():
#     print(f'main {__file__}')
#     file = Path(__file__).absolute()
#     entry_dir = file.parent
#     py_src_dir = entry_dir / 'lode'
#
#     verify_habitat(entry_dir, py_src_dir)
#
#     sub_main(py_src_dir)
#     print('main DONE')


# file = Path(__file__).absolute()
# entry_dir = file.parent
# py_src_dir = entry_dir / 'lode'
#
# verify_habitat(entry_dir, py_src_dir)
#
# sub_main(py_src_dir)
# print('main DONE')


def verify_habitat(entry_dir, py_src_dir):
    buggy_dir = Path('/opt/buggy')
    print_vars()
    dir_list = os.listdir(entry_dir)
    print(f'entry_dir: {entry_dir}')
    for dir_item in dir_list:
        print(f' - {dir_item}')
        # if dir_item.startswith('lode'):
        #     py_src_dir = entry_dir / dir_item
        #     # print(f'py_src_dir: {py_src_dir}')
        #     if str(py_src_dir) not in sys.path:
        #         sys.path.insert(0, str(py_src_dir))
    if py_src_dir.exists():
        print(f'py_src_dir: {py_src_dir}')
        dir_list = os.listdir(py_src_dir)
        for dir_item in dir_list:
            print(f' - {dir_item}')
    examine_dir(buggy_dir)


def examine_dir(dir_):
    print(f'examine_dir: {dir_}')
    if not isinstance(dir_, Path):
        dir_ = Path(dir_)
    if dir_.exists():
        dir_list = os.listdir(dir_)
        if dir_list:
            print(f'dir: {dir_}')
            for dir_item in dir_list:
                print(f' - {dir_item}')
        else:
            print(f' - dir is empty.')
    else:
        print(f' - dir does not exist.')


def print_var(var_name):
    print(f" - {var_name}: {os.environ.get(var_name, 'NADA')}")


def print_vars():
    print("print_vars")
    print_var("VAR1")
    print_var("VAR2")
    print_var("VAR3")
