<template>
    <div>
        <el-select
            v-model="search_input"
            filterable
            remote
            placeholder="Please input pid/process name/cmdline"
            size="large"
            :remote-method="searchProcess"
            :loading="search_loading"
            @change="procSelected">
            <el-option
                v-for="item in search_result" :key="item" :label="item" :value="item">
            </el-option>
        </el-select>
    </div>
</template>

<style scoped>
    div.el-select{
        width: 100%;
        margin-top: 8px;
    }

</style>

<script>

    export default {

        data: function () {
            return {
                search_input: null,
                search_loading: false,
                search_result: [],
            };
        },

        methods: {
            searchProcess: function (query) {
                if(query != ''){
                    this.search_loading = true;
                    api.search_process.get({'q': query}).then((response)=>{
                        this.search_loading = false;
                        let res_list = response.data.data;
                        this.search_result = res_list.map((item)=>{
                            return item.slice(0, 40);
                        });
                    }, (error)=>{

                    });
                }
            },

            procSelected: function () {
                const pid = this.search_input.split('-')[0];
                this.search_input = null;
                this.search_result = [];
                this.$router.push({name: 'process', params: {pid: pid}});
            }
        }
    }
</script>
