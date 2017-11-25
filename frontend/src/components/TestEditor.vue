<template>
	<div >
		<Editor></Editor>
		<Editor></Editor>
	</div>
</template>

<script type="text/javascript">
import Editor from './general/Editor'
export default {
  name: 'test_editor',
  components: { Editor }
}
</script>

<style type="text/css" scoped>
  .quill{
  	height: 50px;
    width: 75px;
    .quill-editor{
      height: 50%;
      width: 75%;
    }
  }
</style>