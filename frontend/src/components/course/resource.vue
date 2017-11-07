<template>
  <div id="resource">
    <el-row>
      <el-col :span="24">
        <Header></Header>
      </el-col>
    </el-row>
    <el-row style="margin:80px 0px 0px 0px;">
      <el-row>
        <el-col :span="8" :offset="1">
          <el-button type="button" @click.native="return_course_info_page_clicked()"><i class="el-icon-d-arrow-left"></i>返回课程页面</el-button>
        </el-col>
        <el-col id="resourceTitle" :span="15">
          {{ course }}-课程资源
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="24" style="text-align:center;">
          <el-button-group>
            <el-button type="primary" style="width:250px;">课件</el-button>
            <el-button type="button" style="width:250px;" @click.native="closed">考题</el-button>
            <el-button type="button" style="width:250px;" @click.native="closed">习题</el-button>
            <el-button type="button" style="width:250px;" @click.native="closed">笔记</el-button>
            <el-button type="button" style="width:250px;" @click.native="closed">其他</el-button>
          </el-button-group>
        </el-col>
      </el-row>
      <el-row style="margin:20px 0px 0px 0px;">
        <el-col :span="4" :offset="2">
          <el-select v-model="sortMode" placeholder="请选择排序方式">
            <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
            </el-option>
          </el-select>
        </el-col>
        <el-col :span="2">
          <el-button type="button" @click.native="closed">升序排序</el-button>
        </el-col>
        <el-col :span="2">
          <el-button type="button" @click.native="closed">降序排序</el-button>
        </el-col>
         <el-col :span="4" :offset="6">
          <el-input v-model="input" placeholder="资源名称"></el-input>
        </el-col>
        <el-col :span="2" :offset="1">
          <el-button type="button" @click.native="closed">搜索资源</el-button>
        </el-col>       
      </el-row>
      <el-row>
        <el-col :span="20" :offset="2">
          <el-row style="margin:20px 0px 0px 0px;height:1px;background-color:black;">
          </el-row>
        </el-col>
      </el-row>
      <el-row style="margin:20px 0px 0px 0px;">
        <el-col :span="6" :offset="2">          
        <el-row v-for="item in resourcesData" v-if="item.col1" class="hoverChange"  @click.native="dialogVisible=true">
          <el-row style="margin:20px 0px 0px 0px;" >
            <el-col :span="8" :offset="1">
              <img :src="zipImg" style="height:100px;"></img>
            </el-col>
            <el-col :span="14" :offset="1">
              <el-row class="resourseTitle">
                {{ item.name }}
              </el-row>
              <el-row class="resourseIntro">
                {{ item.intro }}
              </el-row>
            </el-col>
          </el-row>
          <el-row  style="margin:20px 0px 0px 0px;">
            <el-col :span="4" :offset="1">
              <i class="el-icon-star-off"></i>&nbsp;{{ item.collections }}
            </el-col>
            <el-col :span="4">
              <i class="el-icon-arrow-down"></i>&nbsp;{{ item.downloads }}
            </el-col>
            <el-col :span="4">
              <i class="el-icon-message"></i>&nbsp;{{ item.messages }}
            </el-col>
            <el-col :span="2" :offset="5">
              <img :src="zipImg" style="height:18px;"></img>
            </el-col>
            <el-col :span="4">
              <a href="">{{ item.author }}</a>
            </el-col>
          </el-row>
          <el-row style="margin:10px 0px 0px 0px;">
            <el-col :span="11" :offset="13" style="color:#d3d3d3;">
              上传时间:{{ item.time }}
            </el-col>
          </el-row>
          <el-row style="margin:5px 0px 0px 0px;height:1px;background-color:black;"></el-row>
        </el-row>        
        </el-col>
         

        <el-col :span="6" :offset="1">
          <el-row v-for="item in resourcesData" v-if="item.col2" class="hoverChange"  @click.native="dialogVisible=true">
          <el-row style="margin:20px 0px 0px 0px;" >
            <el-col :span="8" :offset="1">
              <img :src="zipImg" style="height:100px;"></img>
            </el-col>
            <el-col :span="14" :offset="1">
              <el-row class="resourseTitle">
                {{ item.name }}
              </el-row>
              <el-row class="resourseIntro">
                {{ item.intro }}
              </el-row>
            </el-col>
          </el-row>
          <el-row  style="margin:20px 0px 0px 0px;">
            <el-col :span="4" :offset="1">
              <i class="el-icon-star-off"></i>&nbsp;{{ item.collections }}
            </el-col>
            <el-col :span="4">
              <i class="el-icon-arrow-down"></i>&nbsp;{{ item.downloads }}
            </el-col>
            <el-col :span="4">
              <i class="el-icon-message"></i>&nbsp;{{ item.messages }}
            </el-col>
            <el-col :span="2" :offset="5">
              <img :src="zipImg" style="height:18px;"></img>
            </el-col>
            <el-col :span="4">
              <a href="">{{ item.author }}</a>
            </el-col>
          </el-row>
          <el-row style="margin:10px 0px 0px 0px;">
            <el-col :span="11" :offset="13" style="color:#d3d3d3;">
              上传时间:{{ item.time }}
            </el-col>
          </el-row>
          <el-row style="margin:5px 0px 0px 0px;height:1px;background-color:black;"></el-row>
        </el-row>
        </el-col>
        <el-col :span="6" :offset="1">
          <el-row v-for="item in resourcesData" v-if="item.col3" class="hoverChange" @click.native="dialogVisible=true">
          <el-row style="margin:20px 0px 0px 0px;" >
            <el-col :span="8" :offset="1">
              <img :src="zipImg" style="height:100px;"></img>
            </el-col>
            <el-col :span="14" :offset="1">
              <el-row class="resourseTitle">
                {{ item.name }}
              </el-row>
              <el-row class="resourseIntro">
                {{ item.intro }}
              </el-row>
            </el-col>
          </el-row>
          <el-row  style="margin:20px 0px 0px 0px;">
            <el-col :span="4" :offset="1">
              <i class="el-icon-star-off"></i>&nbsp;{{ item.collections }}
            </el-col>
            <el-col :span="4">
              <i class="el-icon-arrow-down"></i>&nbsp;{{ item.downloads }}
            </el-col>
            <el-col :span="4">
              <i class="el-icon-message"></i>&nbsp;{{ item.messages }}
            </el-col>
            <el-col :span="2" :offset="5">
              <img :src="zipImg" style="height:18px;"></img>
            </el-col>
            <el-col :span="4">
              <a href="">{{ item.author }}</a>
            </el-col>
          </el-row>
          <el-row style="margin:10px 0px 0px 0px;">
            <el-col :span="11" :offset="13" style="color:#d3d3d3;">
              上传时间:{{ item.time }}
            </el-col>
          </el-row>
          <el-row style="margin:5px 0px 0px 0px;height:1px;background-color:black;"></el-row>
        </el-row>
        </el-col>
      </el-row>
    </el-row>

    <!-- 资源详细信息窗口 -->
    <el-dialog title="资源信息" :visible.sync="dialogVisible" size="tiny">
      <el-row>
        <el-col :span="24">
          <div id="dialogTitle">全部资源</div>
        </el-col>
      </el-row>
      <el-row style="margin:15px 0px 0px 0px;">
        <el-col :span="16" :offset="1">
          <el-row>
            <el-col :span="8">
              上传者:
            </el-col>
            <el-col :span="16">
              <img :src="zipImg" style="height:18px;"></img>
              <a href="">果冻</a>
            </el-col>
          </el-row>
          <el-row style="margin:10px 0px 0px 0px;">
            <el-col :span="8">
              上传时间:
            </el-col>
            <el-col :span="16">
              2017-3-26
            </el-col>
          </el-row>
          <el-row style="margin:10px 0px 0px 0px;">
            <el-col :span="8">
              资源大小:
            </el-col>
            <el-col :span="16">
              98.6MB
            </el-col>
          </el-row>
          <el-row style="margin:10px 0px 0px 0px;">
            <el-col :span="24">
              简介:
            </el-col>
          </el-row>
          <el-row style="margin:10px 0px 0px 0px;">
            <el-col :span="24">
              里面整合了1~13章课件，全部是pdf格式
            </el-col>
          </el-row>
        </el-col>
        <el-col :span="7">
          <el-row style="text-align:center;">
            <img :src="zipImg" style="height:120px;"></img>
          </el-row>
          <el-row style="text-align:center;">
            <el-button type="primary">点击下载</el-button>
          </el-row>
        </el-col>
      </el-row>
      <el-row style="margin:10px 0px 0px 0px;">
        <el-col :span="2" :offset="1">标签:</el-col>
        <el-col :span="3">课件:</el-col>
        <el-col :span="2" :offset="11"><a href="">好评</a></el-col>
        <el-col :span="1">21</el-col>
        <el-col :span="2" :offset="1"><a href="">差评</a></el-col>
        <el-col :span="1">2</el-col>
      </el-row>
      <el-row style="margin:10px 0px 0px 0px;">
        <el-col :span="1" :offset="1"><i class="el-icon-star-off"></i></el-col>
        <el-col :span="1">23</el-col>
        <el-col :span="1" :offset="1"><i class="el-icon-arrow-down"></i></el-col>
        <el-col :span="1">656</el-col>
      </el-row>
      <el-row style="margin:20px 0px 0px 0px;">
        <el-col :span="6" :offset="1" style="height:20px;font-weight:bold;font-size:20px;">全部评论</el-col>
        <el-col :span="1" :offset="1" style="height:20px;line-height:20px;"><i class="el-icon-message"></i></el-col>
        <el-col :span="1" style="height:20px;line-height:20px;">0</el-col>
        <el-col :span="4" :offset="10" style="height:20px;line-height:20px;"><a href="">我要评论</a></el-col>        
      </el-row>
      <el-row style="margin:5px 0px 0px 0px;">
        <el-col :span="22" :offset="1">
          <el-row style="background-color:black;height:3px;"></el-row>
        </el-col>
      </el-row>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible=false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>



  </div>
