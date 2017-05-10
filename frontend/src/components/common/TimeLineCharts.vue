<template>
        <echarts :option="charts"></echarts>
</template>

<script>
    import IEcharts from 'vue-echarts-v3';
    export default{
        components: {
            'echarts': IEcharts
        },

        props: {

            title: {
                type: String,
                default: ''
            },

            values: {
                type: Object,
                required: true,
                default: function () {
                    return {};
                }
            },

            names: {
                type: Array,
                required: true
            },

            label: {
                type: Object,
                required: false,
                default: function () {
                    return null;
                }
            }

        },

        data: function () {
            return {
                charts: {
                    color:["#20a0ff","#13CE66","#F7BA2A","#FF4949","#61a0a8", "#F0CBC5", "#DAEAC6"], // 折线颜色

                    tooltip: {  // 提示框
                        trigger: 'none',
                        axisPointer: {
                            type: 'cross',
                        },
                        lineStyle: {
                            color: '#48b',
                            width: 2,
                            type: 'solid'
                        }
                    },

                    title : {  // 主题
                        text : '',
                        textStyle: {
                            color: '#293C55',
                            fontSize: 16
                        },
                        left: 'left',
                        top: 'top'
                    },

                    legend : {  //折线标题
                        data : [],
                        itemWidth:20,
                        itemHeight:10,
                        textStyle:{
                            fontSize:14,
                            color:'#61A0A8'
                        }
                    },

                    toolbox: {  // 工具
                        show: true,
                        feature: {
                            dataZoom: {
                                yAxisIndex: 'none'
                            },
                            saveAsImage: {}
                        }
                    },

                    xAxis : { // X轴
                        type: 'category',

                        splitLine: {
                            show: false
                        },

                        axisLine: {
                            splitLine:{show: false},
                            splitArea : {show : true},
                            lineStyle: {
                                type: 'solid',
                                color: "#20A0FF",
                                width:'2'
                            }
                        },

                        axisLabel: {
                            textStyle: {
                                color: '#6c912d',
                            }
                        },

                        data:[]
                    },

                    yAxis : { // y轴
                        type : 'value',

                        splitLine: {
                            show: false
                        },

                        axisLine: {
                            splitLine:{show: false},
                            splitArea : {show : true},
                            lineStyle: {
                                type: 'solid',
                                color: "#20A0FF",
                                width:'2'
                            }
                        },
                        axisLabel: {
                            textStyle: {
                                color: '#6c912d',
                            }
                        }
                    },

                    series : []
                }
            };
        },


        methods: {
            initCharts: function () {
                if(this.label){
                    this.charts.yAxis['axisLabel'] = this.label;
                }

                this.charts.title.text = this.title;
                this.charts.xAxis.data = this.names;
                this.updateValues(this.values);
            },

            updateValues: function (values) {
                let keys = []
                for(let key in values){
                    keys.push(key);
                    this.charts.series.push({
                        name: key,
                        type: 'line',
                        smooth: true,
                        data: values[key]
                    });
                }

                this.charts.legend.data = keys;
            }
        },

        mounted: function() {
            this.initCharts();
        }
    }
</script>
