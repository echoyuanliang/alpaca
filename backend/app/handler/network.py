import time
from threading import Thread, Lock
from copy import deepcopy
from app.lib.network import get_iface_status, get_connections


class NetHandler(Thread):

    def __init__(self, interval=10):
        Thread.__init__(self)
        self.net_cache = [{}, {}]
        self.connections = {}
        self.lock = Lock()
        self.interval = interval

    def run(self):
        from app.main import app

        while True:
            with app.app_context():
                try:
                    net = get_iface_status()
                    self._set_net_async(net)
                    self._set_connections()
                    time.sleep(self.interval)
                except Exception as e:
                    app.logger.exception(str(e))

    def _set_net(self, net):
        self.net_cache[1] = self.net_cache[0]
        self.net_cache[0] = net

    def _set_net_async(self, net):
        with self.lock:
            self._set_net(net)

    def _set_connections(self):
        connections = get_connections()
        with self.lock:
            self.connections = connections

    @staticmethod
    def _sub_iface_status(left_iface, right_iface):
        res = {}
        for key, value in left_iface.items():
            res[key] = left_iface[key] - right_iface[key]

        return res

    def _compute_sub(self, iface_status):
        now_status, previous_status = iface_status
        if not now_status or not previous_status:
            tmp_status = get_iface_status()
            self._set_net_async(tmp_status)
            return []

        iface_list = []
        for iface, cur_status in now_status.items():
            prev_status = previous_status[iface]
            res_status = self._sub_iface_status(cur_status, prev_status)
            res_status['iface'] = iface
            iface_list.append(res_status)

        return iface_list

    def get_iface_status(self):
        with self.lock:
            iface_status = deepcopy(self.net_cache)

        return self._compute_sub(iface_status)

    def get_connections(self):
        with self.lock:
            connections = deepcopy(self.connections)
        return connections

    def get_network_info(self):
        with self.lock:
            iface_status = deepcopy(self.net_cache)
            connections = deepcopy(self.connections)

        return {
            'connections': connections,
            'iface_status': self._compute_sub(iface_status)
        }

net_handler = NetHandler()
net_handler.start()
