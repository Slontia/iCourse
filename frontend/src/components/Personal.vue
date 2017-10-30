<template>
  <div id="personal">
    <el-col :span="24" class="header">
      <el-col :span="12" style="text-align:right;font-size:30px;font-weight:bold;">{{ spaceName }}</el-col>
      <el-col :span="12" style="text-align:left;font-size:20px;font-style:italic;"><p>{{ signature }}</p></el-col>
    </el-col>    
    <el-col :span="2" :offset="1">
      <el-menu>
        <el-menu-item index="1" @click.native="toPersonalData">个人资料</el-menu-item>
        <el-menu-item index="2" @click.native="test">全部博文</el-menu-item>
        <el-menu-item index="3" @click.native="test">我的资源</el-menu-item>
        <el-menu-item index="4" @click.native="test">消息</el-menu-item>
        <el-menu-item index="5" @click.native="test">设置</el-menu-item>
      </el-menu>
    </el-col>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'personal',
  data () {
    return {
      spaceName: '森高Slontia的花园',
      signature: '一只有情怀的程序猿'
    }
  },
  methods: {
    test: function () { alert('还未开放') },
    toPersonalData: function () { this.$router.push({ path: '/personalData' }) }
  }
}
</script>

<style>
  .header{
    height: 60px;
    line-height: 60px;
    background: #20a0ff;
    color:#fff;
    text-align: center;
    font-size: 20px;
  }
  .el-menu-item {
    color: black;
    font-size: 14px;
  }
  .el-row {
    margin-bottom: 10px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 0px;
  }
</style>