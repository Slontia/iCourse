<template>
  <div id="personal">
    <el-col :span="24" class="header">
      <el-col :span="12" style="text-align:right;font-size:30px;font-weight:bold;">{{ nickname }}的花园</el-col>
      <el-col :span="12" style="text-align:left;font-size:20px;font-style:italic;"><p>{{ signature }}</p></el-col>
    </el-col>    
    <el-col :span="2" :offset="1">
      <el-menu>
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
              <el-col :span="4">用户名:</el-col>
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
            <el-row>
              <el-col :span="4">关注:</el-col>
              <el-col :span="6">{{ follows }}</el-col>
              <el-col :span="4">粉丝:</el-col>
              <el-col :span="6">{{ fans }}</el-col>
            </el-row>
          </el-col>
          <el-col :span="8">
            <el-button type="button"><i class="el-icon-edit"></i>
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
  </div>
</template>

<script>
import $ from 'jquery'
import hp from './../assets/headportrait.jpg'
export default {
  name: 'personal',
  data () {
    return {
      spaceName: this.username + '的花园',
      signature: '一只有情怀的程序猿',
      username: '',
      nickname: '',
      gender: '',
      college: '暂无',
      follows: 0,
      fans: 0,
      personalIntro: 'NULL',
      tableData: [
        {
          course: '工科数学分析',
          points: '100'
        },
        {
          course: '软件工程基础',
          points: '38'
        },
        {
          course: '工科高等代数',
          points: '19'
        },
        {
          course: 'C++/C#程序设计',
          points: '3'
        }
      ],
      headPortrait: hp
    }
  },
  methods: {
    test: function () { alert('还未开放') }
  },
  created: function () {
    var personalSelf = this
    /*
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: '/sign/logged_in/',
      type: 'POST',
      async: false,
      success: function (data) {
        personalSelf.username = data['username']
      },
      error: function () {
        alert('加载导航栏连接服务器失败')
      }
    })
    */
    this.username = this.$route.params.username
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: '/user/information/',
      type: 'POST',
      data: {'username': personalSelf.username},
      success: function (data) {
        personalSelf.username = data['user_info']['username']
        personalSelf.nickname = data['user_info']['nickname']
        if (data['user_info']['gender'] === '1') {
          personalSelf.gender = '男'
        } else if (data['user_info']['gender'] === '2') {
          personalSelf.gender = '女'
        } else {
          personalSelf.gender = '保密'
        }
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
