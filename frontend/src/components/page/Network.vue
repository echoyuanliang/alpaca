<template>
    <div>
        <el-row type="flex" justify="space-around" class="row-section" v-for="(item, key) in iface_charts">
            <el-col :span="22">
                <section>
                    <el-row type="flex" justify="space-around">
                        <h3 class="title-tag">
                            <el-tag  type="success">{{key}} &nbsp; 网络流量</el-tag>
                        </h3>
                    </el-row>
                    <el-row type="flex" justify="space-around" class="row-section">
                        <el-col :span="11">
                            <div class="charts">
                                <time-line-charts :values="item.bytes_charts.data" :names="item.bytes_charts.names"
                                                  :title="item.bytes_charts.title"></time-line-charts>
                            </div>
                        </el-col>
                        <el-col :span="11">
                            <div class="charts">
                                <time-line-charts :values="item.packets_charts.data" :names="item.packets_charts.names"
                                                  :title="item.packets_charts.title"></time-line-charts>
                            </div>
                        </el-col>
                    </el-row>
                </section>
            </el-col>
        </el-row>

        <el-row type="flex" justify="space-around" class="row-section">
            <el-col :span="22">
                <section>
                    <el-row type="flex" justify="space-around">
                        <h3 class="title-tag">
                            <el-tag  type="success">连接状态</el-tag>
                        </h3>
                    </el-row>
                    <el-row type="flex" justify="space-around" class="row-section">
                        <el-col :span="11">
                            <div class="charts" v-if="conn_charts.tcp.values">
                                <pie-charts :values="conn_charts.tcp.values" :names="conn_charts.tcp.names"
                                                  :title="conn_charts.tcp.title"></pie-charts>
                            </div>
                        </el-col>
                        <el-col :span="11">
                            <div class="charts" v-if="conn_charts.tcp.values">
                                <pie-charts :values="conn_charts.udp.values" :names="conn_charts.udp.names"
                                            :title="conn_charts.udp.title"></pie-charts>
                            </div>
                        </el-col>
                    </el-row>
                </section>
            </el-col>
        </el-row>
        <el-row type="flex" justify="space-around" class="row-section">
            <el-col :span="22">
                <section v-if="connections.tcp">
                    <el-row type="flex" justify="space-around">
                        <el-tag type="success">TCP 连接详情 &nbsp; (共 {{connections.tcp.length}} 个连接)</el-tag>
                    </el-row>
                    <el-row type="flex" justify="space-around" class="table-row">
                        <el-table :data="connections.tcp" border>
                            <el-table-column label="pid" width="100" align="center">
                                <template scope="scope">
                                    <el-button type="text" size="small" :disabled="scope.row.pid == '-'">
                                        <router-link :to="{name: 'process', params:{pid: scope.row.pid}}" tag="span" v-if="scope.row.pid != '-'">
                                            {{scope.row.pid}}
                                        </router-link>
                                        <span v-else>-</span>
                                    </el-button>
                                </template>
                            </el-table-column>
                            <el-table-column prop="l_addr" label="l_addr" align="center">
                            </el-table-column>
                            <el-table-column prop="r_addr" label="r_addr" align="center">
                            </el-table-column>
                            <el-table-column prop="recv_q" label="recv_q" sortable width="150" align="center">
                            </el-table-column>
                            <el-table-column prop="send_q" label="send_q" sortable width="150" align="center">
                            </el-table-column>
                            <el-table-column prop="status" label="status" :filters="tcp_filters"
                                             :filter-method="filterStatus"
                                             filter-placement="bottom-end" width="180" align="center">
                            </el-table-column>
                        </el-table>
                    </el-row>
                </section>
            </el-col>
        </el-row>

        <el-row type="flex" justify="space-around" class="row-section">
            <el-col :span="22">
                <section v-if="connections.udp">
                    <el-row type="flex" justify="space-around">
                        <el-tag type="success">UDP连接详情 &nbsp; (共 {{connections.udp.length}} 个连接)</el-tag>
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
                            <el-table-column prop="recv_q" label="recv_q" sortable>
                            </el-table-column>
                            <el-table-column prop="send_q" label="send_q" sortable>
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

    div.charts{
        height: 300px;
        background-color: #EEF1F6;
        border: 2px solid #EEF1ea;
        -webkit-border-radius: 2px;
        -moz-border-radius: 2px;
        border-radius: 2px;
    }

    span.el-tag{
        font-size: 18px;
        font-weight: bold;
    }

