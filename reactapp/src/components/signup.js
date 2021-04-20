import React, { Component } from "react";
//import { BrowserRouter as Link } from 'react-router-dom'



export default class SignUp extends Component {
    
    render() {
        return (
            <>
            <form>
                <h3>Register</h3>

                <div className="form-group">
                    <label>username</label>
                    <input type="text" className="form-control" placeholder="First name" />
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
                    <label> Confirm Password</label>
                    <input type="password" className="form-control" placeholder="Enter password" />
                </div>

                <div className="form-group">
                    <div className="custom-control custom-checkbox">
                        <input type="checkbox" className="custom-control-input" id="customCheck1" />
                        <label className="custom-control-label" htmlFor="customCheck1">Agree to Terms and Conditions</label>
                    </div>
                </div>

                <button type="submit" className="btn btn-dark btn-lg btn-block">Register</button>
                <p className="forgot-password text-right">
                    <button>Already registered?</button>
                </p>
            </form>
            </>
        );
    }
}

