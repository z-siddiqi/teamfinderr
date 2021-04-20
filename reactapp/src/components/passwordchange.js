import React, { Component } from "react";

class PasswordChange extends Component {
    state = {  }
    render() { 
        return(
            <>
            <form>

                <h3>Forgot Password?</h3>

                <div className="form-group">
                    <label>Username</label>
                    <input type="username" className="form-control" placeholder="Enter username" />
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input type="password" className="form-control" placeholder="Enter password" />
                </div>

                <div className="form-group">
                    <label>Confirm Password</label>
                    <input type="password" className="form-control" placeholder="Enter password" />
                </div>

                <button type="submit" onClick={() => this.handleClick()} className="btn btn-dark btn-lg btn-block">Submit</button>
            </form> 
            </>

        );
    }
}
 
export default PasswordChange;

// TO-DO 

