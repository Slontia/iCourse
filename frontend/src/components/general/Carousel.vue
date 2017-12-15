<template>
  <div id="Carousel" class="carousel">
    <h2 class="demonstration">北 航 课 程 资 源 下 载 站</h2>
    <el-row type="flex" justify="center">
      <el-col :span="6" :offset="18">
        <el-select v-model="academy" placeholder="选择系别来查看不同的内容~">
          <el-option v-for="item in academies" :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-col :span="16">
    <el-tabs v-model="active_post_type" type="card" @tab-click="handle_tab_clicked">
      <el-tab-pane label="热门帖子" name="hot_post">
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
      <center><hr width="80%"style="margin-top: 20px;"/></center>
      </template>
      </el-tab-pane>
      <el-tab-pane label="最新帖子" name="new_post">
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
      <center><hr width="80%"style="margin-top: 20px;"/></center>
      </template>
      </el-tab-pane>
    </el-tabs>
  </el-col>

  <el-col :span="1">
  <hr style="height:500px;margin:100px 0px 0px 20px;width:1px;border: none;border-left: 1px solid rgb(241,242,244)">
  </el-col>
  <el-col :span="6">
    <el-tabs v-model="active_resource_type" type="card" @tab-click="handle_tab_clicked">
      <el-tab-pane label="热门资源" name="hot_resource">
        <template v-for="resource in hot_resources">
      <el-row>
      <el-col :span="24" :offset="0">
                  <el-button type="text" class="card_button" @click.native="resource_clicked(resource.id)">
                        <el-row>
                          <el-col :span="12">
                            
                          <p class="card_title_text"><i class="el-icon-document"></i> {{ resource.title }}</p>
                        </el-col>
                        <el-col :span="2" :offset="10">
                        <p>
                          下载:{{ resource.frequency}}
                        </p>
                      </el-col>
                        </el-row>
                </el-button>
              <hr style="border: none;border-top: 1px solid rgb(241,242,244)"/>
                </el-col>
      </el-row>
      </template>
      </el-tab-pane>
      <el-tab-pane label="最新资源" name="new_resource">
        <template v-for="resource in new_resources">
      <el-row>
      <el-col :span="24" :offset="0">
                  <el-button type="text" class="card_button" @click.native="resource_button_clicked(resource.id)">
                        <el-row>
                          <el-col :span="12">
                            
                          <p class="card_title_text"><i class="el-icon-document"></i> {{ resource.title }}</p>
                        </el-col>
                        <el-col :span="2" :offset="10">
                        <p>
                          下载:{{ resource.frequency}}
                        </p>
                      </el-col>
                        </el-row>
                </el-button>
              <hr style="border: none;border-top: 1px solid rgb(241,242,244)"/>
                </el-col>
      </el-row>
      </template>
      </el-tab-pane>
    </el-tabs>
  </el-col>
  </el-row>
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
export default {
  name: 'Carousel',
  beforeCreate () {
  },
  data () {
    return {
      active_post_type: 'hot_post',
      active_resource_type: 'hot_resource',
      academy: '全部',
      academies: [
                { label: '计算机学院', value: 6 }
      ],
      new_threads: [],
      hot_threads: [],
      new_resources: [],
      hot_resources: []
    }
  },
  methods: {
    handle_tab_clicked: function (tab, event) {
    },
    enter_thread_button_clicked: function (value) {
      // value saves thread id
    },
    resource_button_clicked: function (value) {
      // value saves resource id
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
    color: grey;
    white-space: pre-wrap;
    word-break: break-all;
    word-wrap:break-word;
  }
</style>