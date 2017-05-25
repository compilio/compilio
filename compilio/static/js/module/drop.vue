<template>
  <div class="col-md-6 drag-drop">
    <h3>Drag &amp; Drop</h3>
    <form action="#" method="post" @submit.prevent>
      <drop-area ref="area"></drop-area>
      <compiler-list ref="list" @compile="launch"></compiler-list>
    </form>
  </div>
</template>

<script type="text/javascript">
  import DropArea from './drop-area.vue'
  import CompilerList from './compiler-list.vue'
  import Axios from 'axios'

  export default {
    name: 'drop',
    components: {
      DropArea,
      CompilerList
    },
    data () {
      return {
        files: null
      }
    },
    methods: {
      launch (command) {
        if (this.files === null || this.files.length === 0) {
          this.$refs.list.failure()

          return
        }

        for (let i = 0; i < this.files.length; i++) {
          command += ' ' + this.files[i].name
        }

        let params = new URLSearchParams()
        params.append('command', command)

        Axios.post('/compiler/init', params)
          .then((response) => {
            let data = new FormData()
            data.append('task_id', response.data.task_id)
            data.append('0', this.files[0])

            Axios.post('/compiler/upload', data)
              .then((response) => {
                window.location.href = '/task/' + response.data.task_id
              })
          })
      }
    }
  }
</script>

<style scoped lang="scss" ref="stylesheet/scss">
  @import "../../scss/vars";

  div.drag-drop {
    padding-bottom: 10px;

    @media screen and (min-width: $global-breakpoint-medium) {
      border-right: 1px solid $global-light-color;
    }
  }
</style>
