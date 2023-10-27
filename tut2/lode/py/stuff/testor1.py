import os
import pwd

from stuff.loggor import Loggor


class Testor1:
    def __init__(self):
        self.loggor = Loggor()

    @staticmethod
    def read_env(key, default=None):
        value = os.environ.get(key, default)
        # self.loggor.debug(f'{key}: {value}')
        return value

    def test1(self):
        host_name = 'unknown'
        ip_address = 'unknown'
        user_id = 'unknown'
        user_name = 'unknown'

        user_id = os.getuid()
        user_name = pwd.getpwuid(user_id).pw_name

        self.loggor.debug(f'user id: {user_id}')
        self.loggor.debug(f'user name: {user_name}')

        try:
            import socket
        except ModuleNotFoundError as e:
            raise e

        try:
            host_name = socket.gethostname()
        except Exception as e:
            print(e)

        try:
            ip_address = socket.gethostbyname(host_name)
        except Exception as e:
            print(e)

        self.loggor.debug(f'hostname: {host_name}')
        self.loggor.debug(f'ip address: {ip_address}')

    def test2(self):
        self.loggor.debug('test2')
        app_dir = os.environ.get('APP_DIR', None)
        self.loggor.debug(f'app_dir: {app_dir}')

    def test3(self):
        self.loggor.debug('test3')
        # from docker_python.tut2.entry.app import App
        from pytut.entre import Entre
        entre = Entre.singleton
        product_stage = self.read_env('PRODUCT_STAGE', 'nada')
        self.loggor.debug(f'product_stage: {product_stage}')

#
