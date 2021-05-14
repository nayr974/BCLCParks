import React from "react";
import "./App.css";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import BookingBoard from "components/booking/BookingBoard";
import Redemption from "components/redemption/Redemption";
import { Button, Popconfirm, Space, Row, Col } from "antd";
import styles from "./App.module.css";

function App() {
  return (
    <Router>
      <div className="App" className={styles.bg}>
        <div className="AppContainer">
          <div>
            <div className={styles.header}>
              <img
                src={"/img/BCLC_Logo.svg"}
                style={{ height: "30px" }}
                alt="BC(LC)Parks Logo"
              />
              <img
                src={"/img/logo-bcparks-text.png"}
                style={{ height: "30px" }}
                alt="BC(LC)Parks Logo"
              />
              <div className={styles.titleContainer}>
                <span className={styles.subtitle}>
                  Your chance to win a lifetime experience at one BC park
                </span>
              </div>
              <Space className={styles.buttons}>
                <div></div>
              </Space>
            </div>
            <div className={styles.page}>
              <Switch>
                <Route path="/redeem">
                  <Redemption />
                </Route>
                <Route path="/">
                  <BookingBoard />
                </Route>
              </Switch>
            </div>
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App;
