<template>
	<div>
	
	</div>
</template>
<script type="text/javascript">
export default {
	name: 'Editor',
	data () {
		return {
			editor: {
				content: '',
				option: {},
				current_text_length: 0,
				current_available_text: 5000
			}
		}
	},
	props: {
		defaultMsg: {
			type: String
		},
		config: {
			type: Object
		}
	},
	mounted() {
		const _this = this
		this.editor = UE.getEditor('editor',this.config)
		this.editor.addListener("ready",function () {
			_this.editor.setContent(_this.defaultMsg)
		})
	},
	methods: {
		get_UE_content() {
			return this.editor.getContent()
		}
	},
	destroyed() {
		this.editor.destroy();
	}
}
</script>