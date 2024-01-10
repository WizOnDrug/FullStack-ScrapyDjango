
import Card from "../modules/Card";


const DivarPage = ({ data }) => {
  return (
    <div className={styles.container}>
      <div className={styles.main}>
        {data.length ? null : (
          <p className={styles.text}>هیچ آگهی ثبت نشده است</p>
        )}
        {data.map((profile) => (
          <Card key={profile._id} data={profile} />
        ))}
      </div>
    </div>
  );
};

export default DivarPage;