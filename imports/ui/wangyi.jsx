import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router';
import { wangyiCollections } from '../api/collections'
import { List, Pagination } from 'antd';
import { useTracker } from 'meteor/react-meteor-data';
export default WangYi = () => {
  const location = useLocation();
  const [curPage, setCurPage] = useState(1)
  const pageSize = 15;
  const GetData = () => {
    let condition = { type: location.pathname.split('/')[2] }

    return {
      count: useTracker(() => wangyiCollections.find(condition).count()),
      data: useTracker(() => wangyiCollections.find(condition, { sort: { create: -1 } }).fetch())
    }

  }
  const onChange = (page) => {
    setCurPage(page)
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