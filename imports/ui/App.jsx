import React, { useState, useEffect } from 'react';
import { Layout, Breadcrumb } from 'antd';
import { useNavigate, useLocation } from 'react-router-dom';
import { searchRouteText } from '../api/headMenu'
import AppHeader from './header'
import AppContent from './content'
import 'antd/dist/antd.css'
import '../css/app.css'
const { Content, Footer } = Layout;

export const App = () => {
  const navigate = useNavigate()
  const location = useLocation()
  const [headerData, setHeaderText] = useState([1, "https://www.baidu.com/favicon.ico", '百度热搜', '热搜'])
  // console.log(navigate)
  useEffect(() => {
    if (location.pathname === '/') {
      navigate('/baidu/resou', { replace: true });
    } else {
      data = [
        searchRouteText(location.pathname).key,
        searchRouteText(location.pathname).ico,
        searchRouteText(location.pathname).name1,
        searchRouteText(location.pathname).name2,
      ]
      console.log(data)
      setHeaderText(data)
    }
  }, [location.pathname])
  return (
    <Layout className="app-layout">
      <AppHeader changeHeaderText={(data) => setHeaderText(data)} defaultKey={headerData[0]} />
      <Content className="content">
        <Breadcrumb style={{ margin: '20px 0' }}>
          <Breadcrumb.Item>
            <img style={{ height: '16px', width: '16px' }} src={headerData[1]} />
            {headerData[2]}
          </Breadcrumb.Item>
          <Breadcrumb.Item>{headerData[3]}</Breadcrumb.Item>
        </Breadcrumb>
        <div className="site-layout-content">
          <AppContent />
        </div>
      </Content>
      <Footer className='footer'>1.12.246.138 ©2021 Created by charon</Footer>
    </Layout>
  )
}



