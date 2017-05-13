<template>
    <div class="header">
        <el-row type="flex" justify="space-between">
            <el-col :span="8">
                <el-menu :default-active="onRoutes" mode="horizontal"
                         theme="dark" unique-opened router>
                    <el-menu-item index="/home">
                        <i class="el-icon-setting"></i>Alpaca
                    </el-menu-item>
                    <el-menu-item index="/system">
                        <i class="el-icon-menu"></i>SYSTEM
                    </el-menu-item>
                    <el-menu-item index="/network">
                        <i class="el-icon-star-on"></i>NETWORK
                    </el-menu-item>
                </el-menu>
            </el-col>
            <el-col :span="8">
                <search-process :style="{height: '100%'}"></search-process>
            </el-col>
            <el-col :span="2">
                <el-menu mode="horizontal" theme="dark" unique-opened @select="handleSelect">
                    <el-submenu index="auth">
                        <template slot="title">{{username}}</template>
                        <el-menu-item index="logout">LogOut</el-menu-item>
                    </el-submenu>
                </el-menu>
            </el-col>
        </el-row>
    </div>
</template>

<style scoped>
    div.header{
        background-color: #324157;
    }

</style>
<script>
    import Auth from "../../service/auth.js";
    import SearchProcess from './SearchProcess.vue';

    export default {
        components: {
            'search-process': SearchProcess
        },

        computed:{
            onRoutes(){
                return this.$route.path.replace('/','');
            }
        },

        data: function(){
            return {
                username: Auth.user()
            }
        },

        methods: {
            handleSelect: function (key) {
               if(key == 'logout'){
                   Auth.logout(this);
               }
            }
        }
    }
</script>
