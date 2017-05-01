/**
 * Created by zhangyuanliang on 2017/4/26.
 */

"use strict";

exports.filterNum = (num) =>{
    if(!num || num.toString().length <=3 ){
        return num
    }
    num = num.toString().replace(/(?=(?:\d{3})+(?!\d))/g,',');
    return num
};

exports.round = (num) =>{
    return num.toTixed(2);
};
