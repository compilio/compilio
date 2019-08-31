<template>
  <div class="col-sm-4">
    <button type="submit" @click="launch" :name="compiler.name" :title="compiler.description">
      <i :class="'fa fa-' + compiler.icon"></i> {{ compiler.title }}
    </button>
  </div>
</template>

<script type="text/javascript">
  export default {
    name: 'compiler',
    props: ['compiler'],
    methods: {
      launch: function (event) {
        this.$emit('compile', event.target.name)
      }
    }
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
    width: 100%;

    &:hover {
      background: darken($global-light-color, 3%);
    }
  }
</style>
