import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            redirect: '/home'
        },
        {
            path: '/home',
            component: resolve => require(['../components/common/Home.vue'], resolve),
            meta: {
                needAuth: true
            },

            children:[
                {
                    path: '',
                    component: resolve => require(['../components/page/Basic.vue'], resolve),
                    meta: {
                        needAuth: true
                    }
                },

                {
                    path: '/system',
                    meta: {
                        needAuth: true
                    },
                    component: resolve => require(['../components/page/System.vue'], resolve)
                },

                {
                    path: '/network',
                    meta: {
                        needAuth: true
                    },
                    component: resolve => require(['../components/page/Network.vue'], resolve)

                },

                {
                    path: '/process/:pid',
                    name: 'process',
                    meta: {
                        needAuth: true
                    },
                    component: resolve => require(['../components/page/Process.vue'], resolve)
                }
            ]
        },
        {
            path: '/login',
            component: resolve => require(['../components/page/Login.vue'], resolve),
            meta: {
                needAuth: false
            }
        }
    ]
})
