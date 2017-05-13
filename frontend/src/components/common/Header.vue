<template>
    <div class="header">
        <el-row type="flex" justify="space-between">
            <el-col :span="14">
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

    div.el-dropdown{
        width: 100%;
        height: 100%;
    }
</style>
<script>
    import ElMenu from "../../../node_modules/element-ui/packages/menu/src/menu";
    import Auth from "../../service/auth.js";
    import ElMenuItem from "../../../node_modules/element-ui/packages/menu/src/menu-item";
    import ElSubmenu from "../../../node_modules/element-ui/packages/menu/src/submenu";

    export default {
        components: {ElSubmenu, ElMenuItem, ElMenu}, computed:{
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
