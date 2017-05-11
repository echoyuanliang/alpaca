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
                    color:["#18CF69", "#F0CBC5", "#20a0ff",  "#DAEAC6", "#F7BA2A", "#13CE66","#61a0a8", ],

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
                        trigger: 'axis',
                        axisPointer: {
                            type: 'shadow'
                        }
                    },

                    toolbox: {  // 工具
                        show: true,
                        feature: {
                            saveAsImage: {}
                        }
                    },

                    xAxis : {
                        type : 'category',
                        axisTick: {
                            alignWithLabel: true
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

                    },

                    yAxis : {
                        type : 'value',

                        axisLine: {
                            splitLine:{show: false},
                            splitArea : {show : true},
                            lineStyle: {
                                type: 'solid',
                                color: "#20A0FF",
                                width:'2'
                            }
                        },
                    },

                    series : [
                        {
                            name:'',
                            type:'bar',
                            barWidth: '60%',
                            data:[]
                        }
                    ]
                }
            };
        },

        methods: {
            initCharts: function () {
                if(this.label){
                    this.charts.yAxis['axisLabel'] = this.label;
                }

                this.charts.xAxis.data = this.names;
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
