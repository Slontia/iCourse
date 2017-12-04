<template>
  <div id='forum' class='container'>
    <Header></Header>
    <el-row>
      <el-col :span="24">
        <el-button type="primary" icon="d-arrow-left" style="margin:20px 0px 0px 20px" @click="return_course_button_clicked">返回课程页面
        </el-button>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
        <p class="title">
          {{ course_name }}-讨论版
        </p>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="9" :offset="3">
        <el-radio-group v-model="selected_filter" @change="handle_filter_change">
          <template v-for="term in search_terms">
            <el-radio-button class="button_group_static" :label="term.text">
              {{ term.text }}
            </el-radio-button>
          </template>
        </el-radio-group>
      </el-col>
      <el-col :span="3" :offset="3">
        <el-button type="primary" @click="post_button_clicked" icon="plus" style="width:150px;">
          发表新帖子
        </el-button>
      </el-col>
      <el-col :span="4" :offset="0">
        <el-input type="text" v-model = "search_text" placeholder="在当前条目下搜索" @keydown.enter.native.prevent="search_button_clicked" icon="search" :on-icon-click="search_button_clicked"></el-input>
      </el-col>
    </el-row>
    <template v-for="thread in current_threads">
      <el-row type="flex" justify="center" class="thread_container">
        <el-col :span="4">
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
        <el-col :span="14" :offset="1">
          <el-row style="padding-bottom: 10px;">
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
          <el-row>
            <p style="float: right;color:grey"> {{ thread.user_name }} 最后编辑于 {{ thread.time }}</p>
          </el-row>
        </el-col>
      </el-row>
      <center><hr width="80%"/></center>
    </template>
    <el-row type="flex" justify="center">
      <el-col :span="18">
      <center><el-pagination layout="prev,pager,next" @current-change="handle_current_change" :page-size="page_size" :total="total_threads" :current-page.sync="current_page" style="margin-top: 40px"></el-pagination>
      </center>
    </el-col>
    </el-row>
  </div>
</template>

