<template>
    <div>
        <el-row type="flex" justify="space-around" class="row-section" v-for="(item, key) in iface_charts">
            <el-col :span="22">
                <el-card>
                    <div slot="header" align="center">
                        <h3 class="title-tag">
                            <el-tag  type="success">{{key}} &nbsp; Traffic</el-tag>
                        </h3>
                    </div>
                    <el-row type="flex" justify="space-around">
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
                </el-card>
            </el-col>
        </el-row>

        <el-row type="flex" justify="space-around" class="row-section">
            <el-col :span="22">
                <el-card>
                    <div slot="header" align="center">
                        <h3 class="title-tag">
                            <el-tag  type="success">Connection Status</el-tag>
                        </h3>
                    </div>
                    <el-row type="flex" justify="space-around">
                        <el-col :span="11">
                            <div class="charts" v-if="conn_charts.values.length">
                                <pie-charts :values="conn_charts.values" :names="conn_charts.names"
                                                  :title="conn_charts.title"></pie-charts>
                            </div>
                        </el-col>
                        <el-col :span="11">
                            <div class="charts" v-if="status_charts.names.length">
                                <time-line-charts :values="status_charts.data" :names="status_charts.names"
                                                  :title="status_charts.title"></time-line-charts>
                            </div>
                        </el-col>
                    </el-row>
                </el-card>
            </el-col>
        </el-row>
        <el-row type="flex" justify="space-around" class="row-section">
            <el-col :span="22">
                <el-card v-if="connections.conns">
                    <div slot="header" align="center">
                        <h3 class="title-tag">
                            <el-tag type="success">TCP Connection Details &nbsp; ( {{connections.count}} connections)</el-tag>
                        </h3>
                    </div>
                    <el-row type="flex" justify="space-around">
                        <el-table :data="connections.conns" border>
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
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import config from '../../config.js';
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
                tick: null,
                connections: {},
                iface_charts: {},
                conn_charts: {
                    title: '',
                    names: [],
                    values: []
                },
                status_charts: {
                    title: '',
                    names: [],
                    data: {
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
                        this.$log.log(this.connections);
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
                let [names, values] = this.aggregateConns(connections.conns);
                //Object.assign(conn_charts.names, names);
                //Object.assign(conn_charts.values, values);
                conn_charts.names.length = 0;
                for(let name of names){
                    conn_charts.names.push(name);
                }
                conn_charts.values.length = 0;
                for(let value of values){
                    conn_charts.values.push(value);
                }

                const now = new Date();
                const name = [now.getHours(), now.getMinutes() , now.getSeconds()].join(':');
                let status_charts = this.status_charts;
                for(let item of values){
                    if(status_charts.data[item.name]){
                        status_charts.data[item.name].push(item.value);
                    }else {
                        status_charts.data[item.name] = [item.value];
                    }
                }
                status_charts.names.push(name);
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
            this.tick = setInterval(this.getNetworkInfo, config.NET_IDLE);
        },

        destroyed: function () {
            if(this.tick){
                clearInterval(this.tick);
            }
        }
    }
</script>
