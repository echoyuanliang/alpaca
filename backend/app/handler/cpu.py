import time
from threading import Thread, Lock
from copy import deepcopy
from app.lib.system import get_cpu_stat


class CpuHandler(Thread):
    def __init__(self, interval=60):
        Thread.__init__(self)
        self.cpu_stat = [{}, {}]
        self.lock = Lock()
        self.interval = interval

    def run(self):
        while True:
            cpu_stat = get_cpu_stat()
            self._set_stat_sync(cpu_stat)
            time.sleep(self.interval)

    def _set_stat(self, stat):
        self.cpu_stat[1] = self.cpu_stat[0]
        self.cpu_stat[0] = stat

    def _set_stat_sync(self, stat):
        with self.lock:
            self._set_stat(stat)

    @staticmethod
    def _sub_stat(left_stat, right_stat):
        total = float(left_stat['total'] - right_stat['total'])

        def compute_attr_percent(attr):
            return round((left_stat[attr] - right_stat[attr]) * 100 / total, 2)

        stat = {
            'total': round(total, 2),
            'nice': compute_attr_percent('nice'),
            'system': compute_attr_percent('system'),
            'user': compute_attr_percent('user'),
            'idle': compute_attr_percent('idle'),
            'iowait': compute_attr_percent('iowait'),
            'irq': compute_attr_percent('irq'),
            'steal': compute_attr_percent('steal'),
            'guest': compute_attr_percent('guest'),
            'soft_irq': compute_attr_percent('soft_irq')
        }

        return stat

    def _compute_last_stat(self, cpu_stat):
        now_stat, previous_stat = cpu_stat
        if not now_stat or not previous_stat:
            tmp_stat = get_cpu_stat()
            self._set_stat_sync(tmp_stat)
            return []

        stat = {}
        for key, val in now_stat.items():
            if key != 'cpus':
                stat[key] = val
            else:
                stat['cpus'] = []
                for cpu, item in now_stat['cpus'].items():
                    cur_cpu = self._sub_stat(item, previous_stat['cpus'][cpu])
                    cur_cpu['name'] = cpu
                    stat['cpus'].append(cur_cpu)
        return stat

    def get_last_stat(self):
        with self.lock:
            cpu_stat = deepcopy(self.cpu_stat)

        return self._compute_last_stat(cpu_stat)

cpu_handler = CpuHandler()
cpu_handler.start()