</style>
<script>
    import TimeLineCharts from '../common/TimeLineCharts.vue';
    import PieCharts from '../common/PieCharts.vue';

    export default{
        components: {
            'time-line-charts': TimeLineCharts,
            'pie-charts': PieCharts
        },

        data: function () {
            return {
                tcp_filters: [
                    { text: 'CLOSE_WAIT', value: 'CLOSE_WAIT' },
                    { text: 'ESTABLISHED', value: 'ESTABLISHED' },
                    { text: 'LISTEN', value: 'LISTEN' },
                    { text: 'TIME_WAIT', value: 'TIME_WAIT'}
                ],
                connections: {},
                iface_charts: {},
                conn_charts: {
                    tcp: {
                        title: 'TCP连接状态'
                    },

                    udp: {
                        title: 'UDP连接状态'
                    }
                }
            };
        },

        methods: {
            initNetworkInfo: function() {
                api.network.get().then((response)=>{
                    try{
                        let net_info = response.data.data;
                        this.connections = net_info.connections;
                        let iface_status = net_info.iface_status;
                        this.initIfaceCharts(iface_status);
                        this.updateConnCharts(this.connections);
                    }catch(error){
                        this.$log.log(error);
                    }
                }, (error)=>{
                    this.$log.log(error);
                });
            },

            getNetworkInfo: function() {
                api.network.get().then((response)=>{
                    try{
                        let net_info = response.data.data;
                        this.connections = net_info.connections;
                        let iface_status = net_info.iface_status;
                        for(let item of iface_status){
                            this.pushDataToCharts(item);
                        }

                        this.updateConnCharts(this.connections);
                    }catch(error){
                        this.$log.log(error);
                    }
                }, (error)=>{
                    this.$log.log(error);
                });
            },

            filterStatus: function (value, row) {
                return row.status == value;
            },

            aggregateConns: function (conns) {
              let agg = {};
              let names = new Set();
              let values = [];

              for(let conn of conns){
                  if(names.has(conn.status)){
                      agg[conn.status] += 1;
                  }else{
                      agg[conn.status] = 1
                  }

                  names.add(conn.status);
              }

              for(let name of names.keys()){
                  values.push({
                      'name': name,
                      'value': agg[name]
                  });
              }

              return [Array.from(names), values];
            },

            updateConnCharts: function (connections) {
                let conn_charts = this.conn_charts;
                let [tcp_names, tcp_values] = this.aggregateConns(connections.tcp);
                let [udp_names, udp_values] = this.aggregateConns(connections.udp);
                conn_charts.tcp.names = tcp_names;
                conn_charts.tcp.values = tcp_values;
                conn_charts.udp.names = udp_names;
                conn_charts.udp.values = udp_values;
            },

            initIfaceCharts: function (iface_status) {

                for(let item of iface_status){

                    this.iface_charts[item['iface']] = {
                        bytes_charts: {
                            title: 'bytes',
                            names: [],
                            data: {
                                receive_bytes: [],
                                send_bytes: []
                            }
                        },

                        packets_charts: {
                            title: 'packets',
                            names: [],
                            data: {
                                receive_packets: [],
                                send_packets: []
                            }
                        }
                    };

                    this.pushDataToCharts(item);
                }
            },

            pushDataToCharts: function (data_point) {
                let charts = this.iface_charts[data_point['iface']];
                const now = new Date();
                const name = [now.getHours(), now.getMinutes() , now.getSeconds()].join(':');

                // bytes charts
                charts.bytes_charts.names.push(name);
                charts.bytes_charts.data.receive_bytes.push(data_point.receive_bytes);
                charts.bytes_charts.data.send_bytes.push(data_point.send_bytes);

                //packets charts
                charts.packets_charts.names.push(name);
                charts.packets_charts.data.receive_packets.push(data_point.receive_packets);
                charts.packets_charts.data.send_packets.push(data_point.send_packets);
            }
        },

        mounted: function () {
            this.initNetworkInfo();
            const interval = 10000; // 10s
            setInterval(this.getNetworkInfo, interval);
        }
    }
</script>
