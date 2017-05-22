<template>
  <div>
    <label for="drop-area">Compile your files by dropping them on the following area:</label>
    <input id="drop-area" type="file" class="drop-area" multiple v-bind="files" />
  </div>
</template>

<script type="text/javascript">
  export default {
    name: 'drop-area',
    data () {
      return {
        files: null
      }
    }
  }
</script>

<style scoped lang="scss" ref="stylesheet/scss">
  @import "../../scss/vars";

  input.drop-area {
    border: 2px dashed $global-light-color;
    border-radius: 2px;
    width: 100%;
    padding: 80px 10px;
    display: block;
    margin: 0 auto;
  }
</style>
