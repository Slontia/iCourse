<!-- Course_info page -->
<template>
  <div id="course_info">
    <Header></Header>
    <!-- course introduction -->
    <el-row :gutter="50" class="course_introduction">
        <el-col :span="18" >
            <el-button type="primary" icon = "arrow-left" @click="return_course_page_clicked" style="margin-top: 20px">返回课程页面</el-button>
          <div class="info_card">
            <el-card class="box-card">
            <div slot="header" class = "clearfix">
              <span style="line-height:36px;text-align: left;">
                <el-row>
                  <el-col :span="8">
                    <p style="padding-top:30px;font-size: xx-large">{{ course_name }}</p>
                    <p>点击: {{ visit_count }}</p>
                  </el-col>
                  <el-col :span="10">
                    <img :src="img" width="100px" height="100px" style="float:right">
                  </el-col>
              </el-row>
              </span>
            </div>
            <div class="text item">
              授课教师: {{ teacher }}
            </div>
            <div class="text item">
              开课院系: {{ academy }}
            </div>
            <div class="text item">
              学时: {{ hours }}
            </div>
            <div class="text item">
              课程介绍: {{ intro_info }}
            </div>
            <div class="text item">
              <el-button type="text" icon="edit" @click="edit_course" style="float: right">我来补充</el-button>
            </div>
            </el-card>
          </div>     
        </el-col>

      <!-- contribution rank -->
      <el-col :span="6" class = "contribution_container">
        <div class="history_contribution_table">
        <p style="text-align: center; padding-bottom: 10px"> 历史贡献度排行 </p>
        <el-table :data="history_contribution_data" highlight-current-row style="width: auto;" height="300">
          <el-table-column prop="contribution_username" label="用户名"></el-table-column>
          <el-table-column prop="contribution_score" label="贡献度"></el-table-column>
          <el-table-column prop="contribution_level" label="等级"></el-table-column>
        </el-table>
        </div>
        <div class="month_contribution_table">
        <p style="text-align: center; padding-bottom: 10px"> 近一个月贡献度排行 </p>
        <el-table :data="latest_contribution_data" highlight-current-row style="width: auto;" height="300">
          <el-table-column prop="contribution_username" label="用户名"></el-table-column>
          <el-table-column prop="contribution_score" label="贡献度"></el-table-column>
          <el-table-column prop="contribution_level" label="等级"></el-table-column>
        </el-table>
      </div>
      </el-col>
    </el-row>
     <!-- course resource -->

     <div class = "course_resource_container">
      <hr style="margin-top: 20px;width:100%" />
        <el-row class="course_resource_head" style="margin-bottom: 20px">
          <el-col :span="24" style="margin-top: 20px">
            <p style="float: left;font-size: x-large">课程资源</p>
            <el-button type="primary" @click="check_all_resource_clicked" style="float: right;">
              查看全部
            </el-button>
          </el-col>
      </el-row>
        <el-row class = "resource_container" >
          <el-col :span="16" class="hot_resource_container">
              <p style="text-align: left;padding-bottom: 20px;font-size: large"> 热门资源 </p>
          </el-col>
            <el-col :span="8" class= "latest_resource_container" :offset="14">
              <p style="padding-bottom: 10px; font-size: large">最新资源</p>
          </el-col>
        </el-row>
              <el-row>
                <el-col :span="7" v-for="(o,index) in 2" :key="o" :offset="index>0?1:0">
                  <el-button type="text" class="card_button">
                  <el-card :body-style="{ padding: '10px'} " class="card">
                    <el-row>
                      <el-col :span="4" style="">
                        <img :src="img" style="width: 50px; height:50px;"></img>
                      </el-col>
                      <el-col :span="16" :offset="2">
                        <el-row>
                          CHAPTER{{ o }}
                        </el-row>
                        <el-row>
                          上传者:Aletheia
                        </el-row>
                        <el-row>
                          下载次数:11
                        </el-row>
                      </el-col>
                    </el-row>
                  </el-card>
                </el-button>
                </el-col>

                <el-col :span="7" v-for="(o,index) in 1" :key="o" :offset="1">
                  <el-button type="text" class="card_button">
                  <el-card :body-style="{ padding: '10px'}" class="card">
                    <el-row>
                      <el-col :span="4" style="">
                        <img :src="img" style="width: 50px; height:50px;"></img>
                      </el-col>
                      <el-col :span="16" :offset="2">
                        <el-row>
                          CHAPTER{{ o }}
                        </el-row>
                        <el-row>
                          上传者:Aletheia
                        </el-row>
                        <el-row>
                          下载次数:11
                        </el-row>
                      </el-col>
                    </el-row>
                  </el-card>
                </el-button>
                </el-col>
      </el-row>
    </div>
  </div>
</template>

<script type="text/javascript">
/* eslint-disable camelcase */
import Header from '../general/Header.vue'
import Img from '../../assets/pdf.png'
import $ from 'jquery'

export default {
  name: 'course_info',
  components: { Header },
  beforeCreate () {
    var self = this
    var postData = { 'course_id': this.$route.params.course_id }
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: '/course/course_info/',
      type: 'POST',
      data: postData,
      success: function (data) {
        var info = data['course_info']
        self.course_name = info['name']
        self.teacher = undefined
        self.academy = info['college_id']
        self.hours = info['hours']
        self.intro_info = undefined
        self.img = Img
      },
      error: function () {
        alert('fail')
      }
    })
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: '/course/visit_count/',
      type: 'POST',
      data: postData,
      success: function (data) {
        self.visit_count = data['visit_count']
      },
      error: function () {
        alert('点击次数链接异常')
      }
    })
  },
  data () {
    return {
      course_name: '软件工程基础',
      teacher: '罗杰',
      academy: '计算机学院',
      hours: '32',
      intro_info: '计算机学院开设的软件工程课',
      visit_count: -1,
      img: Img,
      history_contribution_data: [],
      latest_contribution_data: []
    }
  },
  methods: {
    return_course_page_clicked: function () {
      this.$router.push({ path: '/course/' })
    },
    edit_course: function () {},
    check_all_resource_clicked: function () {
      this.$router.push({ path: 'resource/' })
    }
  }
}
</script>


<style type="text/css" scoped>
  .course_introduction{
    margin-top: 10px;
    padding-left: 20px;
    height: 70%;
    width: 100%;
  }
  .contribution_container{
    position:absolute;
    left:75%;
    margin-left: 10px;
  }
  .history_contribution_table{
    margin-bottom: 50px;
  }
  .course_resource_container{
    position:absolute;
    top:400px;
    margin-top: 20px;
    padding-left: 20px;
    width: 71%;
  }
  .resource_container{
    widht:auto;
  }
  .hot_resource_container{
    width:auto;
  }
  .latest_resource_container{
    width: auto;
  }
  .card:hover{
    background-color: #409EFF;
  }
  .card_button{
    padding-top:0px;
    margin-top:0px;
    border:0px;
    width:100%;
    height:100%;
    text-align:left;
    color: black;
  }
</style>