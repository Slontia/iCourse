
<script type="text/javascript">
/* eslint-disable brace-style */
/* eslint-disable camelcase */
/* eslint-disable space-infix-ops */
import $ from 'jquery'
import get_url from '../general/getUrl.js'
export default {
  name: 'Editor',
  components: { Header },
  data () {
    return {
      
    }
  },
  mounted () {
    var code = this.$route.query.code
    var error = 1;
    var username = ''
    var post_url = get_url(this.$store.state.dev, '/passport/auth/')
    var post_data = {
      'code': code
    }
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: post_url,
      type: 'POST',
      data: post_data,
      async: false,
      success: function (data) {
        username = data['usernmae']
        error = data['error']
      },
      error: function () {
        alert('验证大失败，容我笑一会')
      }
    })
    if (error == 0) {
      post_url = get_url(this.$store.state.dev, '/sign/login/')
      post_data = {
        'usernmae': username,
        'password': 111111111111111111111111111111
      }
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: post_url,
        type: 'POST',
        data: post_data,
        async: false,
        error: function () {
          alert('登录失败')
        }
      }) 
    }
  }
}
</script>
