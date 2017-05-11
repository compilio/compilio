<template>
    <a href="#"><i class="fa fa-file-pdf-o"></i> PDF LaTeX</a>
</template>

<script type="text/javascript">
  export default {
    name: 'compiler',
    props: ['video']
  }
</script>

<style scoped lang="scss" ref="stylesheet/scss">
  @import "../../scss/vars";

  a {
    border-radius: 4px;
    display: block;
    padding: 3px;
    background: $global-light-color;

    &:hover {
      background: darken($global-light-color, 3%);
    }
  }
</style>
