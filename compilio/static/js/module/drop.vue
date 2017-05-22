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
    methods: {
      launch (command) {
        let params = new URLSearchParams()
        params.append('command', command)

        Axios.post('/compiler/init', params)
          .then(function (response) {
            window.location.href = '/task/' + response.data.task_id
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
