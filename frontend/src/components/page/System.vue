<template>
    <div>
        <el-row type="flex" justify="space-around" class="row-section">
            <el-col :span="11">
                <section>
                    <el-row type="flex" justify="space-around">
                        <el-tag>Cpu Intensive Processes</el-tag>
                    </el-row>
                    <el-row type="flex" justify="space-around" class="table-row">
                        <el-table :data="cpu_intensive" border maxHeight="300">
                            <el-table-column prop="pid" label="pid">
                            </el-table-column>
                            <el-table-column label="name">
                                <template scope="scope">
                                    <el-popover trigger="hover" placement="top">
                                        <p>create_time: {{ scope.row.create_time }}</p>
                                        <p>username: {{ scope.row.username }}</p>
                                        <p>status: {{ scope.row.status }}</p>
                                        <p>mem_percent: {{ scope.row.memory_percent }}</p>
                                        <div slot="reference" class="name-wrapper">
                                            <el-tag>{{ scope.row.name }}</el-tag>
                                        </div>
                                    </el-popover>
                                </template>
                            </el-table-column>
                            <el-table-column prop="cpu_percent" label="cpu_percent">
                            </el-table-column>
                        </el-table>
                    </el-row>
                </section>
            </el-col>

            <el-col :span="11">
                <section>
                    <el-row type="flex" justify="space-around">
                        <el-tag>Memory Intensive Processes</el-tag>
                    </el-row>
                    <el-row type="flex" justify="space-around">
                        <el-table :data="mem_intensive" border maxHeight="300">
                            <el-table-column prop="pid" label="pid">
                            </el-table-column>
                            <el-table-column label="name">
                                <template scope="scope">
                                    <el-popover trigger="hover" placement="top">
                                        <p>create_time: {{ scope.row.create_time }}</p>
                                        <p>username: {{ scope.row.username }}</p>
                                        <p>status: {{ scope.row.status }}</p>
                                        <p>cpu_percent: {{ scope.row.cpu_percent }}</p>
                                        <div slot="reference" class="name-wrapper">
                                            <el-tag>{{ scope.row.name }}</el-tag>
                                        </div>
                                    </el-popover>
                                </template>
                            </el-table-column>
                            <el-table-column prop="memory_percent" label="mem_percent">
                            </el-table-column>
                        </el-table>
                    </el-row>
                </section>
            </el-col>
        </el-row>

         <el-row type="flex" justify="space-around" class="row-section">
            <el-col :span="11">
                <section>
                    <el-row type="flex" justify="space-around">
                        <el-tag>Load Average</el-tag>
                    </el-row>
                    <el-row type="flex" justify="space-around" class="table-row">
                        <el-table :data="loadavg" border maxHeight="300">
                            <el-table-column prop="1min" label="1min"></el-table-column>
                            <el-table-column prop="3min" label="3min"></el-table-column>
                            <el-table-column prop="5min" label="5min"></el-table-column>
                        </el-table>
                    </el-row>
                </section>
            </el-col>

            <el-col :span="11">
                <section>
                    <el-row type="flex" justify="space-around">
                        <el-tag>Process Tree</el-tag>
                    </el-row>
                    <el-row>
                        <el-tree
                            :data="pstree"
                            :props="pstree_props"
                            accordion>
                        </el-tree>
                    </el-row>
                </section>
            </el-col>
        </el-row>

        <el-row type="flex" justify="space-around" class="row-section">
            <el-col :span="23">
                <section>
                    <el-row type="flex" justify="space-around">
                        <el-tag>Cpu Usage</el-tag>
                    </el-row>
                    <el-row type="flex" justify="space-around" class="table-row">
                        <el-table :data="cpustat.cpus" border maxHeight="300">
                            <el-table-column prop="name" label="name"></el-table-column>
                            <el-table-column prop="total" label="total"></el-table-column>
                            <el-table-column prop="system" label="system"></el-table-column>
                            <el-table-column prop="user" label="user"></el-table-column>
                            <el-table-column prop="idle" label="idle"></el-table-column>
                            <el-table-column prop="nice" label="nice"></el-table-column>
                            <el-table-column prop="iowait" label="iowait"></el-table-column>
                            <el-table-column prop="steal" label="steal"></el-table-column>
                            <el-table-column prop="irq" label="irq"></el-table-column>
                            <el-table-column prop="soft_irq" label="soft_irq"></el-table-column>
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
                sys_info: {},
                mem_intensive: [],
                cpu_intensive: [],
                loadavg: [],
                pstree: [],
                cpustat: {},
                pstree_props: {
                    label: 'process',
                    children: 'children'
                }
            }
        },

        methods: {
            getSystemInfo: function () {
                api.system.get().then((response) => {
                    let _self = this;
                    _self.sys_info = response.data.data;
                    _self.cpu_intensive = _self.sys_info.intensive_processes.cpu_intensive;
                    _self.mem_intensive = _self.sys_info.intensive_processes.mem_intensive;
                    _self.loadavg.push(_self.sys_info.loadavg);
                    _self.pstree = _self.sys_info.pstree;
                    _self.cpustat = _self.sys_info.cpu_stat;
                    //console.log(_self.sys_info);
                }, (error) => {
                    //console.log(error);
                });
            }
        },

        mounted: function () {
            this.getSystemInfo();
        }

    }
</script>
