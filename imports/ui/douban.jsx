import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router';
import { useTracker } from 'meteor/react-meteor-data';
import { douBanCollections } from '../api/collections'
import { Card, Row, Col, Pagination, Rate, Tooltip, Descriptions, List } from 'antd';
import '../css/douban.css'
export default DouBan = () => {
  const location = useLocation();
  const [curPage, setCurPage] = useState(1)
  const [pageSize, setPageSize] = useState(12)

  const GetData = () => {
    let condition = {}
    switch (location.pathname) {
      case '/douban/movie':
        condition = { type: 'movie' }
        break;
      case '/douban/music':
        condition = { type: 'music' }
        break;
      case '/douban/book':
        condition = { type: 'book' }
        break;
      case '/douban/group':
        condition = { type: 'group' }
        break;
    }
    return {
      count: useTracker(() => douBanCollections.find(condition).count()),
      data: useTracker(() => douBanCollections.find(condition, { sort: { create: -1 } }).fetch())
    }
  }

  const onChange = (page) => {
    setCurPage(page)
  }

  useEffect(() => {
    setCurPage(1)
  }, [location.pathname])

  const Render = () => {
    switch (location.pathname) {
      case '/douban/movie':
        return Movie();
      case '/douban/music':
        return Music();
      case '/douban/book':
        return Book();
      case '/douban/group':
        return Group();
      default:
        return null;
    }
  }

  const Movie = () => {
    setPageSize(12)
    return (
      <Row gutter={16}>
        {
          GetData().data.slice(pageSize * (curPage - 1), pageSize * curPage).map(item => {
            return (
              <Tooltip key={item.title} title={MovieDetail(item)} placement="leftTop" color="#001529">
                <Col span={4} style={{ marginBottom: '8px' }} onClick={() => { window.open(item.url) }}>
                  <Card
                    hoverable
                    style={{ width: 190 }}
                    cover={<img alt={item.title} src={item.img} referrerPolicy="no-referrer" />}
                  >
                    <Card.Meta title={item.title}
                      description={
                        <div>
                          {
                            item.rate.length !== 0 ?
                              <div>
                                <Rate allowHalf disabled defaultValue={(Number(item.rate) / 10) * 5} count={5} />
                                {item.rate}({item.rater})评价
                              </div> :
                              <p>暂无评分</p>
                          }
                        </div>
                      } />
                  </Card>
                </Col>
              </Tooltip>
            )
          })
        }
      </Row>
    )
  }

  const MovieDetail = (data) => {
    return (
      <Descriptions title={data.title}>
        <Descriptions.Item label="上映">{data.release}年</Descriptions.Item>
        <Descriptions.Item label="地区">{data.region}</Descriptions.Item>
        <Descriptions.Item label="片长">{data.duration}</Descriptions.Item>
        <Descriptions.Item label="导演">{data.director}</Descriptions.Item>
        <Descriptions.Item label="演员">{data.actors}</Descriptions.Item>
      </Descriptions>
    )
  }

  const Music = () => {
    setPageSize(10)
    return (
      <List
        itemLayout="horizontal"
        dataSource={GetData().data.slice(pageSize * (curPage - 1), pageSize * curPage)}
        renderItem={item => (
          <List.Item>
            <List.Item.Meta
              avatar={<img className="music-img" src={item.img} referrerPolicy="no-referrer" />}
              title={<a href={item.url} target="_blank">{item.title}</a>}
              description={item.actors}
            />
            <div className='music-number-box'>
              <span className='music-index-number'>{item.release}</span>
            </div>
          </List.Item>
        )
        }
      />
    )
  }
  const Book = () => {
    setPageSize(16)
    return (
      <Row gutter={16}>
        {
          GetData().data.slice(pageSize * (curPage - 1), pageSize * curPage).map(item => {
            return (
              <Col span={6} style={{ marginBottom: '8px' }} onClick={() => { window.open(item.url) }}>
                <Card style={{ width: 300, marginTop: 16 }}>
                  <Card.Meta
                    avatar={<img className="book-img" src={item.img} referrerPolicy="no-referrer" />}
                    title={item.title}
                    description={
                      <div className="content-box">
                        <span>{item.actors}</span>
                        <span>{item.category}</span>
                        <span>{item.content}</span>
                      </div>
                    }
                  />
                </Card>
              </Col>
            )
          })
        }
      </Row>
    )
  }
  const Group = () => {
    setPageSize(5)
    return (
      <List
        itemLayout="vertical"
        size="large"
        dataSource={GetData().data.slice(pageSize * (curPage - 1), pageSize * curPage)}
        renderItem={item => (
          <List.Item
            key={item.title}
            actions={[
              <div key="1">来自
                <a href={item.gUrl} target="_blank">{item.actors}</a>
              </div>,
              <span key="2">{item.release}</span>,
            ]}
            extra={
              item.img.length != 0 ?
                <img  alt="logo" className="group-img" src={item.img} referrerPolicy="no-referrer" /> :
                null
            }
          >
            <List.Item.Meta
              avatar={
                <div className='group-likes'>
                  {item.rater.replace(/喜欢/g, "")}
                  <br />
                  喜欢
                </div>
              }
              title={<a href={item.url} target="_blank">{item.title}</a>}
              description={<span>{item.content}</span>}
            />
          </List.Item>
        )}
      />
    )
  }
  return (
    <div>
      <Render />
      <Pagination simple pageSize={pageSize} current={curPage} onChange={onChange} total={GetData().count} />
    </div>
  )
}

