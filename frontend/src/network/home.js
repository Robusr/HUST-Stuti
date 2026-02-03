// Robusr 2026.2.3
// 主页请求封装
import {request} from "./requestConfig.js"

export function getMainMenu(){
  return request({
    url:"main_menu/ ",
  })
}
