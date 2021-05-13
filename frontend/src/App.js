import React from 'react';
import './App.css';

import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { Provider } from 'react-redux';

import Layout from './hocs/Layout';
import Home from './containers/Home';
import Login from './containers/Login';
import Signup from './containers/Signup';
import Activate from './containers/Activate';
import ResetPassword from './containers/ResetPassword';
import ResetPasswordConfirm from './containers/ResetPasswordConfirm';
import Product from './containers/Product';
import Profile from './containers/Profile';

import store from './store';

function App() {
  return (
    <Provider store={store}>
      <Router>
        <Layout>
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/login" component={Login} />
            <Route path="/signup" component={Signup} />
            <Route path="/activate/:uid/:token" component={Activate} />
            <Route path="/reset_password" component={ResetPassword} />
            <Route path="/password/reset/confirm/:uid/:token" component={ResetPasswordConfirm} />
            <Route path="/product/:id" component={Product} />
            <Route path="/profile" component={Profile} />
          </Switch>
        </Layout>
      </Router>
    </Provider>
  );
}

export default App;