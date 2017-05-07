/**
 * Created by zhangyuanliang on 2017/4/21.
 */

var Vue = require('vue');
exports.login = Vue.resource('/api/login');
exports.basic = Vue.resource('/api/basic/');
exports.system = Vue.resource('/api/system/');
exports.network = Vue.resource('/api/network/');
exports.process = Vue.resource('/api/system/process/{pid}');
exports.iface_status = Vue.resource('/api/network/iface');
