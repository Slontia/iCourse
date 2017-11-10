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
         <el-col :span="4" :offset="4">
          <el-input v-model="input" placeholder="资源名称"></el-input>
        </el-col>        
        <el-col :span="2" :offset="1">
          <el-button type="button" @click.native="closed">搜索资源</el-button>
        </el-col>
        <el-col :span="2">
          <el-button type="button" @click.native="uploadDialogVisible=true">上传资源</el-button>
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
        <el-row v-for="item in resourcesData" v-if="item.col1" class="hoverChange"  @click.native="openDialog(item.id)">
          <el-row style="margin:20px 0px 0px 0px;" >
            <el-col :span="8" :offset="1">
              <img :src=item.img style="height:100px;"></img>
            </el-col>
            <el-col :span="14" :offset="1">
              <el-row class="resourseTitle">
                <textarea readonly style="font-weight: bold;font-size: 20px;">{{ item.name }}</textarea>
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
              <img :src='defaultImg' style="height:18px;"></img>
            </el-col>
            <el-col :span="4">
              <a href="">{{ item.author }}</a>
            </el-col>
          </el-row>
          <el-row style="margin:10px 0px 0px 0px;">
            <el-col :span="18" :offset="6" style="color:#d3d3d3;">
              上传时间:{{ item.time }}
            </el-col>
          </el-row>
          <el-row style="margin:5px 0px 0px 0px;height:1px;background-color:black;"></el-row>
        </el-row>        
        </el-col>         

        <el-col :span="6" :offset="1">
          <el-row v-for="item in resourcesData" v-if="item.col2" class="hoverChange"  @click.native="openDialog(item.id)">
          <el-row style="margin:20px 0px 0px 0px;" >
            <el-col :span="8" :offset="1">
              <img :src=item.img style="height:100px;"></img>
            </el-col>
            <el-col :span="14" :offset="1">
              <el-row class="resourseTitle">
                <textarea readonly style="font-weight: bold;font-size: 20px;">{{ item.name }}</textarea>
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
              <img :src='defaultImg' style="height:18px;"></img>
            </el-col>
            <el-col :span="4">
              <a href="">{{ item.author }}</a>
            </el-col>
          </el-row>
          <el-row style="margin:10px 0px 0px 0px;">
            <el-col :span="18" :offset="6" style="color:#d3d3d3;">
              上传时间:{{ item.time }}
            </el-col>
          </el-row>
          <el-row style="margin:5px 0px 0px 0px;height:1px;background-color:black;"></el-row>
        </el-row>
        </el-col>
        <el-col :span="6" :offset="1">
          <el-row v-for="item in resourcesData" v-if="item.col3" class="hoverChange" @click.native="openDialog(item.id)">
          <el-row style="margin:20px 0px 0px 0px;" >
            <el-col :span="8" :offset="1">
              <img :src=item.img style="height:100px;"></img>
            </el-col>
            <el-col :span="14" :offset="1">
              <el-row class="resourseTitle">
                <textarea readonly style="font-weight: bold;font-size: 20px;">{{ item.name }}</textarea>
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
              <img :src='defaultImg' style="height:18px;"></img>
            </el-col>
            <el-col :span="4">
              <a href="">{{ item.author }}</a>
            </el-col>
          </el-row>
          <el-row style="margin:10px 0px 0px 0px;">
            <el-col :span="18" :offset="6" style="color:#d3d3d3;">
              上传时间:{{ item.time }}
            </el-col>
          </el-row>
          <el-row style="margin:5px 0px 0px 0px;height:1px;background-color:black;"></el-row>
        </el-row>
        </el-col>
      </el-row>
    </el-row>

    <!-- 资源详细信息窗口 -->
    <el-dialog title="资源信息" :visible.sync="dialogVisible" v-if="dialogVisible" size="tiny">
      <ResourceDialog></ResourceDialog>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible=false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>

    <el-dialog title="上传资源" :visible.sync="uploadDialogVisible" size="tiny">
      <el-form label-position="left">
        <el-form-item type="text" label="资源介绍" :label-width="form_label_width">
          <el-input v-model="resourceIntro" auto_complete="off" placeholder="请输入资源介绍"></el-input>
        </el-form-item>
        <el-form-item :label-width="form_label_width">
          <input type="file" value="" id="file">
          <el-button style="margin-left: 10px;" size="small" type="success" @click.native="upload">上传</el-button>
        </el-form-item>     
      </el-form>  
      <span slot="footer" class="dialog-footer">
        <el-button @click="uploadDialogVisible=false">取 消</el-button>
        <el-button type="primary" @click="uploadDialogVisible = false">确 定</el-button>
      </span>      
    </el-dialog>
  </div>
</template>


