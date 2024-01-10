import styles from "/Users/wiz/Desktop/untitled folder 10/FullStack-ScrapyDjango/FrontEnd/src/components/modules/Card.module.css";

import { sp } from "../../utils/replaceNumber";

const Card = ({ data: {_id ,title, area, construction_year, rooms,price,floor,elevator,parking,warehouse } }) => {
 

  return (
    <div className={styles.container}>
      <p className={styles.title}>{title}</p>
      <p className={styles.location}>
        {area}
      </p>
      <p className={styles.title}>{construction_year}</p>
      <p className={styles.title}>{rooms}</p>
      <p className={styles.title}>{floor}</p>
      <p className={styles.title}>{elevator}</p>
      <p className={styles.title}>{parking}</p>
      <p className={styles.title}>{warehouse}</p>
      <span>{sp(price)} تومان</span>

    </div>
  );
};

export default Card;