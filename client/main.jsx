import React from 'react';
import { Meteor } from 'meteor/meteor';
import { render } from 'react-dom';
import { BrowserRouter, useNavigate } from 'react-router-dom';
import { App } from '/imports/ui/App';

Meteor.startup(() => {
  render(
    <BrowserRouter>
      <App />
    </BrowserRouter>
    , document.getElementById('react-target'));
});
