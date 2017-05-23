<template>
  <div>
    <p>And selecting the compiler to run:</p>
    <div class="row">
      <div class="col-lg-12 centered" v-if="compilers.length === 0 || submitted">
        <i class="fa fa-circle-o-notch fa-spin"></i> Waiting for compilers...
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
        submitted: false
      }
    },
    methods: {
      launch (command) {
        this.submitted = true
        this.$emit('compile', command)
      }
    },
    mounted () {
      Axios.get('/compiler/list')
        .then((response) => {
          this.compilers = JSON.parse(response.data.compilers)
        })
    }
  }
</script>