<script>
import Header from '../general/Header'
import ResourceDialog from '../general/ResourceDialog'
import DefaultImg from './../../assets/fileico/generic.png'
import DocImg from './../../assets/fileico/docx_win.png'
import PdfImg from './../../assets/fileico/pdf.png'
import PptImg from './../../assets/fileico/pptx_win.png'
import JpgImg from './../../assets/fileico/jpeg.png'
import ZipImg from './../../assets/fileico/zip.png'
import RarImg from './../../assets/fileico/rar.png'
import $ from 'jquery'
export default {
  name: 'resource',
  components: { Header, ResourceDialog },
  data () {
    return {
      uploadDialogVisible: false,
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
      pdfImg: PdfImg,
      pptImg: PptImg,
      docImg: DocImg,
      jpgImg: JpgImg,
      rarImg: RarImg,
      defaultImg: DefaultImg,
      resourcesData: [],
      fileList: [],
      resourceIntro: ''
    }
  },
  methods: {
    closed: function () { alert('还未开放') },
    return_course_info_page_clicked () {
      this.$router.push({ path: ('/course/page/' + this.$route.params.course_id + '/') })
    },
    openDialog: function (id) {
      this.$store.state.id = id
      var resourceDialogSelf = this
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: '/resource/information/',
        type: 'POST',
        async: false,
        data: {'resource_id': id},
        success: function (rdata) {
          resourceDialogSelf.$store.state.name = rdata['resource_info']['name']
          $.ajax({
            url: '/user/information/',
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
          resourceDialogSelf.$store.state.size = rdata['resource_info']['size']
          resourceDialogSelf.$store.state.time = rdata['resource_info']['upload_time']
          resourceDialogSelf.$store.state.intro = rdata['resource_info']['intro']
          resourceDialogSelf.$store.state.url = rdata['resource_info']['url']
          resourceDialogSelf.$store.state.download_count = rdata['resource_info']['download_count']
          resourceDialogSelf.dialogVisible = true
        },
        error: function () {
          alert('fail')
        }
      })
    },
    upload: function () {
      var formData = new FormData()
      var fileObj = document.getElementById('file').files[0]
      formData.append('file', fileObj)
      formData.append('name', fileObj.name)
      formData.append('only_url', false)
      formData.append('url', null)
      formData.append('intro', this.resourceIntro)
      formData.append('course_code', this.$store.state.course_code)
      $.ajax({
        url: '/resourceUpload/',
        type: 'POST',
        data: formData,
        async: true,
        cache: false,
        contentType: false,
        processData: false,
        success: function (rdata) {
          rdata = JSON.parse(rdata)
          if (rdata['error'] === 0) {
            alert('上传文件成功！')
          } else {
            alert('上传失败！' + rdata['error'])
          }
        },
        error: function () {
          alert('fail')
        }
      })
    }
  },
  created: function () {
    var ss = this
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: '/course/course_info/',
      type: 'POST',
      async: false,
      data: {'course_id': this.$route.params.course_id},
      success: function (data) {
        ss.course = data['course_info']['name']
        ss.$store.state.course_code = data['course_info']['course_code']
      },
      error: function () {
        alert('fail')
      }
    })
    let resourceSelf = []
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: '/resource/id/list/',
      type: 'POST',
      async: false,
      data: {'course_id': this.$route.params.course_id},
      success: function (data) {
        for (var i = 0; i < data['resource_id_list'].length; i++) {
          $.ajax({
            ContentType: 'application/json; charset=utf-8',
            dataType: 'json',
            url: '/resource/information/',
            type: 'POST',
            async: false,
            data: {'resource_id': data['resource_id_list'][i]},
            success: function (rdata) {
              var tt = {
                col1: false,
                col2: false,
                col3: false,
                name: '全部课件.zip',
                intro: '里面整合了1~13章课件，全部是pdf格式',
                collections: 0,
                downloads: 56,
                messages: 0,
                author: '果冻',
                time: '2017-3-26',
                id: 0,
                img: ''
              }
              if (i % 3 === 0) {
                tt.col1 = true
              }
              if (i % 3 === 1) {
                tt.col2 = true
              }
              if (i % 3 === 2) {
                tt.col3 = true
              }
              tt.name = rdata['resource_info']['name']
              tt.intro = rdata['resource_info']['intro']
              tt.downloads = rdata['resource_info']['download_count']
              $.ajax({
                url: '/user/information/',
                type: 'POST',
                data: {id: rdata['resource_info']['upload_user_id']},
                async: false,
                success: function (data) {
                  data = JSON.parse(data)
                  tt.author = data['user_info']['username']
                },
                error: function () {
                  alert('fail')
                }
              })
              tt.time = rdata['resource_info']['upload_time']
              tt.id = rdata['resource_info']['id']
              tt.img = ss.defaultImg
              var tL = tt.name.length
              if (tt.name[tL - 3].toLowerCase() === 'd' && tt.name[tL - 2].toLowerCase() === 'o' && tt.name[tL - 1].toLowerCase() === 'c') {
                tt.img = ss.docImg
              }
              if (tt.name[tL - 3].toLowerCase() === 'p' && tt.name[tL - 2].toLowerCase() === 'd' && tt.name[tL - 1].toLowerCase() === 'f') {
                tt.img = ss.pdfImg
              }
              if (tt.name[tL - 3].toLowerCase() === 'p' && tt.name[tL - 2].toLowerCase() === 'p' && tt.name[tL - 1].toLowerCase() === 't') {
                tt.img = ss.pptImg
              }
              if (tt.name[tL - 3].toLowerCase() === 'z' && tt.name[tL - 2].toLowerCase() === 'i' && tt.name[tL - 1].toLowerCase() === 'p') {
                tt.img = ss.zipImg
              }
              if (tt.name[tL - 3].toLowerCase() === 'j' && tt.name[tL - 2].toLowerCase() === 'p' && tt.name[tL - 1].toLowerCase() === 'g') {
                tt.img = ss.jpgImg
              }
              if (tt.name[tL - 3].toLowerCase() === 'r' && tt.name[tL - 2].toLowerCase() === 'a' && tt.name[tL - 1].toLowerCase() === 'r') {
                tt.img = ss.rarImg
              }
              resourceSelf.push(tt)
            },
            error: function () {
              alert('fail')
            }
          })
        }
      },
      error: function () {
        alert('fail')
      }
    })
    this.resourcesData = resourceSelf
  }
}
</script>

<style scpoed>
  #resourceTitle {
    font-size: 25px;
    font-weight: bold;
    height: 100px;
    line-height: 60px;
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