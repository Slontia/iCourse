<template>
    <div id="course">
        <Header></Header>
            <el-col :span="24" class="navigator">
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
                              <el-col :span="24" class="tools_bar" style="padding-bottom: 0px;">
                                <el-form :inline="true" :model="filters">
                                  <el-form-item>
                                    <el-input v-model = "filters.name"></el-input>
                                  </el-form-item>
                                  <el-form-item>
                                    <el-button type="primary" v-on:click="search_course_clicked" icon="el-icon-search">搜索</el-button>
                                  </el-form-item>
                                  <el-form-item>
                                    <el-button type="primary" @click="add_course_clicked" icon="el-icon-plus" style="float:left;">新增课程
                                    </el-button>
                                  </el-form-item>
                                </el-form>
                              </el-col>

                            <!-- course table -->
                            <el-table :data="courses" highlight-current-row v-loading="load_courses" style="width: 100%;" height="450">
                              <el-table-column type="index" label="序号"width="100"></el-table-column>
                              <el-table-column prop="course_name" label="课程编号" width="150" sortable></el-table-column>
                              <el-table-column prop="course_id" label="课程名" width="200" sortable></el-table-column>
                              <el-table-column prop="course_academy" label="开设学院" width="200" sortable></el-table-column>
                              <el-table-column prop="course_class" label="课程分类" width="200" sortable></el-table-column>
                              <el-table-column prop="course_teacher" label="任课教师" width="200" sortable></el-table-column>
                            </el-table>

                            <!-- tools bar beneath-->
                            <el-col :span="24" class="tools_bar">
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
import Header from '../general/Header'
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

    get_courses () {
      this.total = 2
      var a = {
        course_name: '软件工程基础',
        course_id: '2333333',
        course_academy: '计算机学院',
        course_teacher: '罗杰',
        course_class: '专业选修课'
      }
      var b = {
        course_name: '编译技术',
        course_id: '1234567',
        course_academy: '计算机学院',
        course_teacher: '史晓华',
        course_class: '核心专业课'
      }
      this.courses.push(a)
      this.courses.push(b)
    },
    course_tree_clicked (data, node) {
      // todo: use api to get the corresponding courses
      this.course_bread_message = node.label
    },
    search_course_clicked () {
      // todo: 1.more search selection 2.use api to get the corresponding courses of this.filters.name
      this.$router.push({ path: '/course_info' })
    },
    add_course_clicked () {
      // todo: add course function
    }
  },
  mounted () {
    this.get_courses()
  }
}
</script>

<style type="text/css">

    .tools_bar {
      width: 100%;
      float: left;
    }

    .navigator {
        display: flex;
        position: absolute;
        top: 60px;
        bottom: 0px;
        oveflow:hidden;
      }
      .course_tree {
        height: 100%;
        width: 330px;
        margin-right: 10px;
      }
      .course_table_title {
            width: 200px;
            float: left;
            color: #475669;
            margin-top: 10px;
          }
      .content-wrapper {
          background-color: #fff;
          box-sizing: border-box;
        }
      .content-container {
        margin-left: 100px;
        flex:1;
        overflow-y: scroll;
        padding: 20px;
      }
</style>