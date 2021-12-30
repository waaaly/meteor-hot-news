import React from 'react'
import { Routes, Route } from 'react-router-dom';
import WeiBo from './weibo'
import BaiDu from './baidu'
import Douban from './douban';
import WangYi from './wangyi'
import { useTracker } from 'meteor/react-meteor-data';
import { headMenuCollection } from '../api/collections'
export default AppContent = () => {
    const list = useTracker(() => headMenuCollection.find({}).fetch())
    return (
        <Routes>
            {
                list.map(item=>{
                    if(item.children.length != 0){
                        return item.children.map(child=>{
                            if(child.url.includes('sina')){
                                return <Route path={child.url} element={<WeiBo />}></Route>
                            }else if(child.url.includes('baidu')){
                                return <Route path={child.url} element={<BaiDu />}></Route>
                            }else if(child.url.includes('douban')){
                                return <Route path={child.url} element={<Douban />}></Route>
                            }else if(child.url.includes('wangyi')){
                                return <Route path={child.url} element={<WangYi />}></Route>
                            }
                        })
                    }
                })
            }
        </Routes>
    )
}