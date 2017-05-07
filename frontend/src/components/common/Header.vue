<template>
        <el-menu :default-active="onRoutes" class="el-menu-vertical-demo" mode="horizontal"
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
</template>

<script>
    export default {
        computed:{
            onRoutes(){
                return this.$route.path.replace('/','');
            }
        }
    }
</script>
