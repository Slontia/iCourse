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
          <el-button type="text" icon="caret-top" size="large" class = "arrow_button" @click="main_agree_button_clicked(1)"></el-button>
        </center>
        </el-row>
        <el-row>
          <center>
            <p class="agree_num">{{ main.agree_num }}</p>
          </center>
        </el-row>
        <el-row>
          <center>
          <el-button type="text" icon="caret-bottom" size="large" class="arrow_button" @click="main_agree_button_clicked(-1)"></el-button>
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
          <el-button type="text" size="large" icon="caret-top" class="arrow_button" @click="response_agree_button_clicked(1,response.id)"></el-button>
        </center>
        </el-row>
        <el-row>
          <center>
            <p class="agree_num">{{ response.agree_num }}</p>
          </center>
        </el-row>
        <el-row>
          <center>
          <el-button type="text" size="large" icon="caret-bottom" class="arrow_button" @click="response_agree_button_clicked(-1,response.id)"></el-button>
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
    <el-button class="bar" type="text">
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
      <quill-editor v-model="editor.content" ref="quill" class="editor" :options="editor.option" @ready="on_editor_ready($event)" @blur="on_editor_blur($event)" @focus="on_editor_focus($event)">
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
import default_img from '../../assets/headportrait.jpg'
export default {
  name: 'Thread',
  components: { Header },
  beforeCreate () {
    // todo:load thread and course name,
  },
  data () {
    return {
      course_name: '软件工程',
      response_num: 1,
      main: { agree_num: 10, title: '如何评论最近上线的BUAA-iCourse?', user_name: 'Aletheia', self_intro: 'buaa-icourse', avatar: default_img, content: '如题，感觉很厉害的样子', comments: [{ user_name: 'buaa_icourse', content: '你说对了！' }, { user_name: 'BUAA_ICOURSE', content: '说的很好。' }], time: '2017-11-29', comment_num: 2, comment_active: { display: 'none' }, input_comment: '' },
      responses: [
        { agree_num: 3, user_name: 'slontia', self_intro: 'buaa-icourse', avatar: default_img, content: '我也觉得很厉害', comments: [{ user_name: 'buaa_icourse', content: '你说对了！' }, { user_name: 'BUAA_ICOURSE', content: '说的很好。' }], time: '2017-11-29', comment_num: 2, comment_active: { display: 'none' }, input_comment: '' },
        { agree_num: 5, user_name: 'icourse', self_intro: 'buaa-icourse', avatar: default_img, content: '顶楼上', comments: [{ user_name: 'buaa_icourse', content: '你说对了！' }, { user_name: 'BUAA_ICOURSE', content: '说的很好。' }], time: '2017-11-29', comment_num: 2, comment_active: { display: 'none' }, input_comment: '' }
      ],
      editor: {
        content: '',
        option: {},
        current_text_length: 0,
        current_available_text: 5000
      }
    }
  },
  methods: {
    return_forum_button_clicked: function () {
      this.$router.push({ path: '/course/page/'+this.$route.params.course_id+'/forum' })
    },
    main_agree_button_clicked: function (value) {
      // todo:1.add the agree num to main,2.record the score of this user
    },
    main_comment_button_clicked: function () {
      this.main.comment_active.display = this.main.comment_active.display==='none' ? 'inline' : 'none'
    },
    response_agree_button_clicked: function (value, id) {
    },
    response_comment_button_clicked: function (index) {
      this.responses[index].comment_active.display = this.responses[index].comment_active.display==='none' ? 'inline' : 'none'
    },
    response_input_comment_button_clicked: function (index) {
      var name = this.$store.state.is_login === true ? this.$store.state.user_name : '匿名用户'
      var target_content = this.responses[index].input_comment
      if (target_content === '') {
        this.$message({
          showClose: true,
          message: '评论内容不能为空！'
        })
      }
      else {
        this.responses[index].comments.push({ user_name: name, content: target_content })
        this.responses[index].input_comment = ''
      }
      // todo: use ajax to send message back to synchronize the database
    },
    main_input_comment_button_clicked: function () {
      var name = this.$store.state.is_login === true ? this.$store.state.user_name : '匿名用户'
      var target_content = this.main.input_comment
      if (target_content === '') {
        this.$message({
          showClose: true,
          message: '评论内容不能为空！'
        })
      }
      else {
        this.main.comments.push({ user_name: name, content: target_content })
        this.main.input_comment = ''
      }
    },
    edit_comment_button_clicked: function () {},
    on_editor_ready: function () {
    },
    post_submit_button_clicked: function () {
      console.log(this.editor.content)
    }
  },
  computed: {
    editor () {
      return this.$refs.quill.quill
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