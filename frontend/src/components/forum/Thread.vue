<template>
  <div id="thread" class="container">
    <Header></Header>
    <el-row>
      <el-col :span="24">
        <el-button type="primary" icon="d-arrow-left" style="margin:20px 0px 0px 20px" @click="return_forum_button_clicked">返回论坛主页面
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
    <center><hr width="80%"/></center>
    <!-- question or passage -->
    <el-row type="flex" justify="center" class="main_container">
      <el-col :span="2">
        <el-row>
          <center>
          <el-button type="text" icon="caret-top" size="large" class = "arrow_button" @click="agree_button_clicked(true,1,main.id,-1)"></el-button>
        </center>
        </el-row>
        <el-row>
          <center>
            <p class="agree_num">{{ main.agree_num }}</p>
          </center>
        </el-row>
        <el-row>
          <center>
          <el-button type="text" icon="caret-bottom" size="large" class="arrow_button" @click="agree_button_clicked(true,-1,main.id,-1)"></el-button>
        </center>
        </el-row>
      </el-col>
      <el-col :span="16">
        <el-row class="main_title_container">
          <p><span class="main_title">{{ main.title }}</span>
          <el-button type="primary" size="large" @click="edit_comment_button_clicked" style="float:right">编辑/添加回复
          </el-button>
          </p>
        </el-row>
        <el-row class="info_row">
          <el-col :span="2">
            <img :src="main.avatar" class="avatar"></el-col>
          <el-col :span="18">
            <el-row>
              <p class="user_name">{{ main.user_name}}</p>
            </el-row>
            <el-row>
              <p class="self_intro">{{ main.self_intro}}</p>
            </el-row>
          </el-col>
        </el-row>
        <el-row>
          <p class="content">{{ main.content }}</p>
        </el-row>
        <el-row class="footer_row">
          <el-button type="text" class="comment_button" @click="main_comment_button_clicked"> 评论({{ main.comment_num }})</el-button>
          <span class="time">最后编辑于{{ main.time }}</span>
        </el-row>
      </el-col>
    </el-row>
    <!-- main comment -->
    <el-row class="comment" v-bind:style="main.comment_active">
      <template v-for="comment in main.comments">
        <el-row type="flex" justify="center" class="comment_row">
          <el-col :span="18" :offset="4">
          <p>
            <span> {{ comment.user_name }} :</span>
            <span> {{ comment.content }}</span>
          </p>
        </el-col>
        </el-row>
        <center>
          <hr width="60%" style="height:0px;border:none;border-top: 1px dotted grey;margin:5px 0px 10px 0px;" />
        </center>
      </template>
      <el-row type="flex" justify="center" class="comment_input">
          <el-col :span="12" :offset="0">
        <el-input v-model="main.input_comment" placeholder="使用评论来获得更多信息或者提出修改意见，回答问题请直接回复"></el-input>
          </el-col>
          <el-col :span="2">
            <el-button type="primary" @click="main_input_comment_button_clicked">评论</el-button>
          </el-col>
        </el-row>
    </el-row>
    <!-- response -->
    <el-row class="response_info_row">
      <p class="response_info">
        共 {{ response_num }} 个回答
      </p>
    </el-row>
    <center>
      <hr width="80%" style="height:0px;border:none;border-top:2px solid grey; margin:10px 0px 20px 0px;" />
    </center>
    <template v-for="(response,index) in responses">
      <el-row type="flex" justify="center">
        <el-col :span="2">
        <el-row>
          <center>
          <el-button type="text" size="large" icon="caret-top" class="arrow_button" @click="agree_button_clicked(false,1,response.id,index)"></el-button>
        </center>
        </el-row>
        <el-row>
          <center>
            <p class="agree_num">{{ response.agree_num }}</p>
          </center>
        </el-row>
        <el-row>
          <center>
          <el-button type="text" size="large" icon="caret-bottom" class="arrow_button" @click="agree_button_clicked(false,-1,response.id,index)"></el-button>
        </center>
        </el-row>
        </el-col>
        <el-col :span="16">
          <el-row class="info_row">
          <el-col :span="2">
            <img :src="response.avatar" class="avatar"></el-col>
          <el-col :span="18">
            <el-row>
              <p class="user_name">{{ response.user_name}}</p>
            </el-row>
            <el-row>
              <p class="self_intro">{{ response.self_intro}}</p>
            </el-row>
          </el-col>
        </el-row>
        <el-row>
          <p class="content">{{ response.content }}</p>
        </el-row>
        <el-row class="footer_row">
          <el-button type="text" class="comment_button" @click="response_comment_button_clicked(index)"> 评论({{ response.comment_num }})</el-button>
          <span class="time">最后编辑于{{ response.time }}</span>
        </el-row>
        </el-col>
      </el-row>
      <!-- response comment -->
      <el-row class="comment" v-bind:style="response.comment_active">
      <template v-for="comment in response.comments">
        <el-row type="flex" justify="center" class="comment_row">
          <el-col :span="18" :offset="4">
          <p>
            <span> {{ comment.user_name }} :</span>
            <span> {{ comment.content }}</span>
          </p>
        </el-col>
        </el-row>
        <center>
          <hr width="60%" style="height:0px;border:none;border-top: 1px dotted grey;margin:5px 0px 10px 0px;" />
        </center>
      </template>
      <el-row type="flex" justify="center" class="comment_input">
          <el-col :span="12" :offset="0">
        <el-input v-model="response.input_comment" placeholder="使用评论来获得更多信息或者提出修改意见，回答问题请直接回复"></el-input>
          </el-col>
          <el-col :span="2">
            <el-button type="primary" @click="response_input_comment_button_clicked(index)">评论</el-button>
          </el-col>
        </el-row>
      </el-row>
      <center>
      <hr width="80%" style="margin-bottom: 20px;"/>
      </center>
    </template>
    
    <center>
    <el-button class="bar" type="text" v-bind:style="more_comment_button_style" @click="load_more_responses_button_clicked">
      <p class="all_text">查看全部{{response_num}}条回复</p>
    </el-button>
    </center>
    
    <!-- editor -->
    <el-row type="flex" justify="center" class="response_info_row">
      <el-col :span="20">
        <p style="text-align: left; margin-bottom: 20px;">发表你的看法</p>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center" >
      <el-col :span="20" class="editor_container">
      <quill-editor v-model="editor.content" ref="quill" class="editor" :options="editor.option" @change="on_editor_change">
      </quill-editor>
    </el-col>
    </el-row>
    <el-row type="flex" justify="center" >
      <el-col :span="20" class="limit">
        已经输入<span> {{ editor.current_text_length }} </span>个字符，还可以输入<span> {{ editor.current_available_text }} </span>个字符
      </el-col>
    </el-row>
    <el-row type="flex">
      <el-col :span="22">
        <el-button type="primary" @click="post_submit_button_clicked" class="submit_button" size="large">
          提交
        </el-button>
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
import default_img from '../../assets/headportrait.jpg'
import $ from 'jquery'
export default {
  name: 'Thread',
  components: { Header },
  mounted () {
    // todo:load thread and course name,
    this.dev = true
    this.response_page_size = 10
    var post_url = (this.dev ? get_url('/follow/id/list/') : '/follow/id/list/')
    var post_data = { post_id: this.$route.params.thread_id }
    var _this = this
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: post_url,
      type: 'POST',
      data: post_data,
      success: function (data) {
        var main_id = data['main_id']
        var id_list = data['id_list']
        _this.response_num = id_list.length
        _this.more_comment_button_style.display = (id_list.length > _this.response_page_size ? 'inline' : 'none')
        for (var i = 0; i < id_list.length; i++) {
          _this.responses_list.push(id_list[i])
        }
        var len = (id_list.length > _this.response_page_size ? _this.response_page_size : id_list.length)
        var target_list = id_list.slice(0, len)
        target_list.unshift(main_id)
        post_url = (_this.dev ? get_url('/follow/info/list/') : '/follow/info/list/')
        post_data = { id_list: target_list }
        if (main_id !== -1) {
          $.ajax({
            ContentType: 'application/json; charset=utf-8',
            dataType: 'json',
            url: post_url,
            type: 'POST',
            data: post_data,
            success: function (data) {
              var info_list = data['info_list']
              // load main
              _this.main.id = target_list[0]
              _this.main.title = '' // need to add
              _this.main.agree_num = 0 // need to add
              _this.main.user_name = info_list[0].username
              _this.main.self_intro = '' // need
              _this.main.avatar = default_img // need
              _this.main.content = info_list[0].content
              _this.main.time = String(info_list[0].edit_time)
              _this.main.comment_active = {}
              _this.main.comment_active.display = 'none'
              _this.main.input_comment = ''
              for (var j = 1; j < info_list.length; j++) {
                var temp = {}
                temp.id = target_list[j]
                temp.agree_num = 0 // need
                temp.user_name = info_list[j].username
                temp.self_intro = '' // need
                temp.avatar = default_img // need
                temp.content = info_list[j].content
                temp.time = String(info_list[j].edit_time)
                temp.comment_active = {}
                temp.comment_active.display = 'none'
                temp.input_comment = ''
                _this.responses.push(temp)
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
        else {
          _this.$message({
            showClose: true,
            type: 'error',
            message: '帖子不存在，大兄弟不要乱输域名'
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
    // todo: load comments
    /*
                { id: -1, agree_num: 10, title: '如何评论最近上线的BUAA-iCourse?', user_name: 'Aletheia', self_intro: 'buaa-icourse', avatar: default_img, content: '如题，感觉很厉害的样子', comments: [{ user_name: 'buaa_icourse', content: '你说对了！' }, { user_name: 'BUAA_ICOURSE', content: '说的很好。' }], time: '2017-11-29', comment_num: 2, comment_active: { display: 'none' }, input_comment: '' }
    */
  },
  data () {
    return {
      course_name: '',
      response_num: 0,
      response_page_size: 10,
      main: {},
      responses_list: [],
      responses: [],
      more_comment_button_style: { display: 'none' },
      editor: {
        content: '',
        option: { placeholder: '保护健康，文明评论' },
        current_text_length: 0,
        overflow: false,
        current_available_text: 2000,
        text_limit: 2000,
        least: 10
      },
      dev: true
    }
  },
  computed: {
  },
  methods: {
    return_forum_button_clicked: function () {
      this.$router.push({ path: '/course/page/'+this.$route.params.course_id+'/forum' })
    },
    agree_button_clicked: function (is_main, value, id, index) {
      console.log(is_main, value, id, index)
      if (!this.$store.state.is_login) {
        this.$message({
          showClose: true,
          type: 'error',
          message: '请先登录'
        })
      } else {
        var post_url = (this.dev ? get_url('/post/follow/evaluate/') : '/post/follow/evaluate')
        var post_data = { follow_id: id, grade: value }
        var _this = this
        $.ajax({
          ContentType: 'application/json; charset=utf-8',
          dataType: 'json',
          url: post_url,
          type: 'POST',
          data: post_data,
          success: function (data) {
            var code = Number(data['error'])
            if (code === 0) {
              var target = (is_main ? _this.main : _this.responses[index])
              target.agree_num += value
            } else if (code === 1) {
              _this.$message({
                showClose: true,
                type: 'error',
                message: '评价失败了呢'
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
    main_comment_button_clicked: function () {
      this.main.comment_active.display = this.main.comment_active.display==='none' ? 'inline' : 'none'
    },
    main_input_comment_button_clicked: function () {
      var target_content = this.main.input_comment
      if (!this.$store.state.is_login) {
        this.$message({
          showClose: true,
          type: 'error',
          message: '请先登录再评论'
        })
      } else if (target_content === '') {
        this.$message({
          showClose: true,
          message: '评论内容不能为空！',
          type: 'error'
        })
      }
      else {
        var post_url = (this.dev ? get_url('/post/comment/publish/') : '/post/comment/publish/')
        var post_data = { follow_id: this.main.id, to_comment_id: -1, content: target_content }
        var _this = this
        $.ajax({
          ContentType: 'application/json; charset=utf-8',
          dataType: 'json',
          url: post_url,
          type: 'POST',
          data: post_data,
          success: function (data) {
            var code = Number(data['error'])
            if (code === 0) {
              _this.$router.push({ path: '/course/page/' + _this.$route.params.course_id + '/forum/' + _this.$route.params.thread_id })
            } else if (code === 1) {
              _this.$message({
                showClose: true,
                type: 'error',
                message: '评论失败'
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
    response_comment_button_clicked: function (index) {
      this.responses[index].comment_active.display = this.responses[index].comment_active.display==='none' ? 'inline' : 'none'
    },
    response_input_comment_button_clicked: function (index) {
      var target_content = this.responses[index].input_comment
      if (!this.$store.state.is_login) {
        this.$message({
          showClose: true,
          type: 'error',
          message: '请先登录再评论'
        })
      } else if (target_content === '') {
        this.$message({
          showClose: true,
          message: '评论内容不能为空！',
          type: 'error'
        })
      }
      else {
        var post_url = (this.dev ? get_url('/post/comment/publish/') : '/post/comment/publish/')
        var post_data = { follow_id: this.responses[index].id, to_comment_id: -1, content: target_content }
        var _this = this
        $.ajax({
          ContentType: 'application/json; charset=utf-8',
          dataType: 'json',
          url: post_url,
          type: 'POST',
          data: post_data,
          success: function (data) {
            var code = Number(data['error'])
            if (code === 0) {
              _this.$router.push({ path: '/course/page/' + _this.$route.params.course_id + '/forum/' + _this.$route.params.thread_id })
            } else if (code === 1) {
              _this.$message({
                showClose: true,
                type: 'error',
                message: '评论失败'
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
    edit_comment_button_clicked: function () {},
    load_more_responses_button_clicked: function () {
      var len = (this.response_num - this.response_page_size > 0 ? this.response_num - this.response_page_size : 0)
      if (len > 0) {
        var target_list = this.responses_list.slice(this.response_page_size, this.response_page_size + len)
        var post_url = (this.dev ? get_url('/follow/info/list/') : '/follow/info/list/')
        var post_data = { id_list: target_list }
        var _this = this
        $.ajax({
          ContentType: 'application/json; charset=utf-8',
          dataType: 'json',
          url: post_url,
          type: 'POST',
          data: post_data,
          success: function (data) {
            var info_list = data['info_list']
            for (var j = 0; j < info_list.length; j++) {
              var temp = {}
              temp.id = target_list[j]
              temp.agree_num = 0 // need
              temp.user_name = info_list[j].username
              temp.self_intro = '' // need
              temp.avatar = default_img // need
              temp.content = info_list[j].content
              temp.time = String(info_list[j].edit_time)
              temp.comment_active = {}
              temp.comment_active.display = 'none'
              temp.input_comment = ''
              _this.responses.push(temp)
            }
            _this.more_comment_button_style.display = 'none'
          },
          error: function () {
            _this.$message({
              showClose: true,
              type: 'error',
              message: '加载全部帖子信息失败'
            })
          }
        })
      }
    },
    on_editor_change: function ({editor, html, text}) {
      this.editor.current_text_length = text.length
      this.editor.overflow = (text.length > this.editor.text_limit || text.length < this.editor.least)
      this.editor.current_available_text = ((this.editor.text_limit - text.length) < 0 ? 0 : (this.editor.text_limit - text.length))
    },
    post_submit_button_clicked: function () {
      if (this.editor.overflow) {
        this.$message({
          showClose: true,
          message: '请控制评论的字符在10-2000之内',
          type: 'error'
        })
      } else if (!this.$store.state.is_login) {
        this.$message({
          showClose: true,
          message: '请先登录再评论',
          type: 'error'
        })
      } else {
        this.$confirm('确认发布评论？', '发布', {
          confirmButtonText: '发布',
          cancelButtonText: '取消',
          type: 'info'
        }).then(() => {
          var post_url = (this.dev ? get_url('/post/follow/publish/') : '/post/follow/publish/')
          var post_data = { post_id: this.$route.params.thread_id, content: this.editor.content, editor: 0 }
          var _this = this
          $.ajax({
            ContentType: 'application/json; charset=utf-8',
            dataType: 'json',
            url: post_url,
            type: 'POST',
            data: post_data,
            success: function (data) {
              var code = Number(data['error'])
              if (code === 0) {
                _this.$message({
                  showClose: true,
                  type: 'success',
                  message: '发布成功'
                })
                _this.$router.push({ path: '/course/page/' + _this.$route.params.course_id + '/forum/' + _this.$route.params.thread_id })
              } else if (code === 1) {
                _this.$message({
                  showClose: true,
                  type: 'error',
                  message: '发布评论失败'
                })
              }
            },
            error: function () {
              _this.$message({
                showClose: true,
                type: 'error',
                message: '无法链接到服务器'
              })
            }
          })
        })
      }
    }
  }
}
</script>

<style type="text/css" scpoed>
  .container{
    font-family: "Microsoft Yahei";
  }
  .title{
    text-align: center;
    font-size: 40px;
    padding-bottom: 30px;
  }
  .main_container{
    height: auto;
    margin-top: 30px;
  }
  .arrow_button{
    height:50px;
  }
  .agree_num{
    font-size: 25px;
    color: grey;
  }
  .main_title_container{
    margin-bottom: 10px;
  }
  .main_title{
    font-size: 32px;
  }
  .avatar{
    height: 50px;
    width: 50px;
  }
  .user_name{
    font-size: 20px;
  }
  .self_intro{
    font-size: 16px;
    color: grey;
  }
  .info_row{
    margin-bottom: 10px;
  }
  .content{
    font-size: 24px;
  }
  .footer_row{
    margin-top: 5px;
    margin-bottom: 10px;
    float: right;
  }
  .comment_button{
    font-size: 18px;
  }
  .time{
    font-size: 18px;
    color: grey;
  }
  .response_info_row{
    text-align: center;
    font-size: 32px;
    margin-top: 20px;
  }
  .comment{
  }
  .comment_row{
  }
  .comment_input{
    margin-bottom: 10px;
  }
  .editor_container{
    height: 500px;
  }
  .editor{
    height: 435px;
  }
  .limit{
    height: 30px;
    border: 1px solid #ccc;
    border-top: none;
    line-height: 30px;
    text-align: right;
    margin-bottom: 20px;
  }
  .all_text{
    text-align: center;
    font-size: 24px;
  }
  .bar{
    padding: 10px 30% 10px 30%;
    border:1px solid #ccc;
    margin-bottom: 30px;
    margin-top:10px;
  }
  .submit_button{
    float: right;
    margin-bottom: 100px;
    width: 100px;
  }
</style>