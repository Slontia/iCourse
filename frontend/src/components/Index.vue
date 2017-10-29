<template>
  <div id="app">
    <Header></Header>
  </div>
</template>

<script type="text/javascript">
import Header from './general/Header'
export default {
  name: 'Index',
  components: {
    Header
  },
  methods: {
    handle_select: function () {},
    login: function () { this.login_form_visible = true },
    personal_space: function () { this.$router.push({ path: '/personal' }) },
    register: function () { this.register_form_visible = true },
    logout: function () {},
    login_confirm_clicked: function () { this.login_form_visible = false },
    register_confirm_clicked: function () { this.register_form_visible = false }
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
</script>