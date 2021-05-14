import { useSelector, useDispatch } from "react-redux";
import {
  selectTaskBoard,
  addLane,
  moveTask,
  saveTaskBoard,
  resetTaskBoard,
} from "app/taskBoardSlice";
import Park from "components/park/Park";
import styles from "./BookingBoard.module.css";
import AddButtonOutlined from "components/common/AddButtonOutlined";
import { Button, Popconfirm, Space, Row, Col } from "antd";
import { groupBy, uniq } from "lodash";

const data = [
  {
    id: "1",
    park_name: "Park1",
    trailhead_name: "Trail1",
    am_capacity: 5,
    pm_capacity: 25,
    capacity_type: "VEHICLE",
  },
  {
    id: "2",
    park_name: "Park1",
    trailhead_name: "Trail1",
    am_capacity: 5,
    pm_capacity: 25,
    capacity_type: "PERSON",
  },
  {
    id: "3",
    park_name: "Park2",
    trailhead_name: "Trail1",
    am_capacity: 5,
    pm_capacity: 25,
    capacity_type: "PERSON",
  },
];

const parks = uniq(data.map((park) => park.park_name));
const trailHeads = groupBy(data, "park_name");

const BookingBoard = () => {
  const taskBoard = useSelector(selectTaskBoard);
  const dispatch = useDispatch();

  return (
    <Row gutter={[24, 24]}>
      {parks.map((park) => (
        <Col span={12}>
          <Park parkName={park} trailHeads={trailHeads[park]} />
        </Col>
      ))}
    </Row>
  );
};

export default BookingBoard;
