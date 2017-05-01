<template>
    <div>
        <el-row type="flex" justify="space-around" class="table-row">
            <kv-panel :span="5" :data="general" header="General Info.">
            </kv-panel>
            <kv-panel :span="5" :data="mem" header="Memory Info.">
            </kv-panel>
            <kv-panel :span="5" :data="cpu" header="Cpu Info.">
            </kv-panel>
            <kv-panel :span="5" :data="swap" header="Swap Info.">
            </kv-panel>
        </el-row>
        <el-row type="flex" justify="space-around" class="table-row">
            <el-col :span="20">
                <el-card >
                    <div slot="header" align="center">
                        <el-tag>Net Info</el-tag>
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
            <el-col :span="20">
                <el-card >
                    <div slot="header" align="center">
                        <el-tag>Disk Info</el-tag>
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
        margin: 10px 2px;
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
                data: {},
                disk: [],
                net: []
            }
        },

        methods: {

            obj2list: function (obj) {
                let ret = [];
                for (let prop in obj) {
                    if (obj.hasOwnProperty(prop)) {
                       ret.push({'k': prop, 'v': obj[prop]})
                    }
                }
                return ret;
            },

            getBasicInfo: function () {
                let _self = this;
                api.basic.get().then(function (response) {
                    _self.data = response.data.data;
                    _self.disk = _self.data.disk;
                    _self.net = _self.data.net;
                }, function (error) {

                });
            }
        },

        computed: {
            cpu: function () {
                // return this.obj2list(this.data.cpu);
                return this.data.cpu;
            },

            general: function () {
                // return this.obj2list(this.data.general);
                return this.data.general;
            },

            mem: function () {
                // return this.obj2list(this.data.mem);
                return this.data.mem;
            },

            swap: function () {
                // return this.obj2list(this.data.swap);
                return this.data.swap;
            }
        },

        mounted: function () {
            this.getBasicInfo();
        }
    }
</script>
