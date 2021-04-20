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
        <div>
        <h1>Home</h1>
        <h4>Search</h4>
        <div class="input-group">
            
            <input type="text" class="form-control" placeholder="Find a member..." aria-label="" aria-describedby="basic-addon1"/>
            <div class="input-group-append">
                <button class="btn btn-success" type="button">Go</button>
            </div>
            
        </div>
        <br/>
        <div class="card">
            <div class="card-body">
                <h4 class="card-title">My Projects</h4>
                <p class="card-text">
                    get existing projects as a list
                </p>
                <a href="#!" class="btn btn-primary btn-block">Go to my projects</a>
            </div>
        </div>
        <br/>
        <form>
            <h4>Create a project</h4>
            <div class="form-group">
                <label for="formGroupExampleInput">Project Name</label>
                <input type="text" class="form-control" id="formGroupExampleInput" placeholder="Enter project name"/>
            </div>
            <div class="form-group">
                <label for="formGroupExampleInput2">Description</label>
                <input type="text" class="form-control" id="formGroupExampleInput2" placeholder="Enter project description"/>
            </div>
            <button class="btn btn-success" type="button">Submit</button>
        </form>
        <br/>
        <button class="btn btn-primary btn-block" type="button">Join a new project</button>
        <br/>
            

        </div>

        </>
        );
    }
}

