import { weiboCollections } from './collections'
import { Meteor } from 'meteor/meteor'
import { PythonShell } from 'python-shell'

export const weiboInit = () => {
  if (weiboCollections.find().count() === 0) {
    PythonShell.runString(Assets.getText('weibo.py'), null, function (err, results) {
      if (err) {
        console.log(err)
      }
      console.log(results)
      // script finished
    });
  }
  Meteor.setInterval(() => {
    PythonShell.runString(Assets.getText('weibo.py'), null, function (err, results) {
      if (err) {
        console.log(err)
      }
      console.log(results)
      // script finished
    });
  }, 1000 * 30 * 5)
}