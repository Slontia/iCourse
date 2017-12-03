<!-- Course_info page -->
<template>
  <div id="course_info">
    <Header></Header>
    <!-- course introduction -->
    <el-row :gutter="50" class="course_introduction">
        <el-col :span="18" >
            <el-button type="primary" icon = "d-arrow-left" @click="return_course_page_clicked" style="margin-top: 20px;margin-bottom: 10px">返回课程页面</el-button>
            <el-button type="primary" @click="enter_forum_clicked"style="float:right;margin-top: 20px; margin-bottom: 10px">进入课程论坛<i class="el-icon-d-arrow-right el-icon--right"></i></el-button>
          <div class="info_card">
            <el-card class="box-card">
            <div slot="header" class = "clearfix">
              <span style="line-height:36px;text-align: left;">
                <el-row>
                  <el-col :span="12">
                    <p style="padding-top:10px;font-size: xx-large;">{{ course_name }}</p>
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
              点击: {{ visit_count }}
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
            <el-col :span="10">
              <p style="float: left;font-size: x-large">课程资源</p>
            </el-col> 
            <el-col :span="2" :offset="9">
              <el-button type="primary" @click="check_all_resource_clicked" style="float: right;">
                查看全部
              </el-button>
            </el-col> 
            <el-col :span="2" :offset="1">
              <el-button type="primary" @click="uploadDialogVisible=true" style="float: right;">
                上传资源
              </el-button>
            </el-col> 
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
        <template v-for="(i,index) in total_resource_line">
              <el-row>
                <el-col :span="7" v-bind:style="{visibility:card_data[index][0].show}">
                  <el-col :span="24">
                  <el-button type="text" class="card_button" @click.native="card_clicked(index,0)">
                  <el-card :body-style="{ padding: '10px'} " class="card">
                    <el-row>
                      <el-col :span="4" style="">
                        <img :src="card_data[index][0].img" style="width: 50px; height:50px;"></img>
                      </el-col>
                      <el-col :span="16" :offset="2">
                        <el-row>
                          资源名：{{ card_data[index][0].title }}
                        </el-row>
                        <el-row>
                          上传者：{{card_data[index][0].uploader}}
                        </el-row>
                        <el-row>
                          下载次数：{{card_data[index][0].frequency}}
                        </el-row>
                      </el-col>
                    </el-row>
                  </el-card>
                </el-button>
                </el-col>
                </el-col>

                <el-col :span="7" :offset="1" v-bind:style="{visibility:card_data[index][1].show}">
                  <el-col :span="24">
                  <el-button type="text" class="card_button" @click.native="card_clicked(index,1)">
                  <el-card :body-style="{ padding: '10px'} " class="card">
                    <el-row>
                      <el-col :span="4" style="">
                        <img :src="card_data[index][1].img" style="width: 50px; height:50px;"></img>
                      </el-col>
                      <el-col :span="16" :offset="2">
                        <el-row>
                          资源名：{{card_data[index][1].title}}
                        </el-row>
                        <el-row>
                          上传者：{{card_data[index][1].uploader}}
                        </el-row>
                        <el-row>
                          下载次数：{{card_data[index][1].frequency}}
                        </el-row>
                      </el-col>
                    </el-row>
                  </el-card>
                </el-button>
                </el-col>
                </el-col>

                <el-col :span="7" :offset="1" v-bind:style="{visibility:card_data[index][2].show}">
                  <el-button type="text" class="card_button" @click.native="card_clicked(index,2)">
                  <el-card :body-style="{ padding: '10px'}" class="card">
                    <el-row>
                      <el-col :span="4" style="">
                        <img :src="card_data[index][2].img" style="width: 50px; height:50px;"></img>
                      </el-col>
                      <el-col :span="16" :offset="2">
                        <el-row>
                          资源名：{{card_data[index][2].title}}
                        </el-row>
                        <el-row>
                          上传者：{{card_data[index][2].uploader}}
                        </el-row>
                        <el-row>
                          下载次数：{{card_data[index][2].frequency}}
                        </el-row>
                      </el-col>
                    </el-row>
                  </el-card>
                </el-button>
                </el-col>
      </el-row>
    </template>
    </div>
  <el-dialog title="上传资源" :visible.sync="uploadDialogVisible" size="tiny">
      <el-form label-position="left">
        <el-form-item type="text" label="资源介绍" :label-width="form_label_width">
          <el-input v-model="resourceIntro" auto_complete="off" placeholder="请输入资源介绍"></el-input>
        </el-form-item>
        <el-form-item :label-width="form_label_width">
          <input type="file" value="" id="file">
        </el-form-item>     
      </el-form>  
      <span slot="footer" class="dialog-footer">
        <el-button @click="uploadDialogVisible=false">取 消</el-button>
        <el-button type="primary" @click.native="upload">上 传</el-button>
      </span>      
    </el-dialog>

  <!-- 资源具体信息dialog -->
  <el-dialog title="资源信息" :visible.sync="dialogVisible" v-if="dialogVisible" size="tiny">
      <ResourceDialog></ResourceDialog>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible=false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
  </el-dialog>
  </div>

</template>

<script type="text/javascript">
/* eslint-disable camelcase */
/* eslint-disable space-infix-ops */
import Header from '../general/Header.vue'
import DocImg from './../../assets/fileico/docx_win.png'
import PdfImg from './../../assets/fileico/pdf.png'
import PptImg from './../../assets/fileico/pptx_win.png'
import JpgImg from './../../assets/fileico/jpeg.png'
import ZipImg from './../../assets/fileico/zip.png'
import RarImg from './../../assets/fileico/rar.png'
import ResourceDialog from '../general/ResourceDialog.vue'
import $ from 'jquery'
// 请不要删除和get_url相关的行，如果你真的需要请告诉我下原因。by xindetai
import get_url from '../general/getUrl.js'

