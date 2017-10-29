<template>
  <div id="personal">
    <el-col :span="24" class="header">
      {{ user_name }}
    </el-col>    
    <el-col :span="4">
      <el-menu default-active="2" class="el-menu-vertical-demo" theme="dark">
        <el-menu-item index="1" @click.native="ziliao">个人资料</el-menu-item>
        <el-menu-item index="2" @click.native="test">全部博文</el-menu-item>
        <el-menu-item index="3" @click.native="test">我的资源</el-menu-item>
        <el-menu-item index="4" @click.native="test">消息</el-menu-item>
        <el-menu-item index="5" @click.native="test">设置</el-menu-item>
      </el-menu>
    </el-col>
    <router-link to="/personalData">个人资料</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'personal',
  data () {
    return {
      user_name: '森高Slontia的花园 一只有情怀的程序猿'
    }
  },
  methods: {
    test: function () { alert(123) },
    ziliao: function () { this.$router.push({ path: '/personalData' }) }
  }
}
</script>

<style>
  .container {
    position: absolute;
    top: 0px;
    bottom: 0px;
    width: 100%;
  }
  .header{
    height: 60px;
    line-height: 60px;
    background: #20a0ff;
    color:#fff;
    text-align: center;
    font-size: 20px;
  }
  .logo{
    height: 60px;
    font-size: 22px;
    font-weight: bold;
    padding-left:20px;
    padding-right:20px;
    border-color: rgba(238,241,146,0.3);
    border-right-width: 0px;
    border-right-style: solid;
  }
  .userinfo {
    text-align: right;
    padding-right: 35px;
    float: right;
  }
  .el-menu-item {
    color: black;
    font-size: 16px;
    font-weight: bold;
  }
  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>