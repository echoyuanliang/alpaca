<template>
    <div>
        <el-row type="flex" justify="space-around" class="row-section">
            <el-col :span="22">
                <el-card>
                    <div type="slot" align="center">
                        <h3 class="title-tag">
                            <el-tag type="success">Basic Info</el-tag>
                        </h3>
                    </div>

                    <el-row type="flex" justify="space-around" class="table-row">
                        <el-table :data="basic_info" border maxHeight="600">
                            <el-table-column prop="pid" label="pid" align="center">
                            </el-table-column>
                            <el-table-column prop="name" label="name" align="center">
                            </el-table-column>
                            <el-table-column label="ppid" align="center">
                                <template scope="scope">
                                    <el-button type="text" size="small" :disabled="scope.row.ppid == '-'">
                                        <router-link :to="{name: 'process', params:{pid: scope.row.ppid}}" tag="span" v-if="scope.row.ppid != '-'">
                                            {{scope.row.ppid}}
                                        </router-link>
                                        <span v-else>-</span>
                                    </el-button>
                                </template>
                            </el-table-column>
                            <el-table-column prop="status" label="status" align="center">
                            </el-table-column>
                            <el-table-column prop="cwd" label="cwd" align="center">
                            </el-table-column>
                            <el-table-column prop="create_time" label="create_time" align="center">
                            </el-table-column>
                        </el-table>
                    </el-row>
                </el-card>
            </el-col>
        </el-row>
        <el-row class="row-section" type="flex" justify="space-around">
            <el-col :span="22">
                <el-card>
                    <el-row type="flex" justify="space-around">
                        <el-col :span="11">
                            <el-card>
                                <div slot="header" align="center">
                                    <h3 class="title-tag">
                                        <el-tag type="success">
                                            Mem Charts
                                        </el-tag>
                                    </h3>
                                </div>
                                <div class="charts" v-if="mem_charts.data.length">
                                    <bar-charts :values="mem_charts.data" :label="mem_charts.label"
                                                      :names="mem_charts.names" :title="mem_charts.title">
                                    </bar-charts>
                                </div>
                            </el-card>

                        </el-col>

                        <el-col :span="11">
                            <el-card>
                                <div slot="header" align="center">
                                    <h3 class="title-tag">
                                        <el-tag type="success">
                                            Threads
                                        </el-tag>
                                    </h3>
                                </div>
                                <el-row type="flex" justify="space-around">
                                    <el-table :data="threads" border :maxHeight="300">
                                        <el-table-column prop="id" label="id" align="center">
                                        </el-table-column>
                                        <el-table-column prop="system_time" label="system_time" align="center">
                                        </el-table-column>
                                        <el-table-column prop="user_time" label="user_time" align="center">
                                        </el-table-column>
                                    </el-table>
                                    <!--

                                    -->
                                </el-row>
                            </el-card>

                        </el-col>
                    </el-row>
                </el-card>
            </el-col>
        </el-row>
        <el-row class="row-section" type="flex" justify="space-around">
            <el-col :span="22">
                <el-card>
                    <el-row type="flex" justify="space-around">
                        <el-col :span="11">
                            <el-card>
                                <div slot="header" align="center">
                                    <h3 class="title-tag">
                                        <el-tag type="success">
                                            Percent Charts
                                        </el-tag>
                                    </h3>
                                </div>
                                <div class="charts" v-if="percent_charts.names.length">
                                    <time-line-charts :values="percent_charts.data" :label="percent_charts.label"
                                                      :names="percent_charts.names" :title="percent_charts.title">
                                    </time-line-charts>
                                </div>
                            </el-card>

                        </el-col>

                        <el-col :span="11">
                            <el-card>
                                <div slot="header" align="center">
                                    <h3 class="title-tag">
                                        <el-tag type="success">
                                            Cpu Time
                                        </el-tag>
                                    </h3>
                                </div>
                                <div class="charts" v-if="cpu_time.names.length">
                                    <time-line-charts :values="cpu_time.data" :names="cpu_time.names" :title="cpu_time.title">
                                    </time-line-charts>
                                </div>
                            </el-card>

                        </el-col>
                    </el-row>
                </el-card>
            </el-col>
        </el-row>
        <el-row class="row-section" type="flex" justify="space-around">
            <el-col :span="22">
                <el-card>
                    <div slot="header" align="center">
                        <h3 class="title-tag">
                            <el-tag type="success"> IO Counters</el-tag>
                        </h3>
                    </div>
                    <el-row type="flex" justify="space-around">
                        <el-col :span="11">
                            <div class="charts" v-if="io_chars.names.length">
                                <time-line-charts :values="io_chars.data"
                                                  :names="io_chars.names" :title="io_chars.title">
                                </time-line-charts>
                            </div>
                        </el-col>

                        <el-col :span="11">
                            <div class="charts" v-if="io_count.names.length">
                                <time-line-charts :values="io_count.data" :names="io_count.names" :title="io_count.title">
                                </time-line-charts>
                            </div>
                        </el-col>
                    </el-row>
                </el-card>
            </el-col>
        </el-row>
        <el-row class="row-section" type="flex" justify="space-around">
            <el-col :span="22">
                <el-card>
                    <div slot="header" align="center">
                        <h3 class="title-tag">
                            <el-tag type="success">Connections</el-tag>
                        </h3>
                    </div>
                    <el-row type="flex" justify="space-around" class="table-row">
                        <el-table :data="conns" border maxHeight="300">
                            <el-table-column prop="type" label="type" align="center">
                            </el-table-column>
                            <el-table-column prop="status" label="status" align="center">
                            </el-table-column>
                            <el-table-column prop="fd" label="fd" align="center">
                            </el-table-column>
                            <el-table-column prop="laddr" label="laddr" align="center">
                            </el-table-column>
                            <el-table-column prop="raddr" label="raddr" align="center">
                            </el-table-column>
                        </el-table>
                    </el-row>
                </el-card>
            </el-col>
        </el-row>
        <el-row class="row-section" type="flex" justify="space-around">
            <el-col :span="22">
                <el-card>
                    <div slot="header" align="center">
                        <h3 class="title-tag">
                            <el-tag type="success">Children</el-tag>
                        </h3>
                    </div>
                    <el-row type="flex" justify="space-around">
                        <el-table :data="children" border>
                            <el-table-column label="pid" align="center">
                                <template scope="scope">
                                    <el-button type="text" size="small" :disabled="scope.row.pid == '-'">
                                        <router-link :to="{name: 'process', params:{pid: scope.row.pid}}" tag="span" v-if="scope.row.pid != '-'">
                                            {{scope.row.pid}}
                                                    </router-link>
                                        <span v-else>-</span>
                                    </el-button>
                                </template>
                            </el-table-column>
                            <el-table-column prop="name" label="name" align="center">
                            </el-table-column>
                            <el-table-column prop="status" label="status" align="center">
                            </el-table-column>
                            <el-table-column prop="create_time" label="create_time" align="center">
                            </el-table-column>
                        </el-table>
                    </el-row>
                </el-card>
            </el-col>
        </el-row>
        <el-row class="row-section" type="flex" justify="space-around">
            <el-col :span="22">
                <el-card>
                    <div slot="header" align="center">
                        <h3 class="title-tag">
                            <el-tag type="success">Open Files</el-tag>
                        </h3>
                    </div>
                    <el-row type="flex" justify="space-around" class="table-row">
                        <el-table :data="open_files" border :maxHeight="300">
                            <el-table-column prop="fd" label="fd" align="center">
                            </el-table-column>
                            <el-table-column prop="mode" label="mode" align="center">
                            </el-table-column>
                            <el-table-column prop="path" label="path" align="center">
                            </el-table-column>
                        </el-table>
                    </el-row>
                </el-card>
            </el-col>
        </el-row>

    </div>
