import time
from threading import Thread, Lock
from copy import deepcopy
from app.lib import system


class SystemHandler(Thread):
    def __init__(self, interval=10):
        Thread.__init__(self)
        self.system_info = {}
        self.cpu_stat = [{}, {}]
        self.io_counters = [{}, {}]
        self.lock = Lock()
        self.interval = interval

    def run(self):
        while True:
            self._set_system()
            time.sleep(self.interval)

    def _set_system(self):
        from app.main import app
        with app.app_context():
            try:
                cpu_stat = system.get_cpu_stat()
                io_counters = system.get_io_counters()

                system_info = {
                    'loadavg': system.get_loadavg(),
                    'intensive_processes': system.get_intensive_processes(),
                    # 'pstree': system.get_pstree(),
                    'mem_info': system.get_mem_info()
                }

                with self.lock:
                    self._set_stat(cpu_stat)
                    self._set_io(io_counters)
                    system_info['cpu_stat'] = self._compute_last_stat(self.cpu_stat)
                    system_info['io_counters'] = self._compute_io_counters(self.io_counters)
                    self.system_info = system_info
            except Exception as e:
                app.logger.exception(str(e))

    def get_system(self):
        with self.lock:
            tmp_info = self.system_info

        return tmp_info

    def _set_stat(self, stat):
        self.cpu_stat[1] = self.cpu_stat[0]
        self.cpu_stat[0] = stat

    def _set_io(self, io):
        self.io_counters[1] = self.io_counters[0]
        self.io_counters[0] = io

    def _set_io_sync(self, io):
        with self.lock:
            self._set_io(io)

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

    @staticmethod
    def _sub_io(left_io, right_io):
        res = {}
        for key, value in left_io.items():
            res[key] = left_io[key] - right_io[key]

        res['avg_read_time'] = round(res['read_time'] / float(res['read_count']), 2) if res['read_count'] else 0
        res['avg_write_time'] = round(res['write_time'] / float(res['write_count']), 2) if res['write_count'] else 0
        res['avg_read_bytes'] = round(res['read_bytes'] / float(res['read_count']), 2) if res['read_count'] else 0
        res['avg_write_bytes'] = round(res['write_bytes'] / float(res['write_count']), 2) if res['write_count'] else 0
        return res

    def _compute_last_stat(self, cpu_stat):
        now_stat, previous_stat = cpu_stat
        if not now_stat or not previous_stat:
            return {}

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

    def _compute_io_counters(self, io_counters):
        now_io, previous_io = io_counters
        if not now_io or not previous_io:
            return {}

        return self._sub_io(now_io, previous_io)

    def get_last_io(self):
        with self.lock:
            io_counters = deepcopy(self.io_counters)

        return self._compute_last_stat(io_counters)

    def get_last_stat(self):
        with self.lock:
            cpu_stat = deepcopy(self.cpu_stat)

        return self._compute_last_stat(cpu_stat)


system_handler = SystemHandler()
system_handler.start()
