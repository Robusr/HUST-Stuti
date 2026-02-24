<!--Robusr 2026.2.3-->
<!--导航栏公共组件封装-->
<template>
<!--  <van-config-provider :theme-vars="themeVars">-->
  <van-config-provider>
    <div>
      <van-nav-bar title="HUST Stuti" />
    </div>
  </van-config-provider>
</template>

<script setup>
// //van-config-provider组件覆盖CSS默认样式
// import { ref, reactive } from 'vue';
//
// // export default {
// //   setup() {
// //     const themeVars = reactive({
// //       navBarBackground:'#09316a',
// //       navBarTitleTextColor:'#FFFFFF'
// //     });
// //     return{
// //       themeVars
// //     }
// //   }
// // }
//
// //Vue3 setup语法糖写法
//     const themeVars = reactive({
//       navBarBackground:'#09316a',
//       navBarTitleTextColor:'#FFFFFF'
//     });
</script>

<style>

</style>
