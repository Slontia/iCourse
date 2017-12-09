<template>
  <div id="resourceDialog">
      <el-row style="margin:0px 0px 0px 0px;">
        <el-col :span="16" :offset="1">
          <el-row>
            <el-col :span="24">
              <span class="text" style="font-size: 20px;">{{ this.$store.state.name }}</span>
            </el-col>
          </el-row>
          <el-row style="margin:15px 0px 0px 0px;">
            <el-col :span="8">
              上传者:
            </el-col>
            <el-col :span="16">
              <!--<img :src="defaultImg" style="height:18px;"></img>-->
              {{ this.$store.state.author }}
            </el-col>
          </el-row>
          <el-row style="margin:15px 0px 0px 0px;">
            <el-col :span="8">
              上传时间:
            </el-col>
            <el-col :span="16">
              {{ this.$store.state.time }}
            </el-col>
          </el-row>
          <el-row style="margin:15px 0px 0px 0px;">
            <el-col :span="8">
              资源大小:
            </el-col>
            <el-col :span="16">
              {{ this.$store.state.size }}
            </el-col>
          </el-row>
          <el-row style="margin:15px 0px 0px 0px;">
            <el-col :span="24">
              简介:
            </el-col>
          </el-row>
          <el-row style="margin:15px 0px 0px 0px;">
            <el-col :span="24">
              <span class="text">{{ this.$store.state.intro }}</span>
            </el-col>
          </el-row>
          <el-row style="margin:15px 0px 0px 0px;">
            <el-col :span="8">
              大家的评分<span style="color:#ccc">({{ rate_count }})</span>:
            </el-col>
            <el-col :span="16">
              <el-rate v-model="public_rate" :colors="['#99A9BF', '#F7BA2A', '#FF9900']" show-text disabled text-tamplate="{value}">
          </el-rate>
            </el-col>
          </el-row>
          <el-row style="margin:15px 0px 0px 0px;">
            <el-col :span="8">
              你的评分:
            </el-col>
            <el-col :span="16">
              <el-rate v-model="rate" :colors="['#99A9BF', '#F7BA2A', '#FF9900']" show-text :disabled="rate_disable" @change="handle_rate_change">
          </el-rate>
            </el-col>
          </el-row>
        </el-col>
        <el-col :span="7">
          <el-row style="text-align:center;">
            <img :src='img' style="height:120px;"></img>
          </el-row>
          <el-row style="text-align:center;">
            <el-button type="primary" @click.native="gotoDownload">点击下载</el-button>
          </el-row>
        </el-col>
      </el-row>
      <el-row style="margin:10px 0px 0px 0px;">
        
      </el-row>
      <!--
      <el-row style="margin:10px 0px 0px 0px;">
        <el-col :span="1" :offset="1"><i class="el-icon-star-off"></i></el-col>
        <el-col :span="1">0</el-col>
        <el-col :span="1" :offset="1"><i class="el-icon-arrow-down"></i></el-col>
        <el-col :span="1">{{ this.$store.state.download_count }}</el-col>
      </el-row>
    -->

      <!--
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
    -->
  </div>
</template>

<script>
/* eslint-disable camelcase */
import DefaultImg from './../../assets/fileico/generic.png'
import DocImg from './../../assets/fileico/docx_win.png'
import PdfImg from './../../assets/fileico/pdf.png'
import PptImg from './../../assets/fileico/pptx.png'
import JpgImg from './../../assets/fileico/jpeg.png'
import ZipImg from './../../assets/fileico/zip.png'
import RarImg from './../../assets/fileico/rar.png'
import $ from 'jquery'
import get_url from './getUrl.js'

