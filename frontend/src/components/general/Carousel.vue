<template>
  <div id="Carousel" class="carousel">
    <h2 class="demonstration">北 航 课 程 资 源 下 载 站</h2>
    <el-row type="flex" justify="center" class="academy_selection_container">
      <el-col :span="6" :offset="17">
        <el-select v-model="academy" placeholder="选择系别来查看不同的内容~" @change="handle_selection_change" >
          <el-option v-for="item in academies" :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-col :span="16">
    <el-tabs v-model="active_post_type" class="tab" type="card" @tab-click="handle_tab_clicked">
      <el-tab-pane name="hot_post">
        <span slot="label" class="tab_pane">热门帖子</span>
        <template v-for="thread in hot_threads">
          <el-row type="flex" justify="center" class="thread_container">
          <el-col :span="6">
          <el-row>
            <el-col :span="8">
              <p class="thread_info_num" style="color:#58B7FF">{{ thread.agree_num }}</p>
            </el-col>
            <el-col :span="8">
              <p class="thread_info_num" style="color:rgb(80,80,80)">{{ thread.follow_num }}</p>
            </el-col>
            <el-col :span="8">
              <p class="thread_info_num" style="color:grey">{{ thread.read_num }}</p>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="8">
              <p class="thread_info_term" style="color:#58B7FF">赞同</p>
            </el-col>
            <el-col :span="8">
              <p class="thread_info_term" style="color:rgb(80,80,80)">跟帖</p>
            </el-col>
            <el-col :span="8">
              <p class="thread_info_term" style="color:grey">浏览</p>
            </el-col>
          </el-row>
        </el-col>
        <el-col :span="16" :offset="1">
          <el-row style="padding:10px 0px 0px 0px;">
            <el-button type="text" class="title_button" @click="enter_thread_button_clicked(thread.id)">
            <p style="">
              <span style="">{{ thread.type }} ·</span>
              <span style="">{{ thread.title }}</span>
            </p>
          </el-button>
          </el-row>
          <el-row style="padding-bottom: 10px;">
            <p class="thread_description"> {{ thread.description }} </p>
          </el-row>
        </el-col>
      </el-row>
      <el-row>
       <el-col :span="16" :offset="1">
        <el-button type="text" @click="course_name_clicked(thread.course_id)"> 
       <el-col :span="16" :offset="1">
        <p style="color:#58B7FF" @click="course_name_clicked(thread.course_id)"> {{ thread.course_name }} </p>
       </el-col>
        </el-button>
        </el-col>
      </el-row>
      <center><hr width="90%"style="margin-top: 20px; border: none;border-top: 1px solid rgb(241,242,244)"/></center>
      </template>
      </el-tab-pane>
      <el-tab-pane name="new_post">
        <span slot="label" class="tab_pane">最新帖子</span>
        <template v-for="thread in new_threads">
          <el-row type="flex" justify="center" class="thread_container">
          <el-col :span="6">
          <el-row>
            <el-col :span="8">
              <p class="thread_info_num" style="color:#58B7FF">{{ thread.agree_num }}</p>
            </el-col>
            <el-col :span="8">
              <p class="thread_info_num" style="color:rgb(80,80,80)">{{ thread.follow_num }}</p>
            </el-col>
            <el-col :span="8">
              <p class="thread_info_num" style="color:grey">{{ thread.read_num }}</p>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="8">
              <p class="thread_info_term" style="color:#58B7FF">赞同</p>
            </el-col>
            <el-col :span="8">
              <p class="thread_info_term" style="color:rgb(80,80,80)">跟帖</p>
            </el-col>
            <el-col :span="8">
              <p class="thread_info_term" style="color:grey">浏览</p>
            </el-col>
          </el-row>
        </el-col>
        <el-col :span="16" :offset="1">
          <el-row style="padding:10px 0px 0px 0px;">
            <el-button type="text" class="title_button" @click="enter_thread_button_clicked(thread.id)">
            <p style="">
              <span style="">{{ thread.type }} ·</span>
              <span style="">{{ thread.title }}</span>
            </p>
          </el-button>
          </el-row>
          <el-row style="padding-bottom: 10px;">
            <p class="thread_description"> {{ thread.description }} </p>
          </el-row>
        </el-col>
      </el-row>
      <el-row>
       <el-col :span="16" :offset="1">
        <p style="color:#58B7FF" @click="course_name_clicked(thread.course_id)"> {{ thread.course_name }} </p>
       </el-col>
      </el-row>
      <center><hr width="90%"style="margin-top: 20px; border: none;border-top: 1px solid rgb(241,242,244)"/></center>
      </template>
      </el-tab-pane>
    </el-tabs>
  </el-col>

  <el-col :span="1">
  <hr style="height:90%;margin:100px 0px 0px 20px;width:1px;border: none;border-left: 1px solid #ccc">
  </el-col>
  <el-col :span="6">
    <el-tabs v-model="active_resource_type" class="tab" type="card" @tab-click="handle_tab_clicked">
      <el-tab-pane name="hot_resource">
        <span slot="label" class="tab_pane">热门资源</span>
        <template v-for="resource in hot_resources">
      <el-row>
      <el-col :span="24" :offset="0">
        <el-tooltip effect="dark" :content="resource.name" placement="left">
                  <el-button type="text" class="card_button" @click.native="resource_button_clicked(resource.id)">
                        <el-row>
                          <el-col :span="24">
                            
                          <p class="card_title_text"><i class="el-icon-document"></i> {{ resource.name }}</p>
                        </el-col>
                        <!--
                        <el-col :span="2" :offset="10">
                        <p class="card_title_text">
                          下载:{{ resource.download_count}}
                        </p>
                      </el-col>
                    -->
                        </el-row>
                </el-button>
              </el-tooltip>
              <hr style="border: none;border-top: 1px solid rgb(241,242,244)"/>
                </el-col>
      </el-row>
      </template>
      </el-tab-pane>
      <el-tab-pane name="new_resource">
        <span slot="label" class="tab_pane">最新资源</span>
        <template v-for="resource in new_resources">
      <el-row>
      <el-col :span="24" :offset="0">
        <el-tooltip effect="dark" :content="resource.name" placement="left">
                  <el-button type="text" class="card_button" @click.native="resource_button_clicked(resource.id)">
                        <el-row>
                          <el-col :span="24">
                            
                          <p class="card_title_text"><i class="el-icon-document"></i> {{ resource.name }}</p>
                        </el-col>
                        <!--
                        <el-col :span="2" :offset="10">
                        <p class="card_title_text">
                          下载:{{ resource.download_count}}
                        </p>
                      </el-col>
                    -->
                        </el-row>
                </el-button>
              </el-tooltip>
              <hr style="border: none;border-top: 1px solid rgb(241,242,244)"/>
                </el-col>
      </el-row>
      </template>
      </el-tab-pane>
    </el-tabs>
  </el-col>
  </el-row>
  <el-dialog title="资源信息" :visible.sync="dialogVisible" v-if="dialogVisible" size="small">
      <ResourceDialog></ResourceDialog>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible=false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
  </el-dialog>
    <!--
    <el-carousel :intervel="carousel_interval" height="600px" arrow="never">
      <el-carousel-item :key="de1">
        <img :src="carousel_image1" height="100%" width="100%">
      </el-carousel-item>
    </el-carousel>
    -->
    
  </div>
  </div>