<script type="text/javascript">
/* eslint-disable brace-style */
/* eslint-disable camelcase */
/* eslint-disable space-infix-ops */
import Header from '../general/Header'
import get_url from '../general/getUrl.js'
import $ from 'jquery'
export default {
  name: 'Forum',
  components: { Header },
  beforeCreate () {
    this.dev = true
    this.page_size = 10
    var post_url = get_url(this.dev, '/post/id/list/')
    var post_data = { course_id: this.$route.params.course_id }
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
          _this.total_threads = id_list.length
          var len = (id_list.length > _this.page_size ? _this.page_size : id_list.length)
          var target_list = id_list.slice(0, len)
          for (var j = 0; j < id_list.length; j++) {
            _this.threads.push(id_list[j])
          }
          post_data = { id_list: target_list, get_content: true, get_grade: true, get_follow_count: true }
          post_url = get_url(_this.dev, '/post/information/list/')
          $.ajax({
            ContentType: 'application/json; charset=utf-8',
            dataType: 'json',
            url: post_url,
            type: 'POST',
            data: post_data,
            success: function (data) {
              var info_list = data['info_list']
              for (var i = 0; i < info_list.length; i++) {
                var type = (info_list[i].type === 1 ? '问题讨论' : (info_list[i].type === 2 ? '学习心得' : '其他'))
              // need to cut description
                var cut_description = (info_list[i].content.length < 100 ? info_list[i].content : info_list[i].content.substr(0, 100))
                var thread = { id: id_list[i], agree_num: info_list[i].grade_sum, follow_num: info_list[i].follow_count, read_num: info_list[i].read_count, type: type, title: info_list[i].title, description: cut_description, user_name: info_list[i].username, time: info_list[i].update_time }
                _this.current_threads.push(thread)
              }
            },
            error: function () {
              _this.$message({
                showClose: true,
                type: 'error',
                message: '加载帖子信息失败'
              })
            }
          })
        }
      },
      error: function () {
        _this.$message({
          showClose: true,
          type: 'error',
          message: '加载帖子列表失败'
        })
      }
    })
    post_data = { 'course_id': this.$route.params.course_id }
    post_url = get_url(this.dev, '/course/course_info/')
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: post_url,
      type: 'POST',
      data: post_data,
      success: function (data) {
        var info = data['course_info']
        _this.course_name = info.name
      },
      error: function () {
        _this.message({
          showClose: true,
          type: 'error',
          message: '获取课程信息失败'
        })
      }
    })
  },
  data () {
    return {
      course_name: '',
      total_threads: 0,
      page_size: 10,
      current_page: 1,
      selected_filter: '全部',
      search_text: '',
      current_threads: [
        { id: '0001', agree_num: 12, follow_num: 5, read_num: 100, type: '学习心得', title: '关于最大团问题的典型解法', description: '很惭愧，一点微小的工作', user_name: '果冻', time: '2017-11-29' },
        { id: '0002', agree_num: 11, follow_num: 3, read_num: 110, type: '问题讨论', title: '如何评论最近上线的BUAA-iCourse?', description: '如题', user_name: 'Aletheia', time: '2017-11-29' }
      ],
      threads: [],
      search_terms: [
        { text: '全部' },
        { text: '学习心得' },
        { text: '问题讨论' },
        { text: '其他' }
      ],
      thread_terms: [ '赞同', '跟帖', '浏览' ]

    }
  },
  methods: {
    return_course_button_clicked: function () {
      this.$router.push({ path: '/course/page/'+this.$route.params.course_id+'/' })
    },
    search_button_clicked: function () {
      this.$message({
        showClose: true,
        message: '尚未开放，敬请期待'
      })
    },
    handle_current_change: function (value) {
      this.current_page = value
      this.current_threads = []
      var len = this.threads.length < value*this.page_size ? this.threads.length % this.page_size : this.page_size
      var target_list = []
      for (var j = 0; j < len; j++) {
        target_list.push(this.threads[(value-1)*this.page_size+j])
      }
      var post_data = { id_list: target_list, get_content: true, get_grade: true, get_follow_count: true }
      var post_url = get_url(this.dev, '/post/information/list/')
      var _this = this
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: post_url,
        type: 'POST',
        data: post_data,
        success: function (data) {
          var info_list = data['info_list']
          for (var i = 0; i < info_list.length; i++) {
            var type = (info_list[i].type === 1 ? '问题讨论' : (info_list[i].type === 2 ? '学习心得' : '其他'))
              // need to cut description
            var cut_description = (info_list[i].content.length < 100 ? info_list[i].content : info_list[i].content.substr(0, 100))
            var thread = { id: target_list[i], agree_num: info_list[i].grade_sum, follow_num: info_list[i].follow_count, read_num: info_list[i].read_count, type: type, title: info_list[i].title, description: cut_description, user_name: info_list[i].username, time: info_list[i].update_time }
            _this.current_threads.push(thread)
          }
        },
        error: function () {
          _this.$message({
            showClose: true,
            type: 'error',
            message: '加载帖子信息失败'
          })
        }
      })
    },
    handle_filter_change: function (value) {
      // handle the filter changing of thread
    },
    enter_thread_button_clicked: function (value) {
      console.log(value)
    },
    post_button_clicked: function () {
      if (this.$store.state.is_login === true) {
        this.$router.push({path: '/course/page/' + this.$route.params.course_id + '/forum/new'})
      }
      else {
        this.$message({
          message: '请先登录再发帖',
          showClose: true,
          type: 'warning'
        })
      }
    }
  }
}
</script>

<style type="text/css" scoped>
  .container{
    font-family: Microsoft Yahei;
  }
  .title{
    text-align: center;
    font-size: 40px;
    padding-bottom: 30px;
  }
  .button_group_static{
    text-align: center;
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
    margin: 4px 0px 0px 4px;
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
  .thread_container{
    margin-top: 30px;
    height: auto;
  }
  .thread_description{
    color: grey;
    white-space: pre-wrap;
    word-break: break-all;
    word-wrap:break-word;
  }
</style>