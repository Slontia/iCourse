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
          <el-button type="button"><i class="el-icon-d-arrow-left"></i>返回课程页面</el-button>
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
      <el-row style="margin:20px 0px 0px 0px;">
        <el-col :span="6" :offset="2">
          <el-row style="margin:20px 0px 0px 0px;">
            <el-col :span="8" :offset="1">
              <img :src="zipImg" style="height:100px;"></img>
            </el-col>
            <el-col :span="14" :offset="1">
              <el-row class="resourseTitle">
                全部课件.zip
              </el-row>
              <el-row class="resourseIntro">
                里面整合了1~13章课件，全部是pdf格式
              </el-row>
            </el-col>
          </el-row>
        </el-col>
        <el-col :span="6" :offset="1">
          <div style="height:200px;background-color:LightSeaGreen;"></div>
        </el-col>
        <el-col :span="6" :offset="1">
          <div style="height:200px;background-color:LightSeaGreen;"></div>
        </el-col>
      </el-row>
    </el-row>
  </div>
</template>


<script>
import Header from '../general/Header'
import ZipImg from './../../assets/headportrait.jpg'
export default {
  name: 'resource',
  components: { Header },
  data () {
    return {
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
      zipImg: ZipImg
    }
  },
  methods: {
    closed: function () { alert('还未开放') }
  }
}
</script>

<style>
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
</style>