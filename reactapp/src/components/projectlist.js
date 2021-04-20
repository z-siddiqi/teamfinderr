import React, { Component } from "react";
//import { BrowserRouter as Link } from 'react-router-dom'
//import { useHistory } from 'react-router-dom';

export default class ProjectListView extends Component {

    projectList(){
        this.props.history.push('/project-list')
    }
    
    render() {
        return (
        <>
            <div>
                <h1>Projects</h1>
                <br/>
                <h4>Search</h4>
                <div class="input-group">
                    
                    <input type="text" class="form-control" placeholder="Find a project..." aria-label="" aria-describedby="basic-addon1"/>
                    <div class="input-group-append">
                        <button class="btn btn-success" type="button">Go</button>
                    </div>
                    
                </div>
                <br/>
                <p>sort get request here - each item in list in container with join button</p>
                <br/>

            </div>

        </>
        );
    }
}
