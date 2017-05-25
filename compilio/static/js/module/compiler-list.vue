<template>
  <div>
    <p>And selecting the compiler to run:</p>
    <div class="row">
      <div class="col-lg-12 centered" v-if="loadingMessage.length !== 0">
        <i class="fa fa-circle-o-notch fa-spin"></i> {{ loadingMessage }}
      </div>
      <compiler :compiler="compiler.fields" v-for="compiler in compilers" :key="compiler.pk" v-else @compile="launch"></compiler>
    </div>
  </div>
</template>

<script type="text/javascript">
  import Compiler from './compiler.vue'
  import Axios from 'axios'

  export default {
    name: 'compiler-list',
    components: {
      Compiler
    },
    data () {
      return {
        compilers: [],
        loadingMessage: 'Loading compilers...'
      }
    },
    methods: {
      launch (command) {
        this.loadingMessage = 'Sending data...'
        this.$emit('compile', command)
      },
      failure () {
        this.loadingMessage = ''
      }
    },
    mounted () {
      Axios.get('/compiler/list')
        .then((response) => {
          this.compilers = JSON.parse(response.data.compilers)
          this.loadingMessage = ''
        })
    }
  }
</script>
