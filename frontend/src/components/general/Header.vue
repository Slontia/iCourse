<template>
  <div id="header">
<el-row class = "container">
  <el-col :span="24" class="header">
    <el-col :span="4" class="logo">
      {{ logo_name }}
    </el-col>
    <el-col :span="16" class="menu">
      <el-menu class="el-menu" theme="light" mode="horizontal" @select="handle_select" style="background-color: white;">
        <el-menu-item index="index" class = "el-menu-item" style="margin-right: 20px;">首页</el-menu-item>
        <el-menu-item index="course" class = "el-menu-item"style="margin-right: 20px">课程</el-menu-item>
        <el-menu-item index="about" class = "el-menu-item">联系我们</el-menu-item>
      </el-menu>
    </el-col>
    <el-col :span="4" class="userinfo">
      <el-dropdown trigger="click">
        <span class="el-dropdown-link">
          <el-button type="text" v-if="!is_login">登录/注册</el-button>
          <el-button type="text" v-else>{{username}}</el-button>
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
  <el-dialog title="登录" :visible="login_form_visible" size="tiny" :before-close="handle_close_login" id="login_dialog">
    <el-form :model="login_form" label-position="left" :rules="login_rules" ref="login_form">
      <el-form-item type="text" label="用户名" :label-width="form_label_width" prop="username" id="login_form1">
        <el-input v-model="login_form.username" auto_complete="off"></el-input>
      </el-form-item>
      <el-form-item label="密码" :label-width="form_label_width" prop="password" id="login_form2">
        <el-input type="password" v-model="login_form.password" auto_complete="off" size="small"></el-input>
      </el-form-item>
    </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click.native="login_confirm_clicked('login_form')">确 定</el-button>
        <el-button @click.native="login_form_visible=false">取 消</el-button>
      </span>
  </el-dialog>
  <!-- 注册页面 -->
  <el-dialog title="注册" :visible="register_form_visible" :before-close="handle_close_register">
    <el-form :model="register_form" label-position="left" :rules="register_rules" ref="register_form" >
      <el-form-item tyep="text" label="用户名" :label-width="form_label_width" prop="username" id="register_form1">
        <el-input v-model="register_form.username" auto_complete="off" placeholder="唯一的用户名,由字母/数字/下划线组成，大小写不敏感，20字符以内"></el-input>
      </el-form-item>
      <el-form-item type="text" label="昵称" :label-width="form_label_width" prop="nickname" id="register_form2">
        <el-input v-model="register_form.nickname" auto_complete="off" placeholder="昵称,20字符以内,支持中文"></el-input>
      </el-form-item>
      <el-form-item type="select" label="性别" :label-width="form_label_width" prop="gender" id="register_form3">
        <el-select v-model="register_form.gender" placeholder="请选择性别">
          <el-option v-for="item in gender_options" :key="item.value" :label="item.label" :value="item.value"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="密码" :label-width="form_label_width" prop="password" id="register_form4">
        <el-input type="password" v-model="register_form.password" auto_complete="off" placeholder="8-20位,大小写敏感"></el-input>
      </el-form-item>
      <el-form-item label="确认密码" :label-width="form_label_width" prop="confirmed_password" id="register_form5">
        <el-input type="password" v-model="register_form.confirmed_password" auto_complete="off" placeholder="确认密码"></el-input>
      </el-form-item>
      <el-form-item type="text" label="北航邮箱" :label-width="form_label_width" prop="email" id="register_form6">
        <el-input v-model="register_form.email" auto_complete="off" placeholder="合法的北航邮箱"></el-input>
      </el-form-item>
    </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click.native="register_confirm_clicked('register_form')">确 定</el-button>
        <el-button @click.native="register_form_visible=false">取 消</el-button>
      </span>
  </el-dialog>
</div>
</template>

