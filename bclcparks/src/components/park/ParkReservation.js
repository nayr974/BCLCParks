import React, { useState } from "react";
import { Button, Input, Radio, Form, Space } from "antd";
import { SaveOutlined } from "@ant-design/icons";
import { CKEditor } from "@ckeditor/ckeditor5-react";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";

import PropTypes from "app/prop-types";
import TaskPriorityIcon from "./TaskPriorityIcon";

const propTypes = {
  initialValues: PropTypes.any.isRequired,
  onFinish: PropTypes.func.isRequired,
};

const ParkReservation = (props) => {
  const [form] = Form.useForm();
  return (
    <div>
      <Form
        form={form}
        layout="vertical"
        initialValues={props.task}
        onFinish={(values) => {
          props.onFinish(values);
        }}
      >
        <Form.Item hidden name="trailhead_id" rules={[{ required: true }]} />
        <Form.Item hidden name="am_or_pm" rules={[{ required: true }]} />
        <Form.Item hidden name="booking_type" rules={[{ required: true }]} />

        <Form.Item label="Email:" name="email" rules={[{ required: true }]}>
          <Input />
        </Form.Item>

        <Form.Item label="Phone:" name="phone_no" rules={[{ required: true }]}>
          <Input />
        </Form.Item>

        {props.initialValues.booking_type === "PERSON" && (
          <Form.Item
            label="Number of people:"
            name="num_of_persons"
            rules={[{}]}
          >
            <Input />
          </Form.Item>
        )}

        {props.initialValues.booking_type === "VEHICLE" && (
          <Form.Item
            label="Vehicle license plate"
            name="vehicle_licence_plate"
            rules={[{}]}
          >
            <Input />
          </Form.Item>
        )}

        <Form.Item style={{ textAlign: "right" }}>
          <Button type="primary" htmlType="submit">
            <SaveOutlined />
            Submit Reservation Request
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};

ParkReservation.propTypes = propTypes;

export default ParkReservation;
