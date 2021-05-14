import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";

import Park from "components/park/Park";
import styles from "./BookingBoard.module.css";
import { Button, Popconfirm, Space, Row, Col } from "antd";
import { groupBy, uniq } from "lodash";
import { selectTrails, getTrails } from "app/bookingSlice";

const BookingBoard = () => {
  const trails = useSelector(selectTrails);
  const dispatch = useDispatch();
  const [loaded, setLoaded] = useState(false);

  if (!loaded) {
    dispatch(getTrails());
    setLoaded(true);
  }

  const parks =
    !loaded || !trails ? [] : uniq(trails.map((park) => park.park_name));
  const trailHeads = !loaded || !trails ? [] : groupBy(trails, "park_name");

  return (
    <Row gutter={[24, 24]}>
      <Col span={24} justify="center">
        <div
          style={{
            display: "block",
            marginLeft: "auto",
            marginRight: "auto",
            width: "fit-content",
            marginTop: "calc(50vh - 200px)",
            marginBottom: "calc(50vh - 200px)",
          }}
        >
          <img
            src={"/img/BCLC_Logo.svg"}
            style={{ height: "120px" }}
            alt="BC(LC)Parks Logo"
          />
          <img
            src={"/img/logo-bcparks-text.png"}
            style={{ height: "120px" }}
            alt="BC(LC)Parks Logo"
          />
          <div className={styles.titleContainer}>
            <span className={styles.subtitle}>
              Your chance to win a <strong>lifetime experience</strong> at a BC
              park.
            </span>
          </div>
        </div>
      </Col>
      {loaded &&
        parks.map((park, index) => (
          <Col span={12}>
            <Park index={index} parkName={park} trailHeads={trailHeads[park]} />
          </Col>
        ))}
    </Row>
  );
};

export default BookingBoard;
