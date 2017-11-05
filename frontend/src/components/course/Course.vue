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
                                <el-form :inline="true" :model="filters">
                                  <el-form-item>
                                    <el-input v-model = "filters.name" placeholder="支持课程名、课程号"></el-input>
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
                              <el-table-column type="index" label="序号"width=""></el-table-column>
                              <el-table-column prop="course_name" label="课程编号"  sortable></el-table-column>
                              <el-table-column prop="course_id" label="课程名"  sortable></el-table-column>
                              <el-table-column prop="course_academy" label="开设学院"  sortable></el-table-column>
                              <el-table-column prop="course_class" label="课程分类"  sortable></el-table-column>
                              <el-table-column prop="course_hours" label="学时"  sortable></el-table-column>
                              <el-table-column prop="course_credit" label="学分"  sortable></el-table-column>
                            </el-table>
                          </el-col>

                            <!-- tools bar beneath-->
                            <el-col :span="24" class="tools_bar_bottom">
                              <el-pagination layout="prev,pager,next" @current_change="handle_current_change" :page-size="20" :total="total" style="float:right;"></el-pagination>
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
import Header from '../general/Header'
import get_url from '../general/getUrl'
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
                   { label: '6系' }
        ]
      }],
      filters: {
        name: ''
      },
      total: 0, // total courses
      page: 1, // current page
      load_courses: false, // v-loading
      courses: [],
      course_bread_message: ''
    }
  },
  methods: {
    handle_current_change (value) {
      this.page = value
      // todo:get_courses
    },
    course_tree_clicked (data, node) {
      // todo: use api to get the corresponding courses
      if (typeof (node.parent.label) !== 'undefined') {
        this.course_bread_message = node.parent.label + '->' + node.label
        this.load_courses = true
        if (node.parent.label === '开设院系') {
          var temp1 = { 'college_id': node.label[0] }
          $.ajax({
            ContentType: 'application/json; charset=utf-8',
            dataType: 'json',
            type: 'POST',
            url: get_url('/course/college_course/'),
            data: temp1,
            success: function (data) {
              this.courses = []
              console.log('ok')
              alert('success')
            },
            error: function () {
              alert('错误')
            }
          })
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
            url: get_url('/course/classification_course/'),
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
        this.load_courses = false
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
        var post_data = {
          'keyword': this.filters.name
        }
        var self = this
        $.ajax({
          ContentType: 'application/json; charset=utf-8',
          dataType: 'json',
          url: get_url('/course/searching/'),
          type: 'POST',
          data: post_data,
          success: function (data) {
            alert('成功！开始搜索')
            self.total = data['query_list'].length
            self.courses = []
            for (var i = 0; i < data['query_list'].length; i++) {
              var course = data['query_list'][i]
              self.courses.push({
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
      }
    },
    add_course_clicked () {
      // todo: add course function
      alert('功能暂未开放,敬请期待')
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
        height: 600px;
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