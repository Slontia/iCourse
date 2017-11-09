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
                  <el-col :span="12">
                    <p style="padding-top:30px;font-size: xx-large">{{ course_name }}</p>
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
    <el-upload class="upload-demo" ref="upload" action="https://jsonplaceholder.typicode.com/posts/" :on-preview="handlePreview" :on-remove="handleRemove" :file-list="fileList" :auto-upload="false">
      <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
      <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传</el-button>
      <div slot="tip" class="el-upload__tip">只能上传pdf/ppt/doc/txt/zip文件，且不超过10Mb</div>
    </el-upload>
    <span slot="footer" class="dialog-footer">
      <el-button @click="uploadDialogVisible=false">取 消</el-button>
      <el-button type="primary" @click="uploadDialogVisible = false">确 定</el-button>
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
    var self = this
    var course_id = this.$route.params.course_id
    var postData = { 'course_id': course_id }
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: get_url('/course/course_info/'),
      type: 'POST',
      data: postData,
      success: function (data) {
        var info = data['course_info']
        self.course_name = info['name']
        self.teacher = undefined
        self.academy = info['college_id']
        self.hours = info['hours']
        self.intro_info = undefined
      },
      error: function () {
        alert('fail')
      }
    })
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: get_url('/course/visit_count/'),
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
    edit_course: function () {},
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
    card_clicked (i, j) {
      console.log(this.card_data[i][j].id)
      this.$store.state.id = this.card_data[i][j].id
      var resourceDialogSelf = this
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: get_url('/resource/information/'),
        type: 'POST',
        async: false,
        data: {'resource_id': resourceDialogSelf.card_data[i][j].id},
        success: function (rdata) {
          resourceDialogSelf.$store.state.name = rdata['resource_info']['name']
          resourceDialogSelf.$store.state.author = rdata['resource_info']['upload_user_id']
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
      url: get_url('/resource/latest/'),
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
          for (var t in self.img) {
            var temp = '.'+t+'$'
            var reg = new RegExp(temp)
            if (reg.test(info[i]['name'])) {
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