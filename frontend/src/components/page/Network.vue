<template>
    <div>
        <el-row type="flex" justify="space-around" class="row-section">
            <el-col :span="22">
                <section>
                    <el-row type="flex" justify="space-around">
                        <el-tag>Network Basic Info</el-tag>
                    </el-row>
                    <el-row type="flex" justify="space-around" class="table-row">
                        <el-table :data="iface_status" border maxHeight="300">
                            <el-table-column prop="iface" label="iface">
                            </el-table-column>
                            <el-table-column prop="receive_bytes" label="receive_bytes">
                            </el-table-column>
                            <el-table-column prop="send_bytes" label="send_bytes">
                            </el-table-column>
                            <el-table-column prop="receive_packets" label="receive_packets">
                            </el-table-column>
                            <el-table-column prop="send_packets" label="send_packets">
                            </el-table-column>
                        </el-table>
                    </el-row>
                </section>
            </el-col>
        </el-row>

        <el-row type="flex" justify="space-around" class="row-section">
            <el-col :span="22">
                <section>
                    <el-row type="flex" justify="space-around">
                        <el-tag>TCP Connections</el-tag>
                    </el-row>
                    <el-row type="flex" justify="space-around" class="table-row">
                        <el-table :data="connections.tcp" border>
                            <el-table-column label="pid">
                                <template scope="scope">
                                    <el-tag type="success">
                                        <router-link :to="{name: 'process', params:{pid: scope.row.pid}}" tag="span">
                                            {{scope.row.pid}}
                                        </router-link>
                                    </el-tag>
                                </template>
                            </el-table-column>
                            <el-table-column prop="l_addr" label="l_addr">
                            </el-table-column>
                            <el-table-column prop="r_addr" label="r_addr">
                            </el-table-column>
                            <el-table-column prop="recv_q" label="recv_q">
                            </el-table-column>
                            <el-table-column prop="send_q" label="send_q">
                            </el-table-column>
                            <el-table-column prop="status" label="status">
                            </el-table-column>
                        </el-table>
                    </el-row>
                </section>
            </el-col>
        </el-row>

        <el-row type="flex" justify="space-around" class="table-row">
            <el-col :span="22">
                <section>
                    <el-row type="flex" justify="space-around">
                        <el-tag>UDP Connections</el-tag>
                    </el-row>
                    <el-row type="flex" justify="space-around" class="table-row">
                        <el-table :data="connections.udp" border>
                            <el-table-column prop="pid" label="pid" @click="$router.go('/process' + scope.row.pid)">
                                <template scope="scope">
                                    <el-tag type="success">{{scope.row.pid}}</el-tag>
                                </template>
                            </el-table-column>
                            <el-table-column prop="l_addr" label="l_addr">
                            </el-table-column>
                            <el-table-column prop="r_addr" label="r_addr">
                            </el-table-column>
                            <el-table-column prop="recv_q" label="recv_q">
                            </el-table-column>
                            <el-table-column prop="send_q" label="send_q">
                            </el-table-column>
                            <el-table-column prop="status" label="status">
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

    a{
        color: #000;
    }
</style>
<script>
    export default{
        data: function () {
            return {
                net_info: {},
                iface_status: [],
                connections: {}
            };
        },

        methods: {
            getNetworkInfo: function () {
                api.network.get().then((response)=>{
                    this.net_info = response.data.data;
                    //console.log(this.net_info);
                    this.iface_status = this.net_info.iface_status;
                    this.connections = this.net_info.connections;
                }, (error)=>{
                    // console.log(error);
                })
            }
        },

        mounted: function () {
            this.getNetworkInfo();
        }
    }
</script>
