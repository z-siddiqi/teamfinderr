import React, { Component } from "react";
import axios from "axios";

const API_HOST = 'http://localhost:8000';

let _csrfToken = null;

async function getCsrfToken() {
    if (_csrfToken === null) {
      const response = await fetch(`${API_HOST}/csrf/`, {
        credentials: 'include',
      });
      const data = await response.json();
      _csrfToken = data.csrfToken;
    }
    return _csrfToken;
  }
  
export default class Login extends Component {

    state = {
        username: '',
        email: '',
        password: ''
      }

    redirectHome = event => {
        event.preventDefault();
        this.props.history.push('/home');
    }

    redirectForgotPassword = event => {
        event.preventDefault();
        this.props.history.push('/password-change')
    }

    handleUsernameChange = event => {
        this.setState({ username: event.target.value });
        }

    handleEmailChange = event => {
        this.setState({ email: event.target.value });
        }

    handlePasswordChange = event => {
        this.setState({ password: event.target.value });
        }

    async componentDidMount() {
        _csrfToken = await getCsrfToken();
        }

    handleSubmit = (event) => {
        event.preventDefault();
       
        console.log(_csrfToken);

        const user = {
            username: this.state.username,
            email: this.state.email,
            password: this.state.password

        }

        const options = {
            headers: {
                'Content-Type': 'application/json',
                'Cookie' : `csrftoken=${_csrfToken}`
            }
          };

        console.log(user)

        axios.post(`http://127.0.0.1:8000/api/v1/dj-rest-auth/login/`, { user }, options)
        .then(res => {
          console.log(res);
          console.log(res.data);
        })
      }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>

                <h3>Login</h3>

                <div className="form-group">
                    <label>Username</label>
                    <input type="text" name="username" onChange={this.handleUsernameChange} className="form-control" placeholder="Enter username" />
                </div>

                <div className="form-group">
                    <label>Email</label>
                    <input type="text" name="email" onChange={this.handleEmailChange} className="form-control" placeholder="Enter email" />
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input type="text" name="password" onChange={this.handlePasswordChange} className="form-control" placeholder="Enter password" />
                </div>

                <div className="form-group">
                    <div className="custom-control custom-checkbox">
                        <input type="checkbox" className="custom-control-input" id="customCheck1" />
                        <label className="custom-control-label" htmlFor="customCheck1">Remember me</label>
                    </div>
                </div>

                <button type="submit" onSubmit={this.redirectHome} className="btn btn-dark btn-lg btn-block">Sign in</button>
                <p className="forgot-password text-right">
                    <button onClick={this.redirectForgotPassword}>Forgot password?</button>
                </p>
            </form>
        );
    }
}

