<template>
    <div>
        <el-row type="flex" justify="space-around" class="row-section">
            <el-col :span="22">
                <el-card>
                    <div slot="header" align="center">
                        <h3 class="title-tag">
                            <el-tag type="success">General Info</el-tag>
                        </h3>
                    </div>

                    <el-table :data="general" border>
                        <el-table-column prop="hostname" label="hostname" align="center"></el-table-column>
                        <el-table-column prop="os_name" label="os_name" align="center"></el-table-column>
                        <el-table-column prop="os_version" label="os_version" align="center"></el-table-column>
                        <el-table-column prop="server_time" label="server_time" align="center"></el-table-column>
                        <el-table-column prop="sys_up" label="sys_up" align="center"></el-table-column>
                    </el-table>
                </el-card>
            </el-col>
        </el-row>

        <el-row type="flex" justify="space-around" class="row-section">
            <el-col :span="22">
                <el-card>
                    <div slot="header" align="center">
                        <h3 class="title-tag">
                            <el-tag type="success">Cpu Info</el-tag>
                        </h3>
                    </div>

                    <el-table :data="cpu" border>
                        <el-table-column prop="architecture" label="architecture" align="center"></el-table-column>
                        <el-table-column prop="byte_order" label="byte-order" align="center"></el-table-column>
                        <el-table-column prop="cpu_mhz" label="cpu-mhz" align="center"></el-table-column>
                        <el-table-column prop="cpus" label="cpu count" align="center"></el-table-column>
                        <el-table-column prop="l1d_cache" label="l1d-cache" align="center"></el-table-column>
                        <el-table-column prop="l1i_cache" label="l1i-cache" align="center"></el-table-column>
                        <el-table-column prop="l2_cache" label="l2-cache" align="center"></el-table-column>
                    </el-table>
                </el-card>
            </el-col>
        </el-row>

        <el-row type="flex" justify="space-around" class="row-section">
            <el-col :span="22">
                <el-card >
                    <div slot="header" align="center">
                        <h3 class="title-tag">
                            <el-tag type="success">Net Info</el-tag>
                        </h3>
                    </div>
                    <el-table :data="net" border>
                        <el-table-column prop="interface" label="interface" align="center">
                        </el-table-column>
                        <el-table-column prop="address" label="address" align="center">
                        </el-table-column>
                        <el-table-column prop="netmask" label="netmask" align="center">
                        </el-table-column>
                    </el-table>
                </el-card>
            </el-col>
        </el-row>

        <el-row type="flex" justify="space-around" class="row-section">
            <el-col :span="22">
                <el-card >
                    <div slot="header" align="center" >
                        <h3 class="title-tag">
                            <el-tag type="success">Disk Info</el-tag>
                        </h3>
                    </div>
                    <el-table :data="disk" border style="width: 100%;">
                        <el-table-column prop="device" label="device" align="center">

                        </el-table-column>
                        <el-table-column prop="fstype" label="fstype" align="center">

                        </el-table-column>
                        <el-table-column prop="mountpoint" label="mount" align="center">

                        </el-table-column>
                        <el-table-column prop="total" label="total" align="center">

                        </el-table-column>
                        <el-table-column prop="used" label="used" align="center">

                        </el-table-column>
                        <el-table-column label="percent" align="center">

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
