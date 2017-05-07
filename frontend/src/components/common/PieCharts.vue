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
                type: Array,
                required: true,
                default: function () {
                    return [];
                }
            },

            names: {
                type: Array,
                required: true
            }

        },

        data: function () {
            return {
                charts: {
                    color:["#20a0ff","#13CE66","#F7BA2A","#FF4949","#61a0a8", "#F0CBC5", "#DAEAC6"],

                    title : {  // 主题
                        text : '',
                        textStyle: {
                            color: '#293C55',
                            fontSize: 16
                        },
                        left: 'left',
                        top: 'top'
                    },

                    tooltip: {
                        trigger: 'item',
                        formatter: "{a} <br/>{b}: {c} ({d}%)"
                    },
                    legend: {
                        orient: 'vertical',
                        x: 'right',
                        top: 'middle',
                        itemWidth:20,
                        itemHeight:10,
                        textStyle:{
                            fontSize:14,
                            color:'#61A0A8'
                        },

                        data:[]
                    },

                    toolbox: {  // 工具
                        show: true,
                        feature: {
                            saveAsImage: {}
                        }
                    },

                    series : [
                        {
                            name:'',
                            type:'pie',
                            radius: ['50%', '70%'],
                            avoidLabelOverlap: false,
                            label: {
                                normal: {
                                    show: false,
                                    position: 'center'
                                },
                                emphasis: {
                                    show: true,
                                    textStyle: {
                                        fontSize: '30',
                                        fontWeight: 'bold'
                                    }
                                }
                            },
                            labelLine: {
                                normal: {
                                    show: false
                                }
                            },
                            data:[]
                        }
                    ]
                }
            };
        },


        methods: {
            initCharts: function () {
                this.charts.legend.data = this.names;
                this.charts.series[0].name = this.title;
                this.charts.title.text = this.title;
                this.charts.series[0].data = this.values;
            },
        },

        mounted: function() {
            this.initCharts();
        }
    }
</script>
