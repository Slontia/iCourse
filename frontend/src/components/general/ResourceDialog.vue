<template>
  <div id="resourceDialog">
    <el-row>
        <el-col :span="24">
          <div id="dialogTitle">全部资源</div>
        </el-col>
      </el-row>
      <el-row style="margin:15px 0px 0px 0px;">
        <el-col :span="16" :offset="1">
          <el-row>
            <el-col :span="8">
              资源名称:
            </el-col>
            <el-col :span="16">
              {{ this.$store.state.name }}
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="8">
              上传者:
            </el-col>
            <el-col :span="16">
              <img :src="zipImg" style="height:18px;"></img>
              <a href="">{{ this.$store.state.author }}</a>
            </el-col>
          </el-row>
          <el-row style="margin:10px 0px 0px 0px;">
            <el-col :span="8">
              上传时间:
            </el-col>
            <el-col :span="16">
              {{ this.$store.state.time }}
            </el-col>
          </el-row>
          <el-row style="margin:10px 0px 0px 0px;">
            <el-col :span="8">
              资源大小:
            </el-col>
            <el-col :span="16">
              {{ this.$store.state.size }}
            </el-col>
          </el-row>
          <el-row style="margin:10px 0px 0px 0px;">
            <el-col :span="24">
              简介:
            </el-col>
          </el-row>
          <el-row style="margin:10px 0px 0px 0px;">
            <el-col :span="24">
              {{ this.$store.state.intro }}
            </el-col>
          </el-row>
        </el-col>
        <el-col :span="7">
          <el-row style="text-align:center;">
            <img :src="zipImg" style="height:120px;"></img>
          </el-row>
          <el-row style="text-align:center;">
            <el-button type="primary">点击下载</el-button>
          </el-row>
        </el-col>
      </el-row>
      <el-row style="margin:10px 0px 0px 0px;">
        <el-col :span="2" :offset="1">标签:</el-col>
        <el-col :span="3">课件:</el-col>
        <el-col :span="2" :offset="11"><a href="">好评</a></el-col>
        <el-col :span="1">21</el-col>
        <el-col :span="2" :offset="1"><a href="">差评</a></el-col>
        <el-col :span="1">2</el-col>
      </el-row>
      <el-row style="margin:10px 0px 0px 0px;">
        <el-col :span="1" :offset="1"><i class="el-icon-star-off"></i></el-col>
        <el-col :span="1">23</el-col>
        <el-col :span="1" :offset="1"><i class="el-icon-arrow-down"></i></el-col>
        <el-col :span="1">656</el-col>
      </el-row>
      <el-row style="margin:20px 0px 0px 0px;">
        <el-col :span="6" :offset="1" style="height:20px;font-weight:bold;font-size:20px;">全部评论</el-col>
        <el-col :span="1" :offset="1" style="height:20px;line-height:20px;"><i class="el-icon-message"></i></el-col>
        <el-col :span="1" style="height:20px;line-height:20px;">0</el-col>
        <el-col :span="4" :offset="10" style="height:20px;line-height:20px;"><a href="">我要评论</a></el-col>        
      </el-row>
      <el-row style="margin:5px 0px 0px 0px;">
        <el-col :span="22" :offset="1">
          <el-row style="background-color:black;height:3px;"></el-row>
        </el-col>
      </el-row>
  </div>
</template>

<script>
import ZipImg from './../../assets/headportrait.jpg'
export default {
  name: 'ResourceDialog',
  data () {
    return {
      zipImg: ZipImg
    }
  },
  methods: {
  }
}
</script>

<style>
</style>