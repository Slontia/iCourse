<template>
  <div id="Carousel" class="carousel">
    <h2 class="demonstration">北 航 课 程 资 源 下 载 站</h2>
    <el-carousel :intervel="carousel_interval" height="500px" arrow="never">
      <el-carousel-item :key="de1">
        <img :src="carousel_image1" height="100%" width="100%">
      </el-carousel-item>
    </el-carousel>
  </div>
  </div>
</template>

<script type="text/javascript">
/* eslint-disable camelcase */
import carousel_image1 from '../../assets/carousel_image.jpg'
export default {
  name: 'Carousel',
  data () {
    return {
      carousel_interval: 5000,
      carousel_image1: carousel_image1
    }
  }
}
</script>

<style type="text/css">
  .carousel{
    position: absolute;
    top:60px;
    margin-top: 20px;
    width: 100%;
  }
  .demonstration{
    font-size: 30px;
    font-weight: 100;
    font-family: Microsoft Yahei;
    text-align: center;
    color:#20a0ff;
  }
</style>