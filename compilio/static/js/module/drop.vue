<template>
  <div class="col-md-6 drag-drop">
    <h3>Drag &amp; Drop</h3>
    <form action="#" method="post">
      <drop-area></drop-area>
      <compiler-list></compiler-list>
    </form>
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

<style scoped lang="scss" ref="stylesheet/scss">
  @import "../../scss/vars";

  div.drag-drop {
    padding-bottom: 10px;

    @media screen and (min-width: $global-breakpoint-medium) {
      border-right: 1px solid $global-light-color;
    }
  }
</style>
