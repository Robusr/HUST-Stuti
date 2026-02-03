// Robusr 2026.2.3
// 前端网络请求封装
import axios from "axios";

export function request(config){
  const instance  = axios.create({
    baseURL:"http://localhost:8000",
    timeout:5000,
  })

  // 请求拦截
  instance.interceptors.request.use(config=>{
    // 为某些实例加上token

    // 直接放行
    return config;
  },err=>{
    // 错误响应
  })

  // 响应拦截
  instance.interceptors.response.use(res=>{
    return res.data?res.data:res;
  },err=>{
    // 响应错误处理
    // 跳转待定处理页面
  })

  return instance(config);
}
