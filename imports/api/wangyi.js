import { Meteor } from 'meteor/meteor'
import { wangyiCollections } from './collections'
import { PythonShell } from 'python-shell'
export const wangyiInit = () => {
    if (wangyiCollections.find().count() === 0) {
        PythonShell.runString(Assets.getText('wangyi.py'), null, function (err, results) {
            if (err) {
                console.log(err)
            }
            console.log(results)
            // script finished
        });
    }
    Meteor.setInterval(() => {
        PythonShell.runString(Assets.getText('wangyi.py'), null, function (err, results) {
            if (err) {
                console.log(err)
            }
            console.log(results)
            // script finished
        });
    }, 1000 * 50 * 5)

}
