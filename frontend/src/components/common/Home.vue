<template>
    <div class="wrapper">
        <v-head></v-head>
        <div>
            <transition><router-view></router-view></transition>
        </div>
    </div>
</template>

<script>
    import vHead from './Header.vue';
    export default {
        components:{
            vHead
        }
    }
</script>
