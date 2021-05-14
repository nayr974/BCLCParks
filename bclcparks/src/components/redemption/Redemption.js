import { useSelector, useDispatch } from "react-redux";
import { Space, Row, Col, Typography } from "antd";
import { groupBy, uniq } from "lodash";
import { Wheel } from "react-custom-roulette";
import React, { useState } from "react";
import styles from "./Redemption.module.css";

const data = [
  {
    option: "asphalt jungle",
    style: { backgroundColor: "#222", textColor: "white" },
  },
  {
    option: "burg",
    style: { backgroundColor: "darkgray", textColor: "white" },
  },
  {
    option: "A beautiful park",
    style: { backgroundColor: "green", textColor: "black" },
  },
  {
    option: "megalopolis",
    style: { backgroundColor: "#222", textColor: "white" },
  },
  {
    option: "town",
    style: { backgroundColor: "lightgray", textColor: "black" },
  },
  {
    option: "metropolis",
    style: { backgroundColor: "darkgray", textColor: "white" },
  },
  {
    option: "municipality",
    style: { backgroundColor: "gray", textColor: "black" },
  },
  {
    option: "A city plaza",
    style: { backgroundColor: "lightgreen", textColor: "black" },
  },
];

const Redemption = () => {
  const [spinning, setSpinning] = useState(true);
  return (
    <div style={{ paddingTop: "48px" }}>
      <Row gutter={[24, 24]} justify="center">
        <Col span={24}>
          <div
            style={{
              display: "block",
              marginLeft: "auto",
              marginRight: "auto",
              width: "fit-content",
            }}
          >
            <Wheel
              mustStartSpinning={true}
              prizeNumber={2}
              data={data}
              backgroundColors={["#3e3e3e", "#df3428"]}
              textColors={["#ffffff"]}
              onStopSpinning={() => setSpinning(false)}
              radiusLineColor={"#eeee"}
              outerBorderColor={"#eeee"}
            />
          </div>
        </Col>
        <Col span={12} style={{ textAlign: "center" }}>
          {!spinning && (
            <div className={styles.bg}>
              <Typography.Title level={1} style={{ color: "white" }}>
                You've got a pass a visit to <strong>a beautiful park</strong>.
              </Typography.Title>
              <Typography.Title level={4} style={{ color: "white" }}>
                We hope you have a very pleasant day and have lots of fun
                playing in the trees. There may or may not be a beautiful pond
                nearby with ducks and frogs, with really beautiful scenery. The
                greenery in the park is very soothing to the eyes.
              </Typography.Title>
            </div>
          )}
        </Col>
      </Row>
    </div>
  );
};

export default Redemption;
