import Vue from 'vue';
import App from './App';
import router from './router';
import VueResource from 'vue-resource'
import axios from 'axios';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-default/index.css';    // 默认主题

import "babel-polyfill";
import Resource from 'vue-resource';
import Auth from 'service/auth.js';
import VueLogger from 'vue-logger';
Vue.use(Resource);
Vue.use(ElementUI);
Vue.use(VueResource);
Vue.use(VueLogger);
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

