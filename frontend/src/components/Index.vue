<template>
  <div id="app">
<el-row class = "container">
  <el-col :span="24" class="header">
    <el-col :span="4" class="logo">
      {{ logo_name }}
    </el-col>
    <el-col :span="16">
      <el-menu class="el-menu" theme="light" mode="horizontal" @select="handle_select">
        <el-menu-item index="1" class = "el-menu-item">首页</el-menu-item>
        <el-menu-item index="2" class = "el-menu-item">课程</el-menu-item>
        <el-menu-item index="3" class = "el-menu-item">联系我们</el-menu-item>
      </el-menu>
    </el-col>
    <el-col :span="4" class="userinfo">
      <el-dropdown trigger="click">
        <span class="el-dropdown-link">
          <i class="el-icon-setting"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item @click.native="personal_space" v-if="is_login">个人主页</el-dropdown-item>
          <el-dropdown-item @click.native="login" v-else>登录</el-dropdown-item>
          <el-dropdown-item divided @click.native="logout" v-if="is_login">登出</el-dropdown-item>
          <el-dropdown-item @click.native="register" v-else>注册</el-dropdown-item>          
        </el-dropdown-menu>
      </el-dropdown>
    </el-col>
  </el-col>
</el-row>
  <!-- 登录界面  -->
  <el-dialog title="登录" :visible="login_form_visible">
    <el-form :model="form" label-position="left">
      <el-form-item tyep="text" label="用户名" :label-width="form_label_width">
        <el-input v-model="login_form.name" auto_complete="off"></el-input>
      </el-form-item>
      <el-form-item label="密码" :label-width="form_label_width">
        <el-input type="password" v-model="login_form.password" auto_complete="off"></el-input>
      </el-form-item>
    </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click.native="login_confirm_clicked">确 定</el-button>
        <el-button @click.native="login_form_visible=false">取 消</el-button>
      </span>
  </el-dialog>
  <!-- 注册页面 -->
  <el-dialog title="注册" :visible="register_form_visible">
    <el-form :model="form" label-position="left">
      <el-form-item tyep="text" label="用户名" :label-width="form_label_width">
        <el-input v-model="register_form.name" auto_complete="off"></el-input>
      </el-form-item>
      <el-form-item tyep="text" label="姓名" :label-width="form_label_width">
        <el-input v-model="register_form.nickname" auto_complete="off"></el-input>
      </el-form-item>
      <el-form-item label="密码" :label-width="form_label_width">
        <el-input type="password" v-model="register_form.password" auto_complete="off"></el-input>
      </el-form-item>
      <el-form-item label="确认密码" :label-width="form_label_width">
        <el-input type="password" v-model="register_form.confirmed_password" auto_complete="off"></el-input>
      </el-form-item>
      <el-form-item type="text" label="北航邮箱" :label-width="form_label_width">
        <el-input v-model="register_form.email" auto_complete="off"></el-input>
      </el-form-item>
    </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click.native="register_confirm_clicked">确 定</el-button>
        <el-button @click.native="register_form_visible=false">取 消</el-button>
      </span>
  </el-dialog>

</div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      logo_name: 'BUAA-iCourse',
      is_login: true,
      login_form_visible: false,
      register_form_visible: false,
      form_label_width: '120px',
      login_form: {
        name: '',
        password: ''
      },
      register_form: {
        name: '',
        nickname: '',
        password: '',
        confirmed_password: '',
        email: ''
      }
    }
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
</style>