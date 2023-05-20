<script>
export default {
  name: 'chat-box',
  data() {
    return {}
  },
  props: {
    something: {
        type: Object,
        default: null
    },
    isSender: {
      type: Boolean,
      default: false
    }
  },
  methods: {}
}
</script>

<template>
  <div class="p-3 rounded-lg" :class="{'col-start-1 col-end-8': isSender, 'col-start-6 col-end-13': !isSender}">
    <div class="flex items-center justify-start">
      <div class="relative mr-3 text-sm py-2 px-4 shadow rounded-xl" :class="{'bg-white': isSender , 'bg-indigo-100': !isSender}">
        <div v-html="something.text"></div>
      </div>
    </div>
  </div>
  
</template>

<style scoped>

</style>
