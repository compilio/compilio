<template>
  <div>
    <compiler :compiler="compiler" v-for="compiler in compilers" :key="compiler.id"></compiler>
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

<style scoped lang="scss" ref="stylesheet/scss">
  div {
    text-align: center;
  }
</style>