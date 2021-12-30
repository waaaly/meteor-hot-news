import React from 'react';
import { Layout, Menu, } from 'antd';
import { useTracker } from 'meteor/react-meteor-data';
import { headMenuCollection } from '../api/collections';
import { Link } from 'react-router-dom';
const { Header } = Layout;

export default AppHeader = (props) => {
    const headList = useTracker(() => headMenuCollection.find({}).fetch());
    const onLinkClick = (item, child) => {
        props.changeHeaderText([child.id,item.img,item.title, child.title])
    }
    return (
        <Header>
            <div className="logo" />
            <Menu theme="dark" mode="horizontal" defaultSelectedKeys={[props.defaultKey]}>
                {headList.map((item, index) => {
                    if (item.children.length == 0) {
                        return <Menu.Item key={item.id}>{item.title}</Menu.Item>;
                    } else {
                        return (
                            <Menu.SubMenu key={item.id} title={item.title}>
                                {
                                    item.children.map(child => {
                                        return (
                                            <Menu.Item key={child.id}>
                                                <Link onClick={() => onLinkClick(item, child)} to={child.url}>{child.title}</Link>
                                            </Menu.Item>)
                                    })
                                }
                            </Menu.SubMenu>
                        )
                    }
                })}
            </Menu>
        </Header>
    )
}