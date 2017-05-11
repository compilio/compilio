<template>
  <div>
    <drop-area></drop-area>
    <compiler-list></compiler-list>
  </div>
</template>

<script type="text/javascript">
  import DropArea from './drop-area.vue'
  import CompilerList from './compiler-list.vue'

  export default {
    name: 'drop',
    components: {
      DropArea,
      CompilerList
    }
  }
</script>
