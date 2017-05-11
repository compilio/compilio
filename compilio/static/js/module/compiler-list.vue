<template>
  <div>
    <p>And selecting the compiler to run:</p>
    <div class="row">
      <compiler :compiler="compiler" v-for="compiler in compilers" :key="compiler.id"></compiler>
    </div>
  </div>
</template>

<script type="text/javascript">
  import Compiler from './compiler.vue'

  export default {
    name: 'compiler-list',
    components: {
      Compiler
    },
    data() {
      return {
        compilers: [
          {
            id: '##id##',
            name: 'PDF LaTeX',
            description: 'Compile .tex files using PDF LaTex'
          }
        ]
      }
    }
  }
</script>
