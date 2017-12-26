<template>
  <div id="personal">
    <el-col :span="24" class="header">
      <el-col :span="12" style="text-align:right;font-size:30px;font-weight:bold;">{{ nickname }}的花园</el-col>
      <el-col :span="12" style="text-align:left;font-size:20px;font-style:italic;"><p>{{ signature }}</p></el-col>
    </el-col>    
    <el-col :span="2" :offset="1">
      <el-menu @select="handle_select">
        <el-menu-item index="index" >首页</el-menu-item>
        <el-menu-item index="1" >个人资料</el-menu-item>
        <el-menu-item index="2" @click.native="test">全部博文</el-menu-item>
        <el-menu-item index="3" @click.native="test">我的资源</el-menu-item>
        <el-menu-item index="4" @click.native="test">消息</el-menu-item>
        <el-menu-item index="5" @click.native="test">设置</el-menu-item>
      </el-menu>
    </el-col>

  <el-col :span="14" style="margin:30px 0px 0px 0px;">
    <el-row>
      <el-col :span="6" :offset="1">
        <div id="headPortrait"><img :src="headPortrait" style="height:200px;"></img></div>
      </el-col>
      <el-col :span="14" :offset="2">
        <el-row style="margin:10px 0px 20px 0px;">
          <el-col :span="16">
            <el-row>
              <el-col :span="5">用户名:</el-col>
              <el-col :span="16">{{ username }}</el-col>          
            </el-row>
            <el-row>
              <el-col :span="4">昵称:</el-col>
              <el-col :span="16">{{ nickname }}</el-col>          
            </el-row>
            <el-row>
              <el-col :span="4">性别:</el-col>
              <el-col :span="20">{{ gender }}</el-col>
            </el-row>
            <el-row>
              <el-col :span="4">学院:</el-col>
              <el-col :span="20">{{ college }}</el-col>
            </el-row>
            <el-row v-if="is_host">
              <el-col :span="4">邮箱:</el-col>
              <el-col :span="20"> {{ email }} </el-col>
            </el-row>
            <el-row v-if="is_host&&!is_superuser">
              <el-col>
                <span style="color:red">该邮箱目前未通过验证</span>
                <el-button type="button" @click="email_check">点此认证</el-button>
              </el-col>
            </el-row>
            <!--el-row>
              <el-col :span="4">关注:</el-col>
              <el-col :span="6">{{ follows }}</el-col>
              <el-col :span="4">粉丝:</el-col>
              <el-col :span="6">{{ fans }}</el-col>
            </el-row-->
          </el-col>
          <el-col :span="8">
            <el-button type="button" @click="edit_info_button_clicked" v-if="is_host"><i class="el-icon-edit"></i>
              编辑资料
            </el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="6">个人介绍:</el-col>
        </el-row>
        <el-row>
          <el-col :span="24">{{ personalIntro }}</el-col>
        </el-row>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="22" :offset="1" style="background-color:green;">
      
      </el-col>
    </el-row>
  </el-col>
  
  <el-col :span="6" style="margin:30px 0px 0px 0px;">
    <el-col id="tableTitle">
      {{ username }}的主要贡献
    </el-col>  
    <el-table :data="tableData" stripe border style="width:100%">
    <el-table-column prop="course" label="课程" :span="12" >
    </el-table-column>
    <el-table-column prop="points" label="贡献点" :span="12">
    </el-table-column>
  </el-table>      
  </el-col>
  <el-dialog title="修改个人信息" :visible.sync="dialog_visible">
    <el-form :model="form" label-position="top" ref="form" :rules="form_rules">
      <el-form-item label="昵称" type="text" :label-width="form_label_width" prop="nickname" required>
        <el-input v-model="form.nickname" auto-complete="off" placeholder="昵称,20字符以内,支持中文"></el-input>
      </el-form-item>
        <el-form-item type="select" label="性别" :label-width="form_label_width" required>
        <el-select v-model="form.gender" placeholder="请选择性别">
          <el-option v-for="item in gender_options" :key="item.value" :label="item.label" :value="item.value"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item type="select" label="所在学院" :label-width="form_label_width" required>
        <el-select v-model="form.college_id" placeholder="所在学院">
          <el-option v-for="item in academy_options" :key="item.value" :label="item.label" :value="item.value"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item type="text" label="个人介绍" :label-width="form_label_width" prop="intro">
        <el-input v-model="form.intro" auto-complete="off" placeholder="一句话自我介绍，50字以内"></el-input>
      </el-form-item>
      
    </el-form>
    <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click.native="edit_confirm_clicked('form')">确 定</el-button>
        <el-button @click.native="dialog_visible=false">取 消</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
