import { douBanCollections } from './collections';
import { Meteor } from 'meteor/meteor'
import { PythonShell } from 'python-shell'
export const doubanInit = () => {
  if (douBanCollections.find().count() === 0) {
    PythonShell.runString(Assets.getText('douban.py'), null, function (err, results) {
      if (err) {
        console.log(err)
      }
      console.log(results)
      // script finished
    });
  }
  Meteor.setInterval(() => {
    PythonShell.runString(Assets.getText('douban.py'), null, function (err, results) {
      if (err) {
        console.log(err)
      }
      console.log(results)
      // script finished
    });
  },1000*60*5)
}