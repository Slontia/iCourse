<template>
    <div id="course">
        <Header></Header>
            <el-col :span="24" class="navigator" style="margin-top: 20px">
              <el-tree :data="tree_data" :props="defaultProps" accordion @node-click="course_tree_clicked" class="course_tree">
              </el-tree>
            <section class="course_content_container">
                <div class = "grid-content bg-purple-light">
                    <el-col :span="24" class="breadcrumb-container">
                        <strong class= "course_table_title">{{ course_bread_message }}
                        </strong>
                        <el-col :span="24" class="course_content_wrapper">
                          <transition name="fade" mode="out-in">
                            <section>
                              <!-- tools bar above -->
                              <el-col :span="24" class="tools_bar_top" style="padding-bottom: 0px;">
                                <el-form :inline="true" :model="filters" >
                                  <el-form-item>
                                    <el-input type="text" v-model = "filters.name" placeholder="支持课程名、课程号" @keydown.enter.native.prevent="search_course_clicked" ></el-input>
                                  </el-form-item>
                                  <el-form-item>
                                    <el-button type="primary" v-on:click="search_course_clicked" icon="search">搜索</el-button>
                                  </el-form-item>
                                  <el-form-item>
                                    <el-button type="primary" @click="add_course_clicked" icon="plus" style="float:left;">添加课程
                                    </el-button>
                                  </el-form-item>
                                </el-form>
                              </el-col>

                            <!-- course table -->
                            <el-col :span="24">
                            <el-table :data="courses" highlight-current-row v-loading="load_courses" style="width: auto;" height="500" stripe>
                              <el-table-column type="index" label=" 序 号 " align="center" width="100"></el-table-column>
                              <el-table-column prop="course_id" label="课程编号"  sortable align="center"></el-table-column>
                              <el-table-column prop="course_name" label="课程名"  sortable align="center"></el-table-column>
                              <el-table-column prop="course_academy" label="开设学院"  sortable align="center"></el-table-column>
                              <el-table-column prop="course_class" label="课程分类"  sortable align="center"></el-table-column>
                              <!--
                              <el-table-column prop="course_hours" label="学时"  sortable></el-table-column>
                            --><el-table-column prop="course_credit" label="学分"  sortable align="center"></el-table-column>
                              <el-table-column label="操作" align="center">
                              <template slot-scope="scope">
                                <el-button
                                  size="mini"
                                  @click="to_course_page(scope.$index)">进入课程</el-button>
                              </template>
                            </el-table-column>
                            </el-table>
                          </el-col>

                            <!-- tools bar beneath-->
                            <el-col :span="24" class="tools_bar_bottom">
                              <el-pagination layout="prev,pager,next" @current-change="handle_current_change" :page-size="page_size" :total="total" :current-page.sync="current_page" style="float:right;"></el-pagination>
                            </el-col>
                            </section>
                          </transition>
                        </el-col>
                    </el-col>

                </div>
            </section>
        </el-col>
</div>
</template>


