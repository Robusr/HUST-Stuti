<template>
  <van-nav-bar title="HUST Stuti" />
  <van-search placeholder="请输入搜索关键词" />
  <van-tabbar>
    <van-tabbar-item icon="home-o">首页</van-tabbar-item>
    <van-tabbar-item icon="search">书籍</van-tabbar-item>
    <van-tabbar-item icon="friends-o">交易</van-tabbar-item>
    <van-tabbar-item icon="setting-o">个人</van-tabbar-item>
  </van-tabbar>
</template>

<script setup>
  import {getMainMenu} from "@/network/home.js";
  getMainMenu().then(res=>{
    console.log(res)
  })
</script>
