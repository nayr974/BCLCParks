import { useSelector, useDispatch } from "react-redux";
import {
  selectTaskBoard,
  addLane,
  moveTask,
  saveTaskBoard,
  resetTaskBoard,
} from "app/taskBoardSlice";
import Lane from "components/lane/Lane";
import styles from "./TaskBoard.module.css";
import { DragDropContext } from "react-beautiful-dnd";
import AddButtonOutlined from "components/common/AddButtonOutlined";
import { Button, Popconfirm, Space } from "antd";

const TaskBoard = () => {
  const taskBoard = useSelector(selectTaskBoard);
  const dispatch = useDispatch();

  return (
    <DragDropContext onDragEnd={(result) => dispatch(moveTask(result))}>
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
            <span className={styles.subtitle}>{taskBoard.subtitle}</span>
          </div>
          <Space className={styles.buttons}>
            <div></div>
          </Space>
        </div>
        <div className={styles.taskboard}>
          {taskBoard.lanes?.map((lane) => (
            <Lane key={lane.id} lane={lane} />
          ))}
          <AddButtonOutlined
            label="Add another lane"
            onClick={() => dispatch(addLane())}
          />
        </div>
      </div>
    </DragDropContext>
  );
};

export default TaskBoard;