<script type="text/javascript">
/* eslint-disable brace-style */
/* eslint-disable camelcase */
/* eslint-disable space-infix-ops */
import Header from '../general/Header'
// 请不要删除和get_url相关的行，如果你真的需要请告诉我下原因。by xindetai
// import get_url from '../general/getUrl'
import $ from 'jquery'
export default {
  name: 'Course',
  components: { Header },
  data () {
    return {
      tree_data: [{
        label: '课程类别',
        children: [{ label: '一般通识课' },
                   { label: '核心通识课' },
                   { label: '核心专业课' },
                   { label: '一般专业课' },
                   { label: '公共必修课' },
                   { label: '公共选修课' }]
      },
      {
        label: '开设院系',
        children: [{ label: '1系' },
                   { label: '2系' },
                   { label: '3系' },
                   { label: '4系' },
                   { label: '5系' },
                   { label: '6系' },
                   { label: '7系' },
                   { label: '9系' },
                   { label: '10系' },
                   { label: '11系' },
                   { label: '12系' },
                   { label: '13系' },
                   { label: '14系' },
                   { label: '15系' },
                   { label: '17系' },
                   { label: '19系' },
                   { label: '20系' },
                   { label: '21系' },
                   { label: '26系' },
                   { label: '27系' }
        ]
      }],
      filters: {
        name: ''
      },
      total: 0, // total courses
      current_page: 1, // current page
      page_size: 10,
      load_courses: false, // v-loading
      courses: [],
      storage: [],
      course_bread_message: ''
    }
  },
  methods: {
    to_course_page (index) {
      this.$router.push({ path: ('/course/page/' + this.courses[index]['course_id'] + '/') })
    },
    handle_current_change (value) {
      this.current_page = value
      this.courses = []
      var len = this.storage.length < value*this.page_size ? this.storage.length % this.page_size : this.page_size
      console.log(this.storage.length)

      for (var i = 0; i < len; i++) {
        this.courses.push(this.storage[(value-1)*this.page_size+i])
      }
    },
    course_tree_clicked (data, node) {
      // todo: use api to get the corresponding courses
      if (typeof (node.parent.label) !== 'undefined') {
        this.course_bread_message = node.parent.label + '->' + node.label
        this.load_courses = true
        var self = this
        if (node.parent.label === '开设院系') {
          var temp1 = { 'college_id': node.label.substr(0, node.label.length-1) }
          $.ajax({
            ContentType: 'application/json; charset=utf-8',
            dataType: 'json',
            type: 'POST',
            url: '/course/college_course/',
            data: temp1,
            async: false,
            success: function (data) {
              // 初始化storage和courses以及当前页数
              var info_list = data['course_info_list']
              self.storage = []
              self.total = info_list.length
              for (var i = 0; i < info_list.length; i++) {
                var item = {
                  'course_name': info_list[i]['name'],
                  'course_id': info_list[i]['id'],
                  'course_academy': info_list[i]['college_id'],
                  'course_hours': info_list[i]['hours'],
                  'course_credit': info_list[i]['credit'],
                  'course_class': info_list[i]['class_id']
                }
                self.storage.push(item)
              }
            },
            error: function () {
              alert('拉取信息失败!')
            }
          })
          self.load_courses = false
          self.handle_current_change(1)
        }
        else if (node.parent.label === '课程类别') {
          var temp2 = { 'class_id': '' }
          switch (node.label) {
            case ('一般通识课'):
              temp2.class_id = '0'
              break
            case ('核心通识课'):
              temp2.class_id = '1'
              break
            case ('核心专业课'):
              temp2.class_id = '2'
              break
            case ('一般专业课'):
              temp2.class_id = '3'
              break
            case ('公共必修课'):
              temp2.class_id = '4'
              break
            case ('公共选修课'):
              temp2.class_id = '5'
              break
            default:
              temp2.class_id = '-1'
          }

          $.ajax({
            ContentType: 'application/json; charset=utf-8',
            dataType: 'json',
            type: 'POST',
            url: '/course/classification_course/',
            data: temp2,
            success: function (data) {
              console.log('ok')
              alert('success')
            },
            error: function () {
              alert('错误')
            }
          })
        }
        else {
          alert('结点不存在')
        }
      }
      else {
        this.course_bread_message = node.label
      }
    },
    search_course_clicked () {
      if (!this.filters.name) {
        alert('搜索内容不能为空！')
      }
      else {
        this.load_courses = true
        this.course_bread_message = this.filters.name
        var post_data = {
          'keyword': this.filters.name
        }
        var self = this
        $.ajax({
          ContentType: 'application/json; charset=utf-8',
          dataType: 'json',
          url: '/course/searching/',
          type: 'POST',
          data: post_data,
          async: false,
          success: function (data) {
            self.total = data['query_list'].length
            self.storage = []
            for (var i = 0; i < data['query_list'].length; i++) {
              var course = data['query_list'][i]
              self.storage.push({
                'course_name': course['name'],
                'course_id': course['id'],
                'course_academy': course['college_id'],
                'course_hours': course['hours'],
                'course_credit': course['credit'],
                'course_class': course['class_id']
              })
            }
          },
          error: function () {
            alert('连接服务器异常')
          }
        })
        self.load_courses = false
        self.handle_current_change(1)
      }
    },
    add_course_clicked () {
      // todo: add course function
      this.$message({
        showClose: true,
        message: '功能暂未开放，敬请期待'
      })
    }
  },
  mounted () {
  }
}
</script>

<style type="text/css" scpoed>
    .tools_bar_above {
      width: auto;
      float: left;
    }
    .tools_bar_bottom {
      margin-top: 10px;
    }
    .navigator {
        font-family: Microsoft Yahei;
        display: flex;
        top: 60px;
        bottom: 0px;
        oveflow:hidden;
      }
      .course_tree {
        height: 800px;
        width: auto;
        min-width: 20%;
        margin-right: 10px;
        font-family: Microsoft Yahei;
      }
      .course_table_title {
            width: 50%;
            float: left;
            color: #475669;
            margin-top: 10px;
            margin-bottom: 10px;
          }
      .content-wrapper {
          background-color: #fff;
          box-sizing: border-box;
        }
      .course_content_container{
      }
</style>