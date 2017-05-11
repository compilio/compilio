<template>
  <input type="file" class="drop-area" />
</template>

<script type="text/javascript">
  export default {
    name: 'drop-zone'
  }
</script>

<style scoped lang="scss" ref="stylesheet/scss">
  @import "../../scss/vars";

  input.drop-area {
    border: 2px dashed $global-light-color;
    height: 150px;
    text-align: center;
    padding-top: 60px;
    border-radius: 2px;

    &:after {
      content: 'Drop your files here';
      color: $global-light-color;
      font-size: 1.4em;
      font-weight: bold;
    }
  }
</style>