</template>

<script type="text/javascript">
/* eslint-disable camelcase */
// import carousel_image1 from '../../assets/carousel_image.jpg'
import $ from 'jquery'
import get_url from './getUrl.js'
import ResourceDialog from './ResourceDialog.vue'
export default {
  name: 'Carousel',
  components: { ResourceDialog },
  mounted () {
    this.get_hot_post(10, -1)
    this.get_new_post(10, -1)
    this.get_hot_resource(10, -1)
    this.get_new_resource(10, -1)
  },
  data () {
    return {
      active_post_type: 'hot_post',
      active_resource_type: 'hot_resource',
      academy: '',
      dialogVisible: false,
      academies: [
                    { label: '全部', value: -1 },
                    { label: '材料科学与工程学院', value: 1 },
                    { label: '电子信息工程学院', value: 2 },
                    { label: '自动化科学与电气工程学院', value: 3 },
                    { label: '能源与动力工程学院', value: 4 },
                    { label: '航空科学与工程学院', value: 5 },
                    { label: '计算机学院', value: 6 },
                    { label: '机械工程及自动化学院', value: 7 },
                    { label: '经济管理学院', value: 8 },
                    { label: '数学与系统科学学院', value: 9 },
                    { label: '生物与医学工程学院', value: 10 },
                    { label: '人文社会科学学院', value: 11 },
                    { label: '外国语学院', value: 12 },
                    { label: '交通科学与工程学院', value: 13 },
                    { label: '可靠性与系统工程学院', value: 14 },
                    { label: '宇航学院', value: 15 },
                    { label: '飞行学院', value: 16 },
                    { label: '仪器科学与光电工程学院', value: 17 },
                    { label: '物理科学与核能工程学院', value: 19 },
                    { label: '法学院', value: 20 },
                    { label: '软件学院', value: 21 },
                    { label: '现代远程教育学院', value: 22 },
                    { label: '高等工程学院', value: 23 },
                    { label: '中法工程师学院', value: 24 },
                    { label: '国际学院', value: 25 },
                    { label: '新媒体艺术与设计学院', value: 26 },
                    { label: '化学与环境学院', value: 27 },
                    { label: '思想政治理论学院', value: 28 },
                    { label: '人文与社会科学高等研究院', value: 29 },
                    { label: '30系', value: 30 },
                    { label: '32系', value: 32 },
                    { label: '33系', value: 33 },
                    { label: '51系', value: 51 },
                    { label: '52系', value: 52 },
                    { label: '56系', value: 56 },
                    { label: '91系', value: 91 }
      ],
      new_threads: [],
      hot_threads: [],
      new_resources: [],
      hot_resources: [],
      current_value: -1
    }
  },
  methods: {
    course_name_clicked: function (course_id) {
      this.$router.push({ path: '/course/page/' + course_id + '/' })
    },
    handle_tab_clicked: function (tab, event) {
    },
    enter_thread_button_clicked: function (value) {
      this.$router.push({ path: '/forum/' + value + '/' })
    },
    resource_button_clicked: function (value) {
      console.log(value)
      this.$store.state.id = value
      var resourceDialogSelf = this
      var post_url = get_url(this.$store.state.dev, '/resource/information/')
      var _this = this
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: post_url,
        type: 'POST',
        async: false,
        data: {'resource_id': value},
        success: function (rdata) {
          resourceDialogSelf.$store.state.name = rdata['resource_info']['name']
          post_url = get_url(_this.$store.state.dev, '/user/information/')
          $.ajax({
            url: post_url,
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
    },
    handle_selection_change: function (value) {
      if (value !== this.current_value) {
        this.hot_threads = []
        this.new_threads = []
        this.hot_resources = []
        this.new_resources = []
        this.get_hot_post(10, value)
        this.get_new_post(10, value)
        this.get_hot_resource(10, value)
        this.get_new_resource(10, value)
        this.current_value = value
      }
    },
    get_hot_post: function (len, value) {
      var post_url = get_url(this.$store.state.dev, '/post/hot/idlist/')
      var post_data = { list_len: len, college_id: value }
      var _this = this
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: post_url,
        type: 'POST',
        data: post_data,
        success: function (data) {
          var id_list = data['id_list']
          if (id_list.length !== 0) {
            post_data = { id_list: JSON.stringify(id_list), get_content: true, get_grade: true, get_follow_count: true }
            post_url = get_url(_this.$store.state.dev, '/post/information/list/')
            $.ajax({
              ContentType: 'application/json; charset=utf-8',
              dataType: 'json',
              url: post_url,
              type: 'POST',
              data: post_data,
              success: function (data) {
                var info_list = data['info_list']
                for (var i = 0; i < info_list.length; i++) {
                  var type = (info_list[i].category === 1 ? '问题讨论' : (info_list[i].category === 2 ? '学习心得' : '其他'))
                  var cut_description = (info_list[i].intro.length < 100 ? info_list[i].intro : info_list[i].intro.substr(0, 100)) + '....'
                  var thread = { id: id_list[i], agree_num: info_list[i].grade_sum, follow_num: info_list[i].follow_count, read_num: info_list[i].click_count, type: type, title: info_list[i].title, description: cut_description, course_name: info_list[i].course_name, course_id: info_list[i].course_id }
                  _this.hot_threads.push(thread)
                }
              },
              error: function () {
                _this.$message({
                  showClose: true,
                  type: 'error',
                  message: '获取帖子信息失败'
                })
              }
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
    },
    get_new_post: function (len, value) {
      var post_url = get_url(this.$store.state.dev, '/post/latest/idlist/')
      var post_data = { list_len: len, college_id: value }
      var _this = this
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: post_url,
        type: 'POST',
        data: post_data,
        success: function (data) {
          var id_list = data['id_list']
          if (id_list.length !== 0) {
            post_data = { id_list: JSON.stringify(id_list), get_content: true, get_grade: true, get_follow_count: true }
            post_url = get_url(_this.$store.state.dev, '/post/information/list/')
            $.ajax({
              ContentType: 'application/json; charset=utf-8',
              dataType: 'json',
              url: post_url,
              type: 'POST',
              data: post_data,
              success: function (data) {
                var info_list = data['info_list']
                for (var i = 0; i < info_list.length; i++) {
                  var type = (info_list[i].category === 1 ? '问题讨论' : (info_list[i].category === 2 ? '学习心得' : '其他'))
                  var cut_description = (info_list[i].intro.length < 100 ? info_list[i].intro : info_list[i].intro.substr(0, 100)) + '....'
                  var thread = { id: id_list[i], agree_num: info_list[i].grade_sum, follow_num: info_list[i].follow_count, read_num: info_list[i].click_count, type: type, title: info_list[i].title, description: cut_description, course_name: info_list[i].course_name, course_id: info_list[i].course_id }
                  _this.new_threads.push(thread)
                }
              },
              error: function () {
                _this.$message({
                  showClose: true,
                  type: 'error',
                  message: '获取帖子信息失败'
                })
              }
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
    },
    get_new_resource: function (len, value) {
      var post_url = get_url(this.$store.state.dev, '/resource/upload/latest/')
      var post_data = { number: len, college_id: value }
      var _this = this
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: post_url,
        type: 'POST',
        data: post_data,
        success: function (data) {
          var info_list = data['result']
          if (info_list.length !== 0) {
            for (var i = 0; i < info_list.length; i++) {
              var resource = {}
              resource.id = info_list[i].resource_id
              resource.username = info_list[i].username
              resource.download_count = info_list[i].download_count
              resource.name = info_list[i].name
              _this.new_resources.push(resource)
            }
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
    },
    get_hot_resource: function (len, value) {
      var post_url = get_url(this.$store.state.dev, '/resource/download/most/')
      var post_data = { number: len, college_id: value }
      var _this = this
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: post_url,
        type: 'POST',
        data: post_data,
        success: function (data) {
          var info_list = data['result']
          if (info_list.length !== 0) {
            for (var i = 0; i < info_list.length; i++) {
              var resource = {}
              resource.id = info_list[i].resource_id
              resource.username = info_list[i].username
              resource.download_count = info_list[i].download_count
              resource.name = info_list[i].name
              _this.hot_resources.push(resource)
            }
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
}
</script>

<style type="text/css" scoped>
  .thread_container{
    margin-top: 30px;
    height: auto;
  }
  .thread_info_num{
    text-align: center;
    font-size: 24px;
    padding-bottom: 10px;
    padding-top: 0px;
    margin-top: 0px;
  }
  .thread_info_term{
    text-align: center;
    font-size: 24px;
  }
    .title_button{
    padding: 0px 0px 0px 0px;
    margin: 0px 0px 0px 4px;
    color:black;
    font-size: 24px;
    word-wrap: break-word;
    word-break:break-all;
    white-space: pre-wrap;
  }
    .title_button:hover{
    color: #58B7FF;
    text-decoration: underline;
  }
  .carousel{
    top:60px;
    margin-top: 20px;
    width: 100%;
  }
  .demonstration{
    font-size: 30px;
    font-weight: 100;
    font-family: Microsoft Yahei;
    text-align: center;
    margin-bottom: 10px;
    margin: 0px,0px,10px,0px;
    color:#20a0ff;
  }
    .thread_description{
    padding-top: 20px;
    color: grey;
    white-space: pre-wrap;
    word-break: break-all;
    word-wrap:break-word;
  }
  .academy_selection_container{
    margin-bottom: 20px;
  }
  .tab_pane{
    font-size: 20px;
  }
  .card_title_text{
    font-size: 14px;
  }
  .course_name{
    font-size: 18px;
  }
</style>