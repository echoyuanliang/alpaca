/**
 * Created by zhangyuanliang on 2017/4/21.
 */

export default {
    authenticated: false,
    login(context, creds, redirect) {
        return context.$http.post('/api/login', creds).then( (data) => {
            localStorage.setItem('user', JSON.stringify(data.user));
            this.authenticated = true;
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

    user: function () {
      return localStorage.getItem('user');
    }
}
