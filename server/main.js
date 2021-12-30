import { Meteor } from 'meteor/meteor';
import { initMenu } from '../imports/api/headMenu';
import { weiboInit } from '../imports/api/weibo';
import { baiduInit } from '../imports/api/baidu';
import { doubanInit } from '../imports/api/douban';
import { wangyiInit } from '../imports/api/wangyi'

/**
 * 最怕问初衷
 * 幻梦成空
 * 年少立志三千里
 * 踌躇百步无寸功
 * 转眼高堂皆白发
 * 儿女蹒跚学堂中
 * 碎银几两催人老
 * 心仍少
 * 皱纹悄然上眉中
 * 浮生醉酒回梦里
 * 青春仍依旧
 * 只叹时光太匆匆
 * 
 * 最怕问初衷
 * 大梦成空
 * 眉间鬓上老英雄
 * 剑甲鞮侔封厚土
 * 说甚擒龙
 * 壮志付西风
 * 逝去无踪
 * 少年早作一闲翁
 * 诗酒琴棋终日里
 * 岁月匆匆
 */
Meteor.startup(() => {
  if (Meteor.isServer) {
    // 初始化头部目录
    initMenu();

    baiduInit();

    weiboInit();

    doubanInit();
    wangyiInit();
  }

});



