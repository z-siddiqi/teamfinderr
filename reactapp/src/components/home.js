import React, { Component } from "react";
//import { BrowserRouter as Link } from 'react-router-dom'
//import { useHistory } from 'react-router-dom';

export default class Home extends Component {

    handleClick() {
        
        this.props.history.push('/sign-in');
    }
    
    render() {
        return (
            <>
            <form>
                <h3>Home Page</h3>

                <button type="submit" onClick={() => this.handleClick()} className="btn btn-dark btn-lg btn-block">Sign Out</button>

            </form>
            </>
        );
    }
}

