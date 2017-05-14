import Vue from 'vue';
import App from './App';
import router from './router';
import VueResource from 'vue-resource'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-default/index.css';

import "babel-polyfill";
import Resource from 'vue-resource';
import VueLogger from 'vue-logger';


Vue.use(Resource);
Vue.use(ElementUI);
Vue.use(VueResource);
Vue.use(VueLogger);

global.api = require('./api.js');

new Vue({
    el: '#app',
    router,
    render: h => h(App)
}).$mount('#app');

