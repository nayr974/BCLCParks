import PropTypes from "app/prop-types";
import styles from "./TreeIcon.module.css";

const propTypes = {
  index: PropTypes.string.isRequired,
  small: PropTypes.bool,
};

const defaultProps = {
  small: false,
};

const TreeIconPath = (index) =>
  ({
    0: "/img/tree1.svg",
    1: "/img/tree2.svg",
    2: "/img/tree3.svg",
    3: "/img/tree4.svg",
    4: "/img/tree5.svg",
    5: "/img/tree6.svg",
    6: "/img/tree7.svg",
    7: "/img/tree8.svg",
    8: "/img/tree9.svg",
    9: "/img/tree10.svg",
    10: "/img/tree1.svg",
    11: "/img/tree2.svg",
    12: "/img/tree3.svg",
    13: "/img/tree4.svg",
    14: "/img/tree5.svg",
    15: "/img/tree6.svg",
    16: "/img/tree7.svg",
    17: "/img/tree8.svg",
    18: "/img/tree9.svg",
    19: "/img/tree10.svg",
  }[index]);

const TreeIcon = (props) => (
  <img
    className={props.small ? styles.small : styles.large}
    src={TreeIconPath(props.index)}
    alt="Priority"
  />
);

TreeIcon.propTypes = propTypes;
TreeIcon.defaultProps = defaultProps;

export default TreeIcon;
