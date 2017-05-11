<template>
  <div class="col-sm-4">
    <button type="submit"><i class="fa fa-file-pdf-o"></i> PDF LaTeX</button>
  </div>
</template>

<script type="text/javascript">
  export default {
    name: 'compiler',
    props: ['video']
  }
</script>

<style scoped lang="scss" ref="stylesheet/scss">
  @import "../../scss/vars";

  button {
    border-radius: 4px;
    display: block;
    padding: 7px 10px;
    background: $global-light-color;
    text-align: center;
    border: 0;
    cursor: pointer;

    &:hover {
      background: darken($global-light-color, 3%);
    }
  }
</style>
