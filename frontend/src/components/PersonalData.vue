<template>
<div id="personalData">
  <el-col :span="14" style="margin:30px 0px 0px 0px;">
    <el-row>
      <el-col :span="6" :offset="1">
        <div id="headPortrait"><img :src="headPortrait" style="height:200px;"></img></div>
      </el-col>
      <el-col :span="14" :offset="2">
        <el-row style="margin:10px 0px 20px 0px;">
          <el-col :span="16">
            <el-row>
              <el-col :span="4">昵称:</el-col>
              <el-col :span="16">{{ name }}</el-col>          
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
      森高的主要贡献
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
import hp from './../assets/headportrait.jpg'
export default {
  name: 'personalData',
  data () {
    return {
      name: '森高',
      gender: '男',
      college: '计算机学院',
      follows: 0,
      fans: 0,
      personalIntro: '这个人比较懒，还没有个人介绍哦~',
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
  }
}
</script>

<style>
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