</template>


<script>
import Header from '../general/Header'
import ZipImg from './../../assets/headportrait.jpg'
import $ from 'jquery'
export default {
  name: 'resource',
  components: { Header },
  data () {
    return {
      dialogVisible: false,
      course: '软件工程基础',
      options: [
        {
          value: '选项1',
          label: '按上传时间排序'
        }, {
          value: '选项2',
          label: '按文件类型排序'
        }, {
          value: '选项3',
          label: '按好评度排序'
        }
      ],
      sortMode: '按上传时间排序',
      zipImg: ZipImg,
      resourcesData: [
        {
          col1: false,
          col2: true,
          col3: false,
          name: '全部课件.zip',
          intro: '里面整合了1~13章课件，全部是pdf格式',
          collections: 23,
          downloads: 56,
          messages: 2,
          author: '果冻',
          time: '2017-3-26'
        },
        {
          col1: false,
          col2: false,
          col3: true,
          name: '全部课件.zip',
          intro: '里面整合了1~13章课件，全部是pdf格式',
          collections: 23,
          downloads: 56,
          messages: 2,
          author: '果冻',
          time: '2017-3-26'
        },
        {
          col1: true,
          col2: false,
          col3: false,
          name: '全部课件.zip',
          intro: '里面整合了1~13章课件，全部是pdf格式',
          collections: 23,
          downloads: 56,
          messages: 2,
          author: '果冻',
          time: '2017-3-26'
        },
        {
          col1: true,
          col2: false,
          col3: false,
          name: '全部课件.zip',
          intro: '里面整合了1~13章课件，全部是pdf格式',
          collections: 23,
          downloads: 56,
          messages: 2,
          author: '果冻',
          time: '2017-3-26'
        }
      ]
    }
  },
  methods: {
    closed: function () { alert('还未开放') },
    return_course_info_page_clicked () {
      this.$router.push({ path: ('/course/page/' + this.$route.params.course_id + '/') })
    }
  },
  created: function () {
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: '/resource/id/list/',
      type: 'POST',
      data: {'course_id': 1},
      success: function (data) {
        alert(data['resource_id_list'].length)
      },
      error: function () {
        alert('fail')
      }
    })
    /* $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: '/resource/information/',
      type: 'POST',
      data: {'resource_id': 1},
      success: function (data) {
        alert(data['resource_info']['id'])
      },
      error: function () {
        alert('fail')
      }
    }) */
  }
}
</script>

<style scpoed>
  #resourceTitle {
    font-size: 25px;
    font-weight: bold;
    height: 60px;
    line-height: 30px;
  }
  .resourseTitle {
    font-weight: bold;
    font-size: 20px;
  }
  .resourseIntro {
    margin: 10px 0px 0px 0px;
  }
  .hoverChange:hover {
    background-color:#7fffd4;
  }
  #dialogTitle {
    height: 30px;
    line-height: 30px;
    font-size: 25px;
    font-weight: bold;
    text-align: center;
  }
</style>