export default {
  name: 'course_info',
  components: { Header, ResourceDialog },
  beforeCreate () {
    this.dev = true
    var self = this
    var course_id = this.$route.params.course_id
    var post_url = (this.dev ? get_url('/course/course_info/') : '/course/course_info/')
    var postData = { 'course_id': course_id }
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: post_url,
      type: 'POST',
      data: postData,
      success: function (data) {
        var info = data['course_info']
        self.course_name = info['name']
        self.teacher = undefined
        self.academy = info['college_id']
        self.hours = info['hours']
        self.intro_info = undefined
        self.$store.state.course_code = info['course_code']
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
    /*
    // loading the contribution_list
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: get_url('')
    })
    */
    // loading the resource
  },
  data () {
    return {
      course_name: '',
      teacher: '',
      academy: '',
      hours: '',
      intro_info: '',
      visit_count: -1,
      history_contribution_data: [],
      latest_contribution_data: [],
      uploadDialogVisible: false,
      fileList: [],
      dev: true,
      total_resource_line: 3,
      dialogVisible: false,
      card_data: [
        [{ title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' },
         { title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' },
         { title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' }],
        [{ title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' },
         { title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' },
         { title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' }],
        [{ title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' },
         { title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' },
         { title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' }]
      ],
      img: { zip: ZipImg,
        pdf: PdfImg,
        ppt: PptImg,
        doc: DocImg,
        jpg: JpgImg,
        rar: RarImg
      }
    }
  },
  methods: {
    return_course_page_clicked: function () {
      this.$router.push({ path: '/course/' })
    },
    upload: function () {
      var formData = new FormData()
      var fileObj = document.getElementById('file').files[0]
      formData.append('file', fileObj)
      formData.append('name', fileObj.name)
      formData.append('only_url', false)
      formData.append('url', null)
      formData.append('intro', this.resourceIntro)
      formData.append('course_code', this.$store.state.course_code)
      $.ajax({
        url: '/resourceUpload/',
        type: 'POST',
        data: formData,
        async: true,
        cache: false,
        contentType: false,
        processData: false,
        success: function (rdata) {
          rdata = JSON.parse(rdata)
          if (rdata['error'] === 0) {
            alert('上传文件成功！')
          } else {
            alert('上传失败！' + rdata['error'])
          }
        },
        error: function () {
          alert('fail')
        }
      })
    },
    edit_course: function () {
      this.$message({
        showClose: true,
        message: '功能暂未开放，敬请期待'
      })
    },
    submitUpload () {
      this.$refs.upload.submit()
    },
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
    },
    check_all_resource_clicked: function () {
      this.$router.push({ path: 'resource/' })
    },
    enter_forum_clicked: function () {
      this.$router.push({ path: 'forum/' })
    },
    card_clicked (i, j) {
      console.log(this.card_data[i][j].id)
      this.$store.state.id = this.card_data[i][j].id
      var resourceDialogSelf = this
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: '/resource/information/',
        type: 'POST',
        async: false,
        data: {'resource_id': resourceDialogSelf.card_data[i][j].id},
        success: function (rdata) {
          resourceDialogSelf.$store.state.name = rdata['resource_info']['name']
          $.ajax({
            url: '/user/information/',
            type: 'POST',
            data: {id: rdata['resource_info']['upload_user_id']},
            async: false,
            success: function (data) {
              data = JSON.parse(data)
              resourceDialogSelf.$store.state.author = data['user_info']['username']
            },
            error: function () {
              alert('fail')
            }
          })
          // resourceDialogSelf.$store.state.author = rdata['resource_info']['upload_user_id']
          resourceDialogSelf.$store.state.size = rdata['resource_info']['size']
          resourceDialogSelf.$store.state.time = rdata['resource_info']['upload_time']
          resourceDialogSelf.$store.state.intro = rdata['resource_info']['intro']
          resourceDialogSelf.$store.state.url = rdata['resource_info']['url']
          resourceDialogSelf.dialogVisible = true
        },
        error: function () {
          alert('拉取资源信息失败')
        }
      })
    }
  },
  mounted () {
    var course_id = this.$route.params.course_id
    var postData = { 'course_id': course_id, 'number': this.total_resource_line }
    var self = this
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: '/resource/latest/',
      type: 'POST',
      data: postData,
      success: function (data) {
        var pos = 2 // pos of latest resource
        var info = data['result']
        for (var i = 0; i < info.length; i++) {
          self.card_data[i][pos].title=info[i]['name']
          self.card_data[i][pos].uploader=info[i]['username']
          self.card_data[i][pos].frequency=info[i]['download_count']
          self.card_data[i][pos].id = info[i]['resource_id']
          self.card_data[i][pos].show = 'visible'
          var name = info[i]['name'].toLowerCase()
          for (var t in self.img) {
            var temp = '.'+t+'$'
            var reg = new RegExp(temp)
            if (reg.test(name)) {
              self.card_data[i][pos].img = self.img[t]
              break
            }
          }
        }
      },
      error: function () {
        alert('拉取资源列表失败')
      }
    })
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
    background-color: #58B7FF;
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
  .text{
    padding-bottom: 5px;
  }
</style>