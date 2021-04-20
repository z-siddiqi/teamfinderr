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

export default class SignUp extends Component {

    state = {
        username: '',
        email: '',
        password1: '',
        password2: ''
      }

    redirectLoginPage = event => {
        event.preventDefault();
        this.props.history.push('/sign-in');
    }
    
    handleUsernameChange = event => {
        this.setState({ username: event.target.value });
        }

    handleEmailChange = event => {
        this.setState({ email: event.target.value });
        }

    handlePasswordOneChange = event => {
        this.setState({ password1: event.target.value });
        }
    
    handlePasswordTwoChange = event => {
        this.setState({ password2: event.target.value });
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
            password1: this.state.password1,
            password2: this.state.password2

        }

        const options = {
            headers: {
                'Content-Type': 'application/json',
                'Cookie' : `csrftoken=${_csrfToken}`
            }
          };

        console.log(user)

        axios.post(`http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/`, { user }, options)
        .then(res => {
          console.log(res);
          console.log(res.data);
        })
      }


    render() {
        return (
            <>
            <form onSubmit={this.handleSubmit}
            >
                <h3>Register</h3>

                <div className="form-group">
                    <label>Username</label>
                    <input type="text" onChange={this.handleUsernameChange} className="form-control" placeholder="Enter username" />
                </div>

                <div className="form-group">
                    <label>Email</label>
                    <input type="email" onChange={this.handleEmailChange} className="form-control" placeholder="Enter email" />
                </div>

                <div className="form-group">
                    <label>Password (8 characters min.)</label>
                    <input type="password" onChange={this.handlePasswordOneChange} className="form-control" placeholder="Enter password" />
                </div>


                <div className="form-group">
                    <label> Confirm Password</label>
                    <input type="password" onChange={this.handlePasswordTwoChange} className="form-control" placeholder="Enter password" />
                </div>

                <div className="form-group">
                    <div className="custom-control custom-checkbox">
                        <input type="checkbox" className="custom-control-input" id="customCheck1" />
                        <label className="custom-control-label" htmlFor="customCheck1">Agree to Terms and Conditions</label>
                    </div>
                </div>
                <button type="submit" onSubmit={this.redirectLoginPage} className="btn btn-dark btn-lg btn-block">Register</button>
                <p className="forgot-password text-right">
                   Already registered? <button btn-primary onClick={this.redirectLoginPage} >Log in</button>
                </p>
            </form>
            </>
        );
    }
}

