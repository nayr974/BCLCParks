import React, { useState } from "react";
import { useDispatch } from "react-redux";

import PropTypes from "app/prop-types";
import styles from "./Park.module.css";
import { Card, Modal, Button, Typography } from "antd";
import { EditOutlined, DeleteOutlined } from "@ant-design/icons";
import ParkReservation from "./ParkReservation";
import { submitReservation } from "app/bookingSlice";
import TreeIcon from "./TreeIcon";

const propTypes = {
  index: PropTypes.number.isRequired,
  parkName: PropTypes.any.isRequired,
  trailHeads: PropTypes.any.isRequired,
};

const Park = (props) => {
  const dispatch = useDispatch();
  const [booking, setBooking] = useState(false);
  const [trailhead, setTrailhead] = useState();
  const [am_or_pm, setAmPm] = useState(false);

  const initialValues = trailhead && {
    ...trailhead,
    am_or_pm,
    trailhead_id: trailhead?.id,
    booking_type: trailhead?.capacity_type,
  };
  return (
    <>
      <Card
        hoverable
        className={styles.park}
        title={<h1 className={styles.white}>{props.parkName}</h1>}
        extra={<TreeIcon index={props.index} />}
      >
        {props.trailHeads.map((trail) => (
          <Card.Grid className={styles.cardgrid}>
            <Typography.Title
              level={5}
            >{`${trail.trailhead_name} (${trail.capacity_type})`}</Typography.Title>
            {trail.am_capacity && (
              <Button
                type="ghost"
                style={{ color: "white" }}
                block
                onClick={() => {
                  setTrailhead(trail);
                  setAmPm(false);
                  setBooking(true);
                }}
              >
                Early Bird
              </Button>
            )}
            {trail.pm_capacity && (
              <Button
                type="ghost"
                block
                style={{ marginTop: "5px", color: "white" }}
                onClick={() => {
                  setTrailhead(trail);
                  setAmPm(false);
                  setBooking(true);
                }}
              >
                Night Owl
              </Button>
            )}
          </Card.Grid>
        ))}
      </Card>
      {trailhead && (
        <Modal
          title="Park Reservation"
          visible={booking}
          width="50vw"
          onCancel={() => setBooking(false)}
          footer={null}
        >
          <ParkReservation
            initialValues={initialValues}
            onFinish={(values) => {
              dispatch(submitReservation(values));
              setBooking(false);
            }}
          />
        </Modal>
      )}
    </>
  );
};

Park.propTypes = propTypes;

export default Park;
