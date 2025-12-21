<script setup>
import { ref } from 'vue'

defineProps({
  text: String,
})

const isVisible = ref(false)
</script>

<template>
  <div class="tooltip-container" @mouseenter="isVisible = true" @mouseleave="isVisible = false">
    <div v-if="isVisible" class="tooltip-box">
      {{ text }}
    </div>
  </div>
</template>

<style scoped>
.tooltip-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
.tooltip-box {
  position: absolute;
  top: 0;
  left: 0;
  transform: translate3d(-70%, -40%, 0);
  background-color: #333;
  color: white;
  padding: 5px 10px;
  border-radius: 4px;
  font-size: 12px;
  white-space: nowrap;
  z-index: 100;
}
</style>
