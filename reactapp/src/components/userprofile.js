import React, { Component } from "react";

class UserProfileView extends Component {
    state = {  }
    render() { 
        return (
        <>
        <div>

            <div class="card">
                <img class="card-img-top" src="/images/pathToYourImage.png" alt="Card image cap"/>
                <div class="card-body">
                    <h4 class="card-title">Bio</h4>
                    <p class="card-text">
                        get bio
                    </p>
                    <a href="#!" class="btn btn-primary">Edit</a>
                </div>
            </div>

            <div class="card">
                <div class="card-body">
                    <h4 class="card-title">Skills</h4>
                    <p class="card-text">
                        get as a list
                    </p>
                    <a href="#!" class="btn btn-primary">Edit</a>
                </div>
            </div>

        </div>

        </>
        );
    }
}
 
export default UserProfileView;


// TODO
// Get user profile bio details
// Get user skills
// add edit hyperlink to edit bio and skills 

