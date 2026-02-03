<template>
  <van-nav-bar title="HUST Stuti" />
  <van-grid :gutter="10">
    <van-grid-item v-for="value in 8" :key="value" icon="photo-o" text="文字" />
  </van-grid>
  <van-tabbar>
    <van-tabbar-item icon="home-o">首页</van-tabbar-item>
    <van-tabbar-item icon="search">书籍</van-tabbar-item>
    <van-tabbar-item icon="friends-o">交易</van-tabbar-item>
    <van-tabbar-item icon="setting-o">个人</van-tabbar-item>
  </van-tabbar>
</template>

<script setup>

</script>