/* eslint-disable brace-style */
/* eslint-disable camelcase */
import $ from 'jquery'
import hp from './../assets/headportrait.jpg'
import get_url from './general/getUrl.js'
import college_map from './general/collegeMap.js'
export default {
  name: 'personal',
  data () {
    var check_nickname = (rule, value, callback) => {
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
    var check_intro = (rule, value, callback) => {
      setTimeout(() => {
        var l = value.length
        var rl = 0
        for (var i = 0; i < l; i++) {
          if ((value.charCodeAt(i) & 0xff00) !== 0) {
            rl++
          }
          rl++
        }
        if (rl >= 1 && rl <= 50) {
          callback()
        }
        else {
          callback(new Error('自我介绍长度必须在50位及以下'))
        }
      }, 500)
    }

    return {
      email: '',
      is_superuser: false,
      is_host: false,
      spaceName: this.username + '的花园',
      signature: '',
      username: '',
      nickname: '',
      gender: '',
      college: '暂无',
      follows: 0,
      fans: 0,
      personalIntro: '',
      tableData: [
        {
          course: '敬请期待',
          points: ''
        }
      ],
      headPortrait: hp,
      dialog_visible: false,
      form_label_width: '80px',
      form: {
        nickname: '',
        gender: '',
        intro: '',
        college_id: ''
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
      academy_options: [
      { label: '1系', value: 1 },
      { label: '2系', value: 2 },
      { label: '3系', value: 3 },
      { label: '4系', value: 4 },
      { label: '5系', value: 5 },
      { label: '6系', value: 6 },
      { label: '7系', value: 7 },
      { label: '8系', value: 8 },
      { label: '9系', value: 9 },
      { label: '10系', value: 10 },
      { label: '11系', value: 11 },
      { label: '12系', value: 12 },
      { label: '13系', value: 13 },
      { label: '14系', value: 14 },
      { label: '15系', value: 15 },
      { label: '16系', value: 16 },
      { label: '17系', value: 17 },
      { label: '18系', value: 18 },
      { label: '19系', value: 19 },
      { label: '20系', value: 20 },
      { label: '21系', value: 21 },
      { label: '23系', value: 23 },
      { label: '24系', value: 24 },
      { label: '25系', value: 25 },
      { label: '26系', value: 26 },
      { label: '27系', value: 27 },
      { label: '28系', value: 28 },
      { label: '29系', value: 29 },
      { label: '30系', value: 30 },
      { label: '32系', value: 32 },
      { label: '33系', value: 33 },
      { label: '51系', value: 51 },
      { label: '52系', value: 52 },
      { label: '56系', value: 56 },
      { label: '91系', value: 91 }
      ],
      form_rules: {
        nickname: [
          { validator: check_nickname, trigger: 'blur' }
        ],
        intro: [
          { validator: check_intro, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    email_check: function () {
      var post_url = get_url(this.$store.state.dev, '/sign/emailcheck/')
      var _this = this
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: post_url,
        type: 'POST',
        success: function (data) {
          var code = data['error']
          if (code === 0) {
            _this.$message({
              showClose: true,
              type: 'success',
              message: '认证邮件已发送至邮箱'
            })
          } else {
            _this.$message({
              showClose: true,
              type: 'error',
              message: '认证失败'
            })
          }
        },
        error: function () {
          _this.$message({
            showClose: true,
            type: 'error',
            message: '邮箱认证：无法连接至服务器'
          })
        }
      })
    },
    test: function () { alert('还未开放') },
    edit_confirm_clicked: function (form_name) {
      this.$refs[form_name].validate((valid) => {
        var post_url = get_url(this.$store.state.dev, '/user/modify/info/')
        var post_data = { nickname: this.form.nickname, gender: this.form.gender, intro: this.form.intro, college_id: this.form.college_id }
        var _this = this
        $.ajax({
          ContentType: 'application/json; charset=utf-8',
          dataType: 'json',
          url: post_url,
          type: 'POST',
          data: post_data,
          success: function (data) {
            var code = data['error']
            if (code === 0) {
              _this.dialog_visible = false
              _this.$router.go(0)
            } else if (code === 1) {
              _this.$message({
                showClose: true,
                type: 'error',
                message: '数据格式错误'
              })
            }
          },
          error: function () {
            _this.$message({
              showClose: true,
              type: 'error',
              message: '修改个人信息失败'
            })
          }
        })
      })
    },
    edit_info_button_clicked: function () {
      this.dialog_visible = !this.dialog_visible
    },
    handle_select: function (key, key_path) {
      if (key === 'index') {
        this.$router.push({ path: '/index' })
      }
    }
  },
  created: function () {
    for (var i = 0; i < this.academy_options.length; i++) {
      var college = this.academy_options[i]
      if (college_map[college['value']] !== undefined) {
        // alert(college_map[college['value']])
        this.academy_options[i]['label'] = college_map[college['value']]
      }
    }
    this.username = this.$route.params.username
    var personalSelf = this
    var post_url = get_url(this.$store.state.dev, '/sign/logged_in/')
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: post_url,
      type: 'POST',
      async: false,
      success: function (data) {
        personalSelf.is_host = (personalSelf.username === data['username'])
      },
      error: function () {
        alert('加载导航栏连接服务器失败')
      }
    })
    post_url = get_url(this.$store.state.dev, '/user/information/')
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: post_url,
      type: 'POST',
      data: {'username': personalSelf.username},
      success: function (data) {
        var user_info = data['user_info']
        personalSelf.username = user_info['username']
        personalSelf.nickname = user_info['nickname']
        personalSelf.form.nickname = user_info['nickname']
        personalSelf.form.gender = user_info['gender']
        if (user_info['gender'] === '1') {
          personalSelf.gender = '男'
        } else if (user_info['gender'] === '2') {
          personalSelf.gender = '女'
        } else if (user_info['gender'] === '0') {
          personalSelf.gender = '保密'
        } else {
          personalSelf.gender = ''
        }
        personalSelf.form.intro = user_info['intro']
        personalSelf.personalIntro = user_info['intro']
        var college_id = user_info['college_id']
        var college_name = (college_map.hasOwnProperty(college_id)) ? college_map[college_id] : college_id.toString() + '系'
        personalSelf.college = college_name
        personalSelf.form.college_id = college_id
        personalSelf.email = user_info['email']
        personalSelf.is_superuser = user_info['is_superuser']
      },
      error: function () {
        alert('fail')
      }
    })
  }
}
</script>

<style scpoed>
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
  #headPortrait {
    height: 200px;
    font-size: 20px;
    text-align: center;
    line-height: 200px;
  }
  #tableTitle {
    font-weight: bold;
    text-align: center;
    
    height: 40px;
    font-size: 20px;
  }
</style>
