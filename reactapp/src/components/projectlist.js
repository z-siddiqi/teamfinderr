import React, { Component } from "react";
import axios from "axios";
//import { BrowserRouter as Link } from 'react-router-dom'
//import { useHistory } from 'react-router-dom';

export default class ProjectListView extends Component {

    state = {
        projects: [],
        project: {},
        isProjectViewOn: false,
        sortValue: '',
        inputValue: '',

    }

    projectList(){
        this.props.history.push('/project-list')
    }

    fetchProjects = async () => {
    const { data } = await axios.get(
        "http://127.0.0.1:8000/api/v1/projects/"
    );
    console.log(data);
    return { data };
    };


    
    render() {
        return (
        <>
            <div  onLoad = {this.fetchProjects}>
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