export default {
  name: 'ResourceDialog',
  data () {
    return {
      zipImg: ZipImg,
      pdfImg: PdfImg,
      pptImg: PptImg,
      docImg: DocImg,
      jpgImg: JpgImg,
      rarImg: RarImg,
      defaultImg: DefaultImg,
      img: '',
      rate: 0,
      public_rate: '',
      rate_disable: true
    }
  },
  methods: {
    gotoDownload: function () {
      var sh = this
      var post_url = get_url(this.$store.state.dev, '/resource/download_count/')
      window.open(this.$store.state.url)
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: post_url,
        type: 'POST',
        data: { 'download_count': sh.$store.state.id },
        success: function (data) {
          sh.$store.state.id = data['download_count']
        },
        error: function () {
          alert('拉取资源列表失败')
        }
      })
    },
    handle_rate_change: function () {
      var post_url = get_url(this.$store.state.dev, '/resource/evaluate/')
      var post_data = { resource_id: this.$store.state.id, grade: this.rate }
      console.log(this.rate)
      var _this = this
      if (this.rate_disable) return
      if (!this.$store.state.is_login) {
        this.$message({
          showClose: true,
          type: 'error',
          message: '请先登录再评分'
        })
        return
      }
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: post_url,
        type: 'POST',
        data: post_data,
        success: function (data) {
          var code = data['error']
          if (code === 0) {
            _this.$message({
              showClose: true,
              type: 'success',
              message: '评分成功'
            })
          } else {
            _this.$message({
              showClose: true,
              type: 'error',
              message: '评分失败了呢'
            })
          }
        },
        error: function () {
          _this.$message({
            showClose: true,
            type: 'error',
            message: '无法连接到服务器'
          })
        }
      })
    }
  },
  created: function () {
    this.img = this.defaultImg
    let tL = this.$store.state.name.length
    if (this.$store.state.name[tL - 3].toLowerCase() === 'd' && this.$store.state.name[tL - 2].toLowerCase() === 'o' && this.$store.state.name[tL - 1].toLowerCase() === 'c') {
      this.img = this.docImg
    }
    if (this.$store.state.name[tL - 3].toLowerCase() === 'p' && this.$store.state.name[tL - 2].toLowerCase() === 'p' && this.$store.state.name[tL - 1].toLowerCase() === 't') {
      this.img = this.pptImg
    }
    if (this.$store.state.name[tL - 3].toLowerCase() === 'p' && this.$store.state.name[tL - 2].toLowerCase() === 'd' && this.$store.state.name[tL - 1].toLowerCase() === 'f') {
      this.img = this.pdfImg
    }
    if (this.$store.state.name[tL - 3].toLowerCase() === 'z' && this.$store.state.name[tL - 2].toLowerCase() === 'i' && this.$store.state.name[tL - 1].toLowerCase() === 'p') {
      this.img = this.zipImg
    }
    if (this.$store.state.name[tL - 3].toLowerCase() === 'r' && this.$store.state.name[tL - 2].toLowerCase() === 'a' && this.$store.state.name[tL - 1].toLowerCase() === 'r') {
      this.img = this.rarImg
    }
    if (this.$store.state.name[tL - 3].toLowerCase() === 'j' && this.$store.state.name[tL - 2].toLowerCase() === 'p' && this.$store.state.name[tL - 1].toLowerCase() === 'g') {
      this.img = this.jpgImg
    }
  },
  beforeCreate: function () {
    var post_url = get_url(this.$store.state.dev, '/resource/evaluation/grade/count/')
    var post_data = { resource_id: this.$store.state.id }
    var _this = this
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: post_url,
      type: 'POST',
      data: post_data,
      success: function (data) {
        var avg = data['avg_grade']
        var personal_grade = data['user_grade']
        _this.rate_count = data['grade_count']
        if (avg === -1) _this.public_rate = 0
        else _this.public_rate = avg
        if (personal_grade === -1) {
          _this.rate_disable = false
        } else {
          _this.rate = personal_grade
        }
      },
      error: function () {
        _this.$message({
          showClose: true,
          type: 'error',
          message: '无法连接到服务器'
        })
      }
    })
  }
}
</script>

<style scoped>
  .text{
    word-break: break-all;
    word-wrap: break-word;
    white-space: pre-wrap;
  }
</style>