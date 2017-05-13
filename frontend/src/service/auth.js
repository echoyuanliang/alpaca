/**
 * Created by zhangyuanliang on 2017/4/21.
 */

export default {
    login: function(context, creds, redirect) {
        return context.$http.post('/api/login', creds).then( (response) => {
            let data = response.data.data;
            localStorage.setItem('user', data.user);
            if(redirect){
                context.$router.push(redirect);
            }
        }).catch((errors) => {
            context.$notify.error({
                title: '登录失败',
                message: '您的IP地址不合法或用户名密码错误'
            });
            console.error(errors);
        });
    },

    logout: function (context) {
        localStorage.removeItem('user');
        context.$router.push('/login');
    },

    user: function () {
      return localStorage.getItem('user');
    },

    authenticated: function () {
        let user = localStorage.getItem('user');
        if(user === undefined || user == null || user=='undefined'){
            return false;
        }
        return true;
    }
}
