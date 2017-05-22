<template>
  <div>
    <p>And selecting the compiler to run:</p>
    <div class="row">
      <compiler :compiler="compiler.fields" v-for="compiler in compilers" :key="compiler.pk"></compiler>
      <div class="col-lg-12 centered" v-if="compilers.length === 0">
        <i class="fa fa-circle-o-notch fa-spin"></i> Loading compilers...
      </div>
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
        compilers: []
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
