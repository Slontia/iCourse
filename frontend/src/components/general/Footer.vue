<template>
	<footer id="Footer" class="footer">	
		<div align="center"><hr class="line"></div>
		<div class="footer-main">
			<p class="footer_copyright"> © 2017 hotcode5</p>
			<p class="footer_link_container">
				<a href="http://baidu.com" target="_blank" class="footer_link">Github</a>
				<a href="http://www.cnblogs.com/hotcode5/" target="_blank" class="footer_link">blog</a>
			</p>
		</div>
	</footer>
</template>

<script type="text/javascript">
	
</script>

<style type="text/css">
	.line{
		width: 90%;
		height: 0px;
	}
	.footer{
		position: absolute;
		font-family: Microsoft Yahei;
		background-size: 100%;
		//background-color: #58B7FF;
		width: 100%;
		height: 100px;
		text-align: center;
		margin-top: 50px;
	}
	.footer_link_container{
		margin-top: 10px;
	}
	.footer_link{
		text-decoration: none;
		margin-right: 25px;
		margin-left: 25px;
		color: #409EFF;
	}
	.footer_copyright{
		padding-top: 20px;
		color:gray;
	}
</style>