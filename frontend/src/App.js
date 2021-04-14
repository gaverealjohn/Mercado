import React from 'react';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import { BrowserRouter as Router, Switch, Route} from "react-router-dom";

import HomePage from './components/Home';
import Login from './components/Login';
import Signup from './components/Signup';
import Activate from './components/Activate';
import ResetPassword from './components/ResetPassword';
import ResetPasswordConfirm from './components/ResetPasswordConfirm';

import { Provider } from 'react-redux';
import store from './store';

function App() {
  return (
    <Provider store={store}>
      <React.Fragment>
        <Router>
          <Switch>
            <Route exact path="/" component={HomePage} />
            <Route path="/login" component={Login} />
            <Route path="/signup" component={Signup} />
            <Route path="/activate/:uid/:token" component={Activate} />
            <Route path="/reset_password" component={ResetPassword} />
            <Route path="/password/reset/confirm/:uid/:token" component={ResetPasswordConfirm} />
          </Switch>
        </Router>
      </React.Fragment>
    </Provider>
  );
}

export default App;