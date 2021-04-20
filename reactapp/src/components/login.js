import React, { Component } from "react";

export default class Login extends Component {

    handleClick() {
        this.props.history.push('/home');
    }

    forgotPassword(){
        this.props.history.push('/password-change')
    }

    render() {
        return (
            <form>

                <h3>Log in</h3>

                <div className="form-group">
                    <label>Username</label>
                    <input type="username" className="form-control" placeholder="Enter username" />
                </div>

                <div className="form-group">
                    <label>Email</label>
                    <input type="email" className="form-control" placeholder="Enter email" />
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input type="password" className="form-control" placeholder="Enter password" />
                </div>

                <div className="form-group">
                    <div className="custom-control custom-checkbox">
                        <input type="checkbox" className="custom-control-input" id="customCheck1" />
                        <label className="custom-control-label" htmlFor="customCheck1">Remember me</label>
                    </div>
                </div>

                <button type="submit" onClick={() => this.handleClick()} className="btn btn-dark btn-lg btn-block">Sign in</button>
                <p className="forgot-password text-right">
                    <button onClick={() => this.forgotPassword()}>Forgot password?</button>
                </p>
            </form>
        );
    }
}