<template>
    <el-col :span="span">
        <el-card>
            <el-row slot="header" type="flex" justify="center">
                <span class="span-name">{{header}}</span>
            </el-row>
            <div class="card-body">
                <div v-for="(value,key) in data" class="text item">
                    <el-row  type="flex" justify="space-around">
                        <el-col :span="11">
                            <span class="item-key">{{key}}:  </span>
                        </el-col>

                        <el-col :span="11">
                        <span>
                            {{value}}
                        </span>
                        </el-col>
                    </el-row>
                </div>
            </div>

        </el-card>

    </el-col>
</template>

<style>
    .text{
        font-size: 14px;
    }

    .item{
        padding: 10px 0;
    }

    .item-key{
        font-weight:bold;
        color: #35495E;
    }

    .item:hover{
        background: #F7F7F7;
    }

    .span-name{
        font-weight:bold;
        font-size:16px;
    }

    .card-body{
        height: 300px;
        overflow: scroll;
    }
</style>

<script>
    export default {
        props: {
            span: {
                type: Number,
                default: 7
            },

            data: {
                type: Object,
                required: true
            },

            header: {
                type:String,
                required: true
            }
        }
    }
</script>