</template>

<script>
    import TimeLineCharts from '../common/TimeLineCharts.vue';
    import BarCharts from '../common/BarCharts.vue';

    export default {
        components: {
            'time-line-charts': TimeLineCharts,
            'bar-charts': BarCharts
        },

        data: function () {
            return {
                process_info: {},
                basic_info: [],
                mem_info: [],
                conns: [],
                io_counters: [null, null],
                cpus: [null, null],
                percent_charts: {
                    title: 'cpu/mem percent',
                    names: [],
                    label: {
                        formatter: '{value} %'
                    },

                    data: {
                        'cpu': [],
                        'mem': []
                    }
                },

                threads: [],
                open_files: [],
                cpu_time: {
                    title: 'cpu_time',
                    names: [],
                    data: {
                        'system': [],
                        'user': [],
                    }
                },

                io_chars: {
                    title: 'io chars',
                    names: [],
                    data: {
                        read: [],
                        write: []
                    }
                },

                io_count: {
                    title: 'io count',
                    names: [],
                    data: {
                        read: [],
                        write: []
                    }
                },

                mem_charts: {
                    title: 'mem usage',
                    label: {
                        formatter: '{value} M'
                    },
                    names: ['vms', 'text', 'data', 'rss', 'shared'],
                    data: []
                },

                children: [],

                tick: null
            };
        },

        methods: {
            getProcessInfo: function () {
                api.process.get({pid: this.$route.params.pid}).then(
                    (response)=>{
                        let process_info = response.data.data;
                        this.basic_info = [this.getBasicInfo(process_info)];
                        this.conns = process_info.connections;
                        this.children = process_info.children;
                        this.open_files = process_info.open_files;
                        this.threads = process_info.threads;
                        this.pushToPercentCharts(process_info);
                        this.pushToCpuTime(process_info['cpu_times']);
                        this.pushToIoCounters(process_info['io_counters']);
                        this.pushToMemCharts(process_info['memory_full_info']);

                    },(error)=>{
                    }
                );
            },

            subItem: function (left, right) {
                if(! (left && right)){
                    return null;
                }

                let res = {};
                for(let key in left){
                    res[key] = left[key] - right[key];
                }

                return res;
            },

            getCurCpu: function () {
                return this.subItem(this.cpus[0], this.cpus[1]);
            },

            saveCpuPoint: function (cpu) {
                this.cpus[1] = this.cpus[0];
                this.cpus[0] = cpu;
            },

            saveIo: function (io_counter) {
                this.io_counters[1] = this.io_counters[0];
                this.io_counters[0] = io_counter;
            },

            getCurIo: function () {
                return this.subItem(this.io_counters[0], this.io_counters[1]);
            },

            pushToMemCharts: function (mem) {
                let mem_charts = this.mem_charts;
                const M = (1024 * 1024).toFixed(2);
                mem_charts.data.length = 0;
                for(let key of mem_charts.names){
                    let mb = (mem[key] / M).toFixed(2);
                    mem_charts.data.push({name: key, value:mb});
                }
            },

            pushToCpuTime: function (cpu) {

                this.saveCpuPoint(cpu);
                let cur_cpu = this.getCurCpu();
                if(cur_cpu){
                    const now = new Date();
                    const timestamp = [now.getHours(), now.getMinutes() , now.getSeconds()].join(':');

                    let cpu_time = this.cpu_time;
                    cpu_time.data['system'].push(cur_cpu['system']);
                    cpu_time.data['user'].push(cur_cpu['user']);
                    cpu_time.names.push(timestamp);
                }
            },

            pushToIoCounters: function (io_counters) {
                this.saveIo(io_counters);
                let cur_io = this.getCurIo();

                if(cur_io){
                    const now = new Date();
                    const timestamp = [now.getHours(), now.getMinutes() , now.getSeconds()].join(':');

                    let io_chars = this.io_chars;
                    io_chars.data['read'].push(cur_io['read_chars']);
                    io_chars.data['write'].push(cur_io['write_chars']);
                    io_chars.names.push(timestamp);

                    let io_count = this.io_count;
                    io_count.data['read'].push(cur_io['read_count']);
                    io_count.data['write'].push(cur_io['write_count']);
                    io_count.names.push(timestamp);
                }
            },

            pushToPercentCharts: function (process) {
                const now = new Date();
                const timestamp = [now.getHours(), now.getMinutes() , now.getSeconds()].join(':');
                const cpu_percent = new Number(process['cpu_percent']);
                const mem_percent = new Number(process['memory_percent']);
                this.percent_charts.data['cpu'].push(cpu_percent.toFixed(2));
                this.percent_charts.data['mem'].push(mem_percent.toFixed(2));
                this.percent_charts.names.push(timestamp);
            },

            initAllCharts: function () {
                this.percent_charts.names = [];
                this.percent_charts.data['cpu'] = [];
                this.percent_charts.data['mem'] = [];

                this.io_chars.names = [];
                this.io_chars.data['read'] = [];
                this.io_chars.data['write'] = [];

                this.io_count.names = [];
                this.io_count.data['read'] = [];
                this.io_count.data['write'] = [];

                this.cpu_time.names = [];
                this.cpu_time.data['system'] = [];
                this.cpu_time.data['user'] = [];

                this.mem_charts.data = [];
                this.io_counters =  [null, null];
                this.cpus =  [null, null];
            },

            getBasicInfo: function (process_info) {
                return {
                    pid: process_info.pid,
                    name: process_info.name,
                    ppid: process_info.ppid,
                    cwd: process_info.cwd,
                    status: process_info.status,
                    create_time: process_info.create_time,
                };
            }
        },

        mounted: function () {
            this.$log.log('mounted');
            this.getProcessInfo();
            this.tick = setInterval(this.getProcessInfo, 1000);
        },

        watch: {
          '$route': function () {
              this.$log.log('changed');
              this.initAllCharts();
          }
        },

        destroyed: function () {
            if(this.tick){
                clearInterval(this.tick);
            }
        }
    }
</script>
