os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class Msgrpc:
    def __init__(self, option=[]):
        self.host = option.get('host') or "127.0.0.1"
        self.port = option.get('port') or 55552
