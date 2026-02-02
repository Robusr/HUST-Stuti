<template>
  <div style="padding: 20px;">
    <van-button type="primary" @click="showTip">点击我（主要按钮）</van-button>
    <van-button type="success" style="margin-left: 10px;">普通成功按钮</van-button>
  </div>
</template>

<script setup>
import { showToast } from 'vant'
const showTip = () => {
  showToast('这是Vant的基础提示')
}
</script>
