<template>
  <div id="personal">
    <div style="height:100px;width:100px;background-color:red;"></div>
  </div>

</template>

<script>
export default {
  name: 'personal',
  data () {
    return {
    }
  },
  methods: {
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
    font-size: 22px;
    font-weight: bold;
  }
</style>