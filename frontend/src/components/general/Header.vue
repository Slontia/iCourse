<template>
  <div id="header">
<el-row class = "container">
  <el-col :span="24" class="header">
    <el-col :span="4" class="logo">
      {{ logo_name }}
    </el-col>
    <el-col :span="16">
      <el-menu class="el-menu" theme="light" mode="horizontal" @select="handle_select">
        <el-menu-item index="index" class = "el-menu-item">首页</el-menu-item>
        <el-menu-item index="course" class = "el-menu-item">课程</el-menu-item>
        <el-menu-item index="about" class = "el-menu-item">联系我们</el-menu-item>
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
    <el-form :model="login_form" label-position="left">
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
    <el-form :model="register_form" label-position="left" :rules="rules">
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
      <el-form-item type="text" label="北航邮箱" :label-width="form_label_width" prop="email">
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
/* eslint-disable brace-style */
/* eslint-disable camelcase */
export default {
  name: 'Header',
  data () {
    var check_email = (rule, value, callback) => {
      setTimeout(() => {
        var pattern = new RegExp(/^[a-zA-Z0-9_-]+@buaa.edu.cn$/)
        if (pattern.test(value)) {
          callback()
        }
        else {
          callback(new Error('亲你填的不是北航邮箱啊?'))
        }
      }, 1000)
    }
    return {
      logo_name: 'BUAA-iCourse',
      is_login: false,
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
      },
      rules: {
        email: [
          { validator: check_email, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    handle_select: function (key, keyPath) {
      if (key === 'index') {
        this.$router.push({ path: '/index' })
      }
      else if (key === 'course') {
        this.$router.push({ path: '/course' })
      }
    },
    login: function () { this.login_form_visible = true },
    personal_space: function () {},
    register: function () { this.register_form_visible = true },
    logout: function () {},
    login_confirm_clicked: function () { this.login_form_visible = false },
    register_confirm_clicked: function () { this.register_form_visible = false }
  }
}
</script>

<style>
 .header{
    height: 60px;
    line-height: 60px;
    background: #20a0ff;
    color:#fff;
      }
  .container {
    position: absolute;
    height: 60px;
    top: 0px;
    bottom: 0px;
    width: 100%;

   
   
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
  }
 
</style>