import React, { useCallback, useEffect, useState } from 'react';
import { List, Pagination } from 'antd';
import { useTracker } from 'meteor/react-meteor-data';
import { weiboCollections } from '../api/collections';
import { useLocation } from 'react-router';
import "../css/weibo.css"
export default WeiBo = () => {
    const pageSize = 13;
    const [curPage, setCurPage] = useState(1)
    const onChange = (page) => {
        setCurPage(page)
    }

    const GetData = () => {
        let condition = {}
        switch (location.pathname) {
            case '/sina/resou':
                condition = {type:'hot'}
                break;
            case '/sina/yaowen':
                condition = {type:'yaowen'}
                break;
            case '/sina/wenyu':
                condition = {type:'wenyu'}
                break;
        }
        return {
            count: useTracker(() => weiboCollections.find(condition).count()),
            data: useTracker(() => weiboCollections.find(condition, { sort: { create: -1 } }).fetch())
        }
    }

    useEffect(() => {
        setCurPage(1)
    }, [location.pathname])

    return (
        <div>
            <List
                dataSource={GetData().data.slice(pageSize * (curPage - 1), pageSize * curPage)}
                renderItem={item => (
                    <List.Item key={item.id}>
                        <List.Item.Meta
                            title={
                                <div>
                                    <i className='icon-dot'></i>
                                    <a href={item.url} target="_blank">{item.title}</a>
                                </div>
                            }
                        />
                        <span>{item.hot}</span>
                    </List.Item>
                )}
            />
            <Pagination simple pageSize={pageSize} current={curPage} onChange={onChange} total={GetData().count} />
        </div>

    )
}
