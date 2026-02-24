<!--Robusr 2026.2.3-->
<!--导航栏公共组件封装-->
<template>
  <van-config-provider :theme-vars="themeVars">
    <div>
      <van-nav-bar title="HUST Stuti" />
    </div>
  </van-config-provider>
</template>

<script>
//van-config-provider组件覆盖CSS默认样式
import { ref, reactive } from 'vue';
export default {
  setup() {
    const themeVars = reactive({
      navBarBackground:'#07c160'
    });
    return{
      themeVars
    }
  }
}

</script>

<style>

</style>
