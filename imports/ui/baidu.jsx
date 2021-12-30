import React, { useState, useCallback, useEffect } from 'react';
import { useLocation } from 'react-router-dom'
import { List, Pagination } from 'antd';
import { baiduCollections } from '../api/collections';
import { useTracker } from 'meteor/react-meteor-data';
import '../css/baidu.css'
export default BaiDu = (props) => {
    const location = useLocation()
    const pageSize = 5;
    const [curPage, setCurPage] = useState(1)

    const onChange = (page) => {
        setCurPage(page)
    }

    const GetData = () => {
        // console.log(location)
        let condition = {}
        switch (location.pathname) {
            case '/baidu/resou':
                condition.type = 'hot';
                break;
            case '/baidu/xiaoshuo':
                condition.type = 'novel';
                break;
            case '/baidu/dianying':
                condition.type = 'moive';
                break;
            case '/baidu/dianshiju':
                condition.type = 'teleplay';
                break;
            case '/baidu/dongman':
                condition.type = 'cartoon';
                break;
            case '/baidu/zongyi':
                condition.type = 'variety';
                break;
            case '/baidu/jilupian':
                condition.type = 'documentary';
                break;
            case '/baidu/qiche':
                condition.type = 'car';
                break;
            case '/baidu/youxi':
                condition.type = 'game';
                break;
        }

        return {
            data: useTracker(() => baiduCollections.find(condition, { sort: { hot: -1 } }).fetch()),
            count: useTracker(() => baiduCollections.find(condition).count())
        }

    }

    useEffect(() => {
        setCurPage(1)
    }, [location.pathname])

    return (
        <div>
            <List
                itemLayout="horizontal"
                dataSource={GetData().data.slice(pageSize * (curPage - 1), pageSize * curPage)}
                renderItem={item => (
                    <List.Item>
                        <List.Item.Meta
                            avatar={<img className="hot-img" src={item.img} />}
                            title={<a href={item.url} target="_blank" >{item.title}</a>}
                            description={
                                <div className="content-box">
                                    <span>{item.author}</span>
                                    <span>{item.category}</span>
                                    <span>{item.content}</span>
                                </div>
                            }
                        />
                        <div className='hot-number-box'>
                            <span className='hot-index-number'>{item.hot}</span>
                            <span className='hot-text'>热搜指数</span>
                        </div>
                    </List.Item>
                )
                }
            />
            <Pagination simple pageSize={pageSize} current={curPage} onChange={onChange} total={GetData().count} />
        </div>
    )
}