<script>
import $ from 'jquery'
// import json from 'json5'
/* eslint-disable brace-style */
/* eslint-disable camelcase */
export default {
  name: 'Header',
  beforeCreate: function () {
    var self = this
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: 'sign/logged_in/',
      type: 'POST',
      success: function (data) {
        self.username = data['username']
        if (self.username == null) {
          self.is_login = false
        } else {
          self.is_login = true
        }
      },
      error: function () {
        alert('加载导航栏连接服务器失败')
      }
    })
  },
  data () {
    var username_check_empty = (rule, value, callback) => {
      if (!value) {
        callback(new Error('用户名不能为空'))
      }
      callback()
      // setTimeout(() => {  }, 500)
    }
    var password_check_empty = (rule, value, callback) => {
      if (!value) {
        callback(new Error('密码不能为空'))
      }
      callback()
      // setTimeout(() => { callback() }, 500)
    }
    var check_username = (rule, value, callback) => {
      if (!value) {
        callback(new Error('用户名不能为空'))
      }
      setTimeout(() => {
        value = value.toLowerCase()
        var pattern = new RegExp(/^[a-z0-9_]{1,20}$/)
        if (pattern.test(value)) {
          callback()
        }
        else {
          callback(new Error('用户名格式错误'))
        }
      }, 500)
    }
    var check_nickname = (rule, value, callback) => {
      if (!value) {
        callback(new Error('昵称不能为空'))
      }
      setTimeout(() => {
        var l = value.length
        var rl = 0
        for (var i = 0; i < l; i++) {
          if ((value.charCodeAt(i) & 0xff00) !== 0) {
            rl++
          }
          rl++
        }
        if (rl >= 1 && rl <= 20) {
          callback()
        }
        else {
          callback(new Error('昵称长度必须在20位及以下'))
        }
      }, 500)
    }
    var check_gender = (rule, value, callback) => {
      if (!value) {
        callback(new Error('性别不能为空'))
      }
      callback()
    }
    var check_password = (rule, value, callback) => {
      if (!value) {
        callback(new Error('密码不能为空'))
      }
      setTimeout(() => {
        var pattern = new RegExp(/^.{8,20}$/)
        if (pattern.test(value)) {
          callback()
        }
        else {
          callback(new Error('密码长度必须在8-20位'))
        }
      }, 500)
    }
    var check_confirmed_password = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请再次输入密码'))
      }
      setTimeout(() => {
        if (value === this.register_form.password) {
          callback()
        }
        else {
          callback(new Error('两次输入密码不一致'))
        }
      }, 500)
    }
    var check_email = (rule, value, callback) => {
      if (!value) {
        callback(new Error('邮箱不能为空'))
      }
      setTimeout(() => {
        var pattern = new RegExp(/^[a-zA-Z0-9_-]+@buaa.edu.cn$/)
        if (pattern.test(value)) {
          callback()
        }
        else {
          callback(new Error('非法邮箱，邮箱必须是北航邮箱'))
        }
      }, 500)
    }
    return {
      logo_name: 'BUAA-iCourse',
      is_login: false,
      login_form_visible: false,
      register_form_visible: false,
      form_label_width: '80px',
      username: '',
      login_form: {
        username: '',
        password: ''
      },
      register_form: {
        username: '',
        nickname: '',
        gender: '',
        password: '',
        confirmed_password: '',
        email: ''
      },
      gender_options: [{
        value: '1',
        label: '男'
      }, {
        value: '2',
        label: '女'
      }, {
        value: '0',
        label: '保密'
      }],
      login_rules: {
        username: [
          { validator: username_check_empty, trigger: 'blur' }
        ],
        password: [
          { validator: password_check_empty, trigger: 'blur' }
        ]
      },
      register_rules: {
        username: [
          { validator: check_username, trigger: 'blur' }
        ],
        nickname: [
          { validator: check_nickname, trigger: 'blur' }
        ],
        gender: [
          { validator: check_gender, trigger: 'blur' }
        ],
        password: [
          { validator: check_password, trigger: 'blur' }
        ],
        confirmed_password: [
          { validator: check_confirmed_password, trigger: 'blur' }
        ],
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
    logout: function () {
      var self = this
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: 'sign/logout/',
        type: 'POST',
        success: function (data) {
          switch (data['error']) {
            case 0:
              self.is_login = false
              self.username = null
              alert('登出成功')
              break
            case 301:
              alert('登出失败')
              break
            default:
              alert('未知错误')
          }
        },
        error: function () {
          alert('登出连接服务器失败')
        }
      })
    },
    login_confirm_clicked: function (form_name) { this.$refs[form_name].validate((valid) => {
      if (valid) {
        var post_data = {
          'username': this.login_form['username'],
          'password': this.login_form['password']
        }
        var self = this
        $.ajax({
          ContentType: 'application/json; charset=utf-8',
          dataType: 'json',
          url: 'sign/login/',
          type: 'POST',
          data: post_data,
          success: function (data) {
            // data = JSON.parse(data)
            // login_form_visible = false
            switch (data['error']) {
              case 0:
                self.login_form_visible = false
                self.username = post_data['username']
                self.is_login = true
                alert('登录成功')
                break
              case 101:
                alert('用户名不存在或账号未被激活')
                break
              case 102:
                alert('密码错误')
                break
              default:
                alert('未知错误')
            }
          },
          error: function () {
            alert('服务器连接异常')
          }
        })
      } else {
        return false
      }
    })
    },
    handle_close_login (done) {
      this.login_form_visible = false
    },
    handle_close_register (done) {
      this.register_form_visible = false
    },
    register_confirm_clicked: function (form_name) { this.$refs[form_name].validate((valid) => {
      if (valid) {
        var post_data = {
          'username': this.register_form['username'],
          'password1': this.register_form['password'],
          'password2': this.register_form['confirmed_password'],
          'email': this.register_form['email'],
          'gender': this.register_form['gender'],
          'nickname': this.register_form['nickname'],
          'intro': null
        }
        var self = this
        $.ajax({
          ContentType: 'application/json; charset=utf-8',
          dataType: 'json',
          url: 'sign/register/',
          type: 'POST',
          data: post_data,
          success: function (data) {
            switch (data['error']) {
              case 0:
                self.register_form_visible = false
                alert('注册成功')
                break
              case 201:
                alert('用户名或邮箱已被注册')
                break
              case 202:
                alert('注册异常')
                break
              default:
                alert('未知错误')
            }
          },
          error: function () {
            alert('服务器连接异常')
          }
        })
      }
      else {
        return false
      }
    }) }
  }
}
</script>

<style>
 .header{
    height: 60px;
    line-height: 60px;
    }
  .container {
    height: 60px;
    width: auto;
  }
  .logo{
    height: 60px;
    font-size: 24px;
    font-weight: 500;
    color: #409EFF;
    font-family: Microsoft YaHei;
    padding-left:20px;
    padding-right:20px;
    margin-right: 50px;
    border-right-width: 0px;
    width:auto;
  }
  .userinfo {
    text-align: right;
    float: right;
    width: auto;
    padding-right: 10px;
  }
  .el-menu-item {
    font-size: 22px;
    font-family: Microsoft YaHei;
  }
  .el-dropdown-link{
    font-family: Microsoft YaHei;
    color: #409EFF;
  }
 
</style>