<template>
    <div class="terminal">
        <p>
            <span class="line" v-if="trace === ''"><i class="fa fa-refresh fa-spin"></i> Loading execution trace...</span>
        </p>
    </div>
</template>

<script type="text/javascript">
  export default {
    name: 'drop-area',
    data () {
      return {
        trace: ''
      }
    }
  }
</script>
