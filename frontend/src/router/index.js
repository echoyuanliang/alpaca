import Vue from 'vue';
import Router from 'vue-router';
import Auth from '../service/auth';

Vue.use(Router);

const router = new Router({
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
});

router.beforeEach((to, from, next) => {
    if (Auth.authenticated() || ! to.meta.needAuth) {
        next();
    }else{
        next({
            path: '/login',
            query: {redirect: to.fullPath}
        });
    }
});

export default router;

