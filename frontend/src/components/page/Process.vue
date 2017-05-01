<template>
    <div>
        <el-row type="flex" justify="space-around" class="row-section">
            <el-col :span="11">
                <section>
                    <el-row type="flex" justify="space-around">
                        <el-tag>Basic Info</el-tag>
                    </el-row>
                    <el-row type="flex" justify="space-around" class="table-row">
                        <el-table :data="basic_info" border maxHeight="600">
                            <el-table-column prop="k" label="k">

                            </el-table-column>
                            <el-table-column prop="v" label="v">

                            </el-table-column>
                        </el-table>
                    </el-row>
                </section>
            </el-col>

            <el-col :span="11">
                <section>
                    <el-row type="flex" justify="space-around">
                        <el-tag>Mem Info</el-tag>
                    </el-row>
                    <el-row type="flex" justify="space-around" class="table-row">
                        <el-table :data="mem_info" border maxHeight="600">
                            <el-table-column prop="k" label="k">
                            </el-table-column>
                            <el-table-column prop="v" label="v">
                            </el-table-column>
                        </el-table>
                    </el-row>
                </section>
            </el-col>

        </el-row>

        <el-row class="row-section">
            <el-col :span="22">
                <el-row type="flex" justify="space-around">
                    <el-tag>Cpu Info</el-tag>
                </el-row>
                <el-row type="flex" justify="space-around">
                    <el-table :data="cpu_info" border maxHeight="300">
                        <el-table-column prop="cpu_id" label="cpu_id">
                        </el-table-column>
                        <el-table-column prop="cpu_percent" label="cpu_percent">
                        </el-table-column>
                        <el-table-column prop="system" label="system_time">
                        </el-table-column>
                        <el-table-column prop="user" label="user_time">
                        </el-table-column>
                        <el-table-column prop="children_system" label="children_system">
                        </el-table-column>
                        <el-table-column prop="children_user" label="children_user">
                        </el-table-column>
                    </el-table>
                </el-row>
            </el-col>
        </el-row>
        <el-row class="row-section">
            <el-col :span="22">
                <section>
                    <el-row type="flex" justify="space-around">
                        <el-tag>Connections</el-tag>
                    </el-row>
                    <el-row type="flex" justify="space-around" class="table-row">
                        <el-table :data="conns" border maxHeight="300">
                            <el-table-column prop="type" label="type">
                            </el-table-column>
                            <el-table-column prop="status" label="status">
                            </el-table-column>
                            <el-table-column prop="fd" label="fd">
                            </el-table-column>
                            <el-table-column prop="laddr" label="laddr">
                            </el-table-column>
                            <el-table-column prop="raddr" label="raddr">
                            </el-table-column>
                        </el-table>
                    </el-row>
                </section>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="22">
                <section>
                    <el-row type="flex" justify="space-around">
                        <el-tag>IO Counters</el-tag>
                    </el-row>
                    <el-row type="flex" justify="space-around" class="table-row">
                        <el-table :data="io_counters" border maxHeight="300">
                            <el-table-column prop="read_bytes" label="read_bytes">
                            </el-table-column>
                            <el-table-column prop="read_count" label="read_count">
                            </el-table-column>
                            <el-table-column prop="write_bytes" label="write_bytes">
                            </el-table-column>
                            <el-table-column prop="write_count" label="write_count">
                            </el-table-column>
                        </el-table>
                    </el-row>
                </section>
            </el-col>
        </el-row>
        <el-row class="row-section">
                <el-col :span="11">
                    <section>
                        <el-row type="flex" justify="space-around">
                            <el-tag>Children</el-tag>
                        </el-row>
                        <el-row type="flex" justify="space-around" class="table-row">
                            <el-table :data="process_info.children" border maxHeight="300">
                                <el-table-column prop="pid" label="pid">
                                </el-table-column>
                                <el-table-column prop="name" label="name">
                                </el-table-column>
                            </el-table>
                        </el-row>
                    </section>
                </el-col>
        </el-row>
    </div>
</template>

<style>
    .row-section{
        margin: 15px 2px;
    }
</style>
<script>
    export default {
        data: function () {
            return {
                process_info: {},
                basic_info: [],
                mem_info: [],
                conns: [],
                cpu_info: [],
                io_counters: []
            };
        },

        methods: {
            getProcessInfo: function () {
                api.process.get({pid: this.$route.params.pid}).then(
                    (response)=>{
                        this.process_info = response.data.data;
                        this.basic_info = this.computeBasicInfo();
                        this.conns = this.process_info.connections;
                        this.cpu_info = this.computeCpuInfo();
                        this.io_counters = [this.process_info.io_counters];
                        this.mem_info = this.computeMemInfo();
                        console.log(this.process_info);
                        // console.log(this.io_counters);
                    },(error)=>{
                        console.error(error);
                    }
                )
            },

            computeBasicInfo: function () {
                let process = this.process_info;
                let basic_list = ['pid', 'name', 'status', 'create_time', 'nice',
                    'exe', 'num_fds', 'num_threads', 'cwd', 'cmdline'];
                let basic = [];
                basic['parent'] = process['parent']['pid'] + '-' + process['parent']['name'];
                for(let k of basic_list){
                    basic.push({
                        'k': k,
                        'v': process[k]
                    });
                }
                return basic;
            },

            computeMemInfo: function () {
                let process = this.process_info;
                let full_info = process.memory_full_info;
                let mem_info = [{'k': 'percent', 'v': process.memory_percent}];

                for(let k in full_info){
                    if(full_info.hasOwnProperty(k)){
                        mem_info.push({
                            'k': k,
                            'v': full_info[k]
                        });
                    }
                }
                return mem_info;
            },

            computeCpuInfo: function () {
                let process = this.process_info;
                let cpu_times = process.cpu_times;
                return [{
                    'cpu_id': process.cpu_num,
                    'cpu_percent': process.cpu_percent,
                    'system': cpu_times.system,
                    'user': cpu_times.user,
                    'children_user': cpu_times.children_user,
                    'children_system': cpu_times.children_system
                }]
            }
        },

        mounted: function () {
            this.getProcessInfo();
        }
    }
</script>
