//import { useState } from 'react'
//import reactLogo from './assets/react.svg'
//import viteLogo from '/vite.svg'
import './Home.css'
import PoolOfImages from './PoolOfImages';

function Home() {
  return (
    <>
      <div className="container">
        <div className="row">
          <div className="col-sm-12">
            <div className="header stacked">
              <h1>My MRI Medical App</h1>
              <h6>App to load MRI images and display</h6>
            </div>
          </div>
        </div>
        <div id="main_content" className="row">
          <nav>
            <div className="nav nav-tabs my-2" id="nav-tab" role="tablist">
              <button
                className="nav-link active"
                id="nav-home-tab"
                data-bs-toggle="tab"
                data-bs-target="#nav-home"
                type="button"
                role="tab"
                aria-controls="nav-home"
                aria-selected="true"
              >
                Images
              </button>
              <button
                className="nav-link"
                id="nav-profile-tab"
                data-bs-toggle="tab"
                data-bs-target="#nav-profile"
                type="button"
                role="tab"
                aria-controls="nav-profile"
                aria-selected="false"
              >
                Operations
              </button>
              <button
                className="nav-link"
                id="nav-contact-tab"
                data-bs-toggle="tab"
                data-bs-target="#nav-contact"
                type="button"
                role="tab"
                aria-controls="nav-contact"
                aria-selected="false"
              >
                Results Viewer
              </button>
            </div>
          </nav>
          <div className="tab-content" id="nav-tabContent">
            <div
              className="tab-pane fade show active"
              id="nav-home"
              role="tabpanel"
              aria-labelledby="nav-home-tab"
            >
              <PoolOfImages></PoolOfImages>
            </div>
            <div
              className="tab-pane fade"
              id="nav-profile"
              role="tabpanel"
              aria-labelledby="nav-profile-tab"
            >
              2
            </div>
            <div
              className="tab-pane fade col-12"
              id="nav-contact"
              role="tabpanel"
              aria-labelledby="nav-contact-tab"
            >
              3
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Home;
