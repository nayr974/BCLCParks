import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Space, Row, Col, Typography } from "antd";
import { groupBy, uniq } from "lodash";
import styles from "./Admin.module.css";
import { selectReservations, getReservations } from "app/bookingSlice";

const mock = [
  {
    id: "1",
    email: "1",
    phone_no: "1",
    passcode: "1",
    trailhead_id: "1",
    date: "2020-01-01",
    am_or_pm: true,
    booking_type: "VEHICLE",
    num_of_persons: "3",
    vehicle_license_plate: "123",
    application_datetime: "2020-01-01",
    state: "WAITING",
  },
];

const Admin = () => {
  const dispatch = useDispatch();
  const [loaded, setLoaded] = useState(false);
  const reservations = useSelector(selectReservations);
  if (!loaded) {
    dispatch(getReservations());
    setLoaded(true);
  }
  return !loaded ? (
    <div>Loading.</div>
  ) : (
    <div style={{ paddingTop: "48px" }}>
      <Row gutter={[24, 24]} justify="center">
        <Col span={24}>
          WUT
          {reservations &&
            reservations.map((reservation) => JSON.stringify(reservation))}
        </Col>
      </Row>
    </div>
  );
};

export default Admin;
