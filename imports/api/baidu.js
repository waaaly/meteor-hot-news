import { baiduCollections } from './collections'
import { Meteor } from 'meteor/meteor'
import { PythonShell } from 'python-shell'
export const baiduInit = () => {
  if (baiduCollections.find().count() === 0) {
    PythonShell.runString(Assets.getText('baidu.py'), null, function (err, results) {
      if (err) {
        console.log(err)
      }
      console.log(results)
      // script finished
    });
  }
  Meteor.setInterval(() => {
    PythonShell.runString(Assets.getText('baidu.py'), null, function (err, results) {
      if (err) {
        console.log(err)
      }
      console.log(results)
      // script finished
    });
  },1000*40*5)
}