import { Meteor } from 'meteor/meteor';
import { Mongo } from 'meteor/mongo';
import { check } from 'meteor/check';
import { headMenuCollection } from './collections'
const menuList = [

    {
        id: '1',
        title: '百度热搜',
        img: 'https://www.baidu.com/favicon.ico',
        children: [
            {
                id: '1-1',
                title: '热搜',
                url: '/baidu/resou'
            },
            {
                id: '1-2',
                title: '小说',
                url: '/baidu/xiaoshuo'
            },
            {
                id: '1-4',
                title: '电影',
                url: '/baidu/dianying'
            },
            {
                id: '1-5',
                title: '电视剧',
                url: '/baidu/dianshiju'
            },
            {
                id: '1-6',
                title: '动漫',
                url: '/baidu/dongman'
            },
            {
                id: '1-7',
                title: '综艺',
                url: '/baidu/zongyi'
            },
            {
                id: '1-8',
                title: '纪录片',
                url: '/baidu/jilupian'
            },
            {
                id: '1-9',
                title: '汽车',
                url: '/baidu/qiche'
            },
            {
                id: '1-10',
                title: '游戏',
                url: '/baidu/youxi'
            },
        ]
    },
    {
        id: '2',
        title: '新浪微博',
        img: 'https://img.t.sinajs.cn/t4/appstyle/searchpc/css/new_pc/img/icon_wb.png',
        children: [
            {
                id: '2-1',
                title: '热搜榜',
                url: '/sina/resou'
            },
            {
                id: '2-2',
                title: '要闻榜',
                url: '/sina/yaowen'
            },
            {
                id: '2-3',
                title: '文娱榜',
                url: '/sina/wenyu'
            }
        ]
    },
    {
        id: '3',
        title: '知乎',
        img: 'https://static.zhihu.com/heifetz/favicon.ico',
        children: [

        ]
    },
    {
        id: '4',
        title: '豆瓣',
        img: 'https://www.douban.com/favicon.ico',
        children: [
            {
                id: '4-1',
                title: '电影',
                url: '/douban/movie'
            },
            {
                id: '4-2',
                title: '音乐',
                url: '/douban/music'
            },
            {
                id: '4-3',
                title: '读书',
                url: '/douban/book'
            },
            {
                id: '4-4',
                title: '小组',
                url: '/douban/group'
            }
        ]
    },
    {
        id: '5',
        title: '网易新闻',
        img: 'https://news.163.com/favicon.ico',
        children: [
            {
                id: '5-1',
                title: '新闻',
                url: '/wangyi/news'
            },
            {
                id: '5-2',
                title: '娱乐',
                url: '/wangyi/yule'
            },
            {
                id: '5-3',
                title: '体育',
                url: '/wangyi/tiyu'
            },
            {
                id: '5-4',
                title: '汽车',
                url: '/wangyi/qiche'
            },
            {
                id: '5-5',
                title: '科技',
                url: '/wangyi/keji'
            },
            {
                id: '5-6',
                title: '家居',
                url: '/wangyi/jiaju'
            },
            {
                id: '5-7',
                title: '时尚',
                url: '/wangyi/shishang'
            },
            
        ]
    }
]


export const initMenu = () => {
    console.log('head init')
    if (headMenuCollection.find().count() === 0) {
        console.log('head size zero')
        menuList.forEach(item => {
            headMenuCollection.insert(item)
        })
    }
}
export const searchRouteText = (pathname) => {
    let data = new Object()
    menuList.forEach(item => {
        if (item.children.length !== 0) {
            item.children.forEach(child => {
                if (pathname === child.url) {
                    data.key = child.id,
                    data.ico = item.img,
                    data.name1 = item.title,
                    data.name2 = child.title
                }
            })
        }
    })
    return data
}