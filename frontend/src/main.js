import Vue from 'vue';
import App from './App';
import router from './router';
import VueResource from 'vue-resource'
import axios from 'axios';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-default/index.css';    // 默认主题
// import '../static/css/theme-green/index.css';       // 浅绿色主题
// import 'jquery/dist/jquery.min.js'
// import 'semantic-ui/dist/semantic.js'
// import 'semantic-ui/dist/semantic.css'
import 'vue-animate/dist/vue-animate.css'

import "babel-polyfill";
import './mock/index.js';
import Resource from 'vue-resource';
import Auth from 'service/auth.js';

Vue.use(Resource);
Vue.use(ElementUI);
Vue.use(VueResource);
Vue.prototype.$axios = axios;

global.api = require('./api.js');

router.beforeEach((to, from, next) => {
    if (Auth.authenticated || ! to.meta.needAuth) {
        next();
    }else{
        next({
            path: '/login',
            query: {redirect: to.fullPath}
        });
    }
});


new Vue({
    router,
    render: h => h(App)
}).$mount('#app');

