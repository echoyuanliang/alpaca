<template>
        <el-menu :default-active="onRoutes" class="el-menu-vertical-demo" theme="dark" unique-opened router>
            <el-menu-item index="home">
                <i class="el-icon-setting"></i>BASIC
            </el-menu-item>
            <el-menu-item index="system">
                <i class="el-icon-menu"></i>SYSTEM
            </el-menu-item>
            <el-menu-item index="network">
                <i class="el-icon-star-on"></i>NETWORK
            </el-menu-item>
        </el-menu>
</template>

<script>
    import ElMenuItem from "../../../node_modules/element-ui/packages/menu/src/menu-item";
    import ElMenu from "../../../node_modules/element-ui/packages/menu/src/menu";
    export default {
        components: {ElMenu, ElMenuItem}, computed:{
            onRoutes(){
                return this.$route.path.replace('/','');
            }
        }
    }
</script>
