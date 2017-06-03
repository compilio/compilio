<template>
    <div class="terminal">
        <p v-if="trace === ''">
            <span class="line"><i class="fa fa-refresh fa-spin"></i> Waiting for execution trace...</span>
        </p>
        <p v-else>
            <span class="line" v-for="line in trace.split('\n')" v-if="line !== ''">{{ line }}</span>
            <span v-if="state === 'COMPILING'"><i class="fa fa-refresh fa-spin"></i> Task is still being executed...</span>
        </p>
    </div>
</template>

<script type="text/javascript">
  import Axios from 'axios'

  export default {
    name: 'drop-area',
    data () {
      return {
        trace: '',
        task: '',
        state: ''
      }
    },
    beforeMount: function () {
      this.task = this.$el.attributes['data-task'].value
      this.state = this.$el.attributes['data-state'].value
    },
    methods: {
      loadTrace () {
        Axios.get('/compiler/task?task_id=' + this.task)
          .then((response) => {
            if (response.data.state !== this.state) {
              location.reload()
            } else {
              this.trace = response.data.output_log
            }
          })
      }
    },
    mounted: function () {
      this.loadTrace()

      if (['PENDING', 'COMPILING'].indexOf(this.state) === -1) {
        return
      }

      setInterval(function () {
        this.loadTrace()
      }.bind(this), 3000)
    }
  }
</script>
