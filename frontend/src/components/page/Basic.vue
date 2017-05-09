<template>
    <div>
        <el-row type="flex" justify="space-around" class="table-row">
            <el-col :span="22">
                <el-card>
                    <div slot="header" align="center">
                        <h3 class="title-tag">
                            <el-tag type="success">General Info</el-tag>
                        </h3>
                    </div>

                    <el-table :data="general" border>
                        <el-table-column prop="hostname" label="hostname"></el-table-column>
                        <el-table-column prop="os_name" label="os_name"></el-table-column>
                        <el-table-column prop="os_version" label="os_version"></el-table-column>
                        <el-table-column prop="server_time" label="server_time"></el-table-column>
                        <el-table-column prop="sys_up" label="sys_up"></el-table-column>
                    </el-table>
                </el-card>
            </el-col>
        </el-row>

        <el-row type="flex" justify="space-around" class="table-row">
            <el-col :span="22">
                <el-card>
                    <div slot="header" align="center">
                        <h3 class="title-tag">
                            <el-tag type="success">Cpu Info</el-tag>
                        </h3>
                    </div>

                    <el-table :data="cpu" border>
                        <el-table-column prop="architecture" label="architecture"></el-table-column>
                        <el-table-column prop="byte_order" label="byte-order"></el-table-column>
                        <el-table-column prop="cpu_mhz" label="cpu-mhz"></el-table-column>
                        <el-table-column prop="cpus" label="cpu count"></el-table-column>
                        <el-table-column prop="l1d_cache" label="l1d-cache"></el-table-column>
                        <el-table-column prop="l1i_cache" label="l1i-cache"></el-table-column>
                        <el-table-column prop="l2_cache" label="l2-cache"></el-table-column>
                    </el-table>
                </el-card>
            </el-col>
        </el-row>
        <el-row type="flex" justify="space-around" class="table-row">
            <el-col :span="22">
                <el-card >
                    <div slot="header" align="center">
                        <h3 class="title-tag">
                            <el-tag type="success">Net Info</el-tag>
                        </h3>
                    </div>
                    <el-table :data="net" border>
                        <el-table-column prop="interface" label="interface">
                        </el-table-column>
                        <el-table-column prop="address" label="address">
                        </el-table-column>
                        <el-table-column prop="netmask" label="netmask">
                        </el-table-column>
                    </el-table>
                </el-card>
            </el-col>
        </el-row>



        <el-row type="flex" justify="space-around" class="table-row">
            <el-col :span="22">
                <el-card >
                    <div slot="header" align="center">
                        <h3 class="title-tag">
                            <el-tag type="success">Disk Info</el-tag>
                        </h3>
                    </div>
                    <el-table :data="disk" border style="width: 100%;">
                        <el-table-column prop="device" label="device">

                        </el-table-column>
                        <el-table-column prop="fstype" label="fstype">

                        </el-table-column>
                        <el-table-column prop="mountpoint" label="mount">

                        </el-table-column>
                        <el-table-column prop="total" label="total">

                        </el-table-column>
                        <el-table-column prop="used" label="used">

                        </el-table-column>
                        <el-table-column label="percent">

                            <template scope="scope">
                                <el-progress :percentage="scope.row.percent" :text-inside="false" :stroke-width="18"></el-progress>
                            </template>

                        </el-table-column>
                    </el-table>
                </el-card>
            </el-col>

        </el-row>
    </div>
</template>

<style>
    .table-row{
        margin: 15px 2px;
    }

    .title-tag span.el-tag{
        font-size: 18px;
        font-weight: bold;
    }

    .el-card__header{
        padding: 10px 10px;
    }

</style>
<script>
    import KvPanel from '../common/KvPanel.vue';

    export default {
        components: {
          KvPanel
        },

        data: function(){
            return {
                disk: [],
                net: [],
                general: [],
                cpu: []
            }
        },

        methods: {

            getBasicInfo: function () {
                let _self = this;
                api.basic.get().then(function (response) {
                    let data = response.data.data;
                    _self.disk = data.disk;
                    _self.net = data.net;
                    _self.cpu = [data.cpu];
                    _self.general = [data.general];
                }, function (error) {

                });
            }
        },

        mounted: function () {
            this.getBasicInfo();
        }
    }
</script